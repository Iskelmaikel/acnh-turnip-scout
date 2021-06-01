from requests import get
import config
from datetime import datetime

def sendText(title, price, created, shortlink):
    # Globally store values from config instead of adding per request
    token = config.read_config('TELEGRAMCONFIG', 'token')
    chatID = config.read_config('TELEGRAMCONFIG', 'chatID')

    created = datetime.fromtimestamp(created)
    multilinemsg = """I found a nice offer! I think the price is {price}.
    
This is what it says: {title}

Posted on: {created}

Here's the link if you want to check it out:
{shortlink}""".format(price=price, title=title, created=created, shortlink=shortlink)

    # urlencode msg for safety
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + multilinemsg

    response = get(send_text)

    if response.status_code == 200:
        print("[TG] - Message sent correctly")
        return True
    else:
        print("[TG] - Error while sending the message")
        return False