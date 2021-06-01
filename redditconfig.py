import praw
import base64
import botconfig as telegram
import database as db
from PIL import Image
#from pytesseract import pytesseract
#import requests
import re
import config



reddit = praw.Reddit(
    client_id = config.read_config('REDDITCONFIG', 'client_id'),
    client_secret = config.read_config('REDDITCONFIG', 'client_secret'),
    user_agent = config.read_config('REDDITCONFIG', 'user_agent')
)
encodingType = 'utf-8'
subreddit = config.read_config('REDDITCONFIG', 'subreddit')
minimum_price = config.read_config('REDDITCONFIG', 'minimum_price')
savedPosts = []


def base64String(value, shouldDecode):
    if(shouldDecode == 'true'):
        return value.decode(encodingType)
    else:
        message_bytes = value.encode(encodingType)
        return base64.b64encode(message_bytes)

def encodeString(str):
    message_bytes = str.encode(encodingType)
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes


def decodeString(base64EncryptedString):
    base64_message = base64EncryptedString.decode(encodingType)
    decoded_string = base64.b64decode(base64_message)
    return decoded_string


# Used as a last resort to find the price from the image if it cannot be found in the submission title
# temporarily disabled
#def extract_text(url):
#    # Uses tesseract from following lib. Needs to be installed locally -> https://github.com/UB-Mannheim/tesseract/wiki
#    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#    image_path = url
#    img_data = requests.get(url).content
#    filename = url.split('/')[-1]
#    if filename:
#        with open(filename, 'wb') as handler:
#            handler.write(img_data)
#
#        img = Image.open(filename)
#        pytesseract.tesseract_cmd = path_to_tesseract
#
#        text = pytesseract.image_to_string(img)
#        return text[:-1]


def evaluatePosts():
    postcount = int(config.read_config('REDDITCONFIG', 'post_count'))
    if not postcount:
        postcount = 10

    for submission in reddit.subreddit(subreddit).new(limit=postcount):
        biggestNumber = 0
        numbers = re.findall(r'\d+', submission.title)

        if numbers:
            for num in numbers:
                if int(num) > int(biggestNumber):
                    biggestNumber = num

        else:
            print("Couldn't find price...")
            # OCR temporarily disabled until included in requirements
            continue

        isAdded = db.add_turnips(submission.title, submission.created, submission.shortlink)

        if isAdded == 'false':
            return
        else:
            if int(biggestNumber) >= int(minimum_price):
                telegram.sendText(submission.title, biggestNumber, submission.shortlink)
            else:
                print("Price is lower than minimum value. No notification")
