# Discord Bot Base

This is a basic Discord bot written in Python using the `discord.py` library. It provides a starting point for building a bot with modular functionality and the ability to load plugins.

## Features

- Responds to commands like ping and echo.
- Supports loading plugins from the "plugins" folder.
- Easily customizable and expandable.

## Requirements

- Python 3.x
- discord.py library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Avista-Technologies/base-discord-bot
```

2. Navigate to the project directory:
```bash
cd base-discord-bot
```

3. Install the dependencies:
```bash
pip -r requirements.txt
```

4. Obtain a Discord bot token:

- Create a new bot on the Discord Developer Portal.
- Copy the bot token.

5. Configure the bot:

- Open the `main.py` file and replace `"YOUR_DISCORD_TOKEN"` with your bot token.

6. Run the bot:
```bash
python discordbot.py
```

## Usage

- Customize the bot's behavior by modifying the `main.py` file and adding commands or event handlers.
- Create separate plugin files in the "plugins" folder to add additional functionality.
- Refer to the `discord.py` documentation for more information on how to extend the bot's capabilities.

## Contributing

Contributions are welcome! If you find any issues or want to suggest improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

