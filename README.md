# atlasbot_discord
AtlasBot is a feature-rich Discord bot built with Python and discord.py, designed to support hybrid commands (prefix + slash), lightweight data storage using JSON, and modular functionality through dynamic cog loading.


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

