from requests import get
import config


def sendText(msg, price, url):
    # Globally store values from config instead of adding per request
    token = config.read_config('TELEGRAMCONFIG', 'token')
    chatID = config.read_config('TELEGRAMCONFIG', 'chatID')

    multilinemsg = """I found a nice offer! I think the price is {price}.
    
This is what it says: {msg}

Here's the link if you want to check it out:
{url}""".format(price=price, msg=msg, url=url)

    # urlencode msg for safety
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + multilinemsg

    response = get(send_text)

    return response.json()