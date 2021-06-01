# Animal Crossing Turnip Price Scout
Turnip Price Scout (TPS) is a python application that scouts turnip prices by crawling the /r/turnipexchange subreddit.
It scouts the subreddit at given intervals and keeps track of turnip prices. When new offers are found, it will send
messages to the configured telegram account.

## Installation

1. Use a package manager like [pip](https://pip.pypa.io/en/stable/) to install the projects requirements.

```bash
pip install -r requirements.txt
```

2. Modify the contents of config.ini to include your reddit api key and telegram token and chat id.
2a. You can generate a new Reddit app [here](https://www.reddit.com/prefs/apps). Scroll down and click 'Create another application'. Follow the instructions
2b. You can create a new Telegram bot [here](https://core.telegram.org/bots#6-botfather). Follow the instructions. To find your chat ID, talk with Telegram's 'userinfobot'.


```
[REDDITCONFIG]
client_id = your id
client_secret = your secret
user_agent = turnip scout
post_count = 10
subreddit = acturnips

[TELEGRAMCONFIG]
token = your token
chatID = your id
```


## Usage

from the root directory run the following command in cmd/Powershell or terminal.

```python
python main.py
```

tip: do not forget to start your telegram bot you've set up in the installation phase.

If the configuration is done well you should end up with a Telegram bot that looks like the following

![image](https://user-images.githubusercontent.com/7192304/120298877-be7d5800-c2ca-11eb-9db3-0c6647bb396c.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

<a href="https://www.buymeacoffee.com/iskelmaikel" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174">

## License
None yet. Feel free to use this.
