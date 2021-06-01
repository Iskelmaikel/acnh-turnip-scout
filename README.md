# Animal Crossing Turnip Price Scout

Turnip Price Scout (TPS) is a Python application that scouts turnip prices by crawling your favorite subreddits. By default the application scouts the [/r/acturnips](https://www.reddit.com/r/acturnips/) subreddit.

It scouts the subreddit at given intervals and keeps track of turnip prices. When new offers are found, it will send
messages to the configured Telegram account.

## Installation

1. Clone/download the repository and navigate into it

    ```bash
    git clone https://github.com/Iskelmaikel/acnh-turnip-scout.git && cd acnh-turnip-scout
    ```

2. Use a package manager like [pip](https://pip.pypa.io/en/stable/) to install the projects requirements.

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/) (on Windows, make sure you add it to PATH during installation)

3. Modify the contents of `config.ini` to include your Reddit API key and Telegram bot token and chat ID.

    ```ini
    [REDDITCONFIG]
    client_id = your app id (below personal use script)
    client_secret = your secret
    user_agent = turnip scout
    post_count = 10
    subreddit = acturnips

    [TELEGRAMCONFIG]
    token = your bot token
    chatID = your chat id
    ```

    1. You can generate a new Reddit app key [here](https://www.reddit.com/prefs/apps). Scroll down and click 'Create another application'.
        1. Give it a **name** of your choice like `acnh turnip scout`
        2. Select type `script`
        3. You can leave **description** and **about url** empty
        4. The **redirect uri** is mandatory but its value doesn't really matter, you can use `http://localhost:8080`
    2. Replace the `client_id` field with the alphanumeric string below **personal use script**
    3. Replace the `client_secret` field with the alphanumeric string on the right side of **secret**
    4. You can create a new Telegram bot [here](https://core.telegram.org/bots#6-botfather). Follow the instructions. To find your chat ID, talk with Telegram's 'userinfobot'.

**NB: after having configured the Telegram bot, open a new chat with the bot and send `/start` or you won't be receiving messages!**

## Usage

From the root directory, double click on `main.py` or run the following command in cmd/Powershell or terminal.

```bash
python main.py
```

If the configuration is done well you should end up with a Telegram bot that looks like the following

![image](https://user-images.githubusercontent.com/7192304/120298877-be7d5800-c2ca-11eb-9db3-0c6647bb396c.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

<a href="https://www.buymeacoffee.com/iskelmaikel" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174">

## License

None yet. Feel free to use this.
