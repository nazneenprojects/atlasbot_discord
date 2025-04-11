# atlasbot_discord
AtlasBot is a feature-rich Discord bot built with Python and discord.py, designed to support hybrid commands (prefix + slash), lightweight data storage using JSON, and modular functionality through dynamic cog loading.


## Prerequisites:

#### Set Up Discord Bot 

Go to the Discord Developer Portal

Create a new application

Go to the Bot tab → Create a bot

Under Privileged Gateway Intents, turn ON:

✅ MESSAGE CONTENT INTENT

✅ SERVER MEMBERS INTENT (just in case for future features)

Copy the bot token and paste it into your script.

#### Invite the Bot to Your Server
Go to OAuth2 > URL Generator, then:

Scopes: bot, applications.commands

Bot Permissions: at least Send Messages, Read Messages, etc.

Use the generated URL to invite your bot to your server.


## Steps
1. Clone this code repository
2. grab the discord bot token from your discord dev account and past into .env file
3. install dependence - pip install -U discord.py. Verify -: pip show discord.py
4. install pip install python-dotenv
5. run the code :
6. Once the bot is online, go to your Discord server and try:

!prefix_store test hello

/hybrid_store test world (you'll need to type / in the chat and select your bot’s slash command)

If nothing appears for the slash command initially, give Discord a few seconds to sync it.

Refer - You can watch Demo of how boat works by watching this video recording - bot_harz/recording_harzbot.mp4

