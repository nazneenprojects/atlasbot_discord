import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv




# Enable all intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


# Database (JSON) Handling
def load_db():
    try:
        with open('database.json', 'r') as f:
            bot.db = json.load(f)
    except FileNotFoundError:
        bot.db = {}

def save_db():
    with open('database.json', 'w') as f:
        json.dump(bot.db, f, indent=4)


# Cog Loading
async def load_cogs():
    for filename in os.listdir("./cog"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"cog.{filename[:-3]}")
                print(f"Loaded cog: {filename[:-3]}")
            except commands.ExtensionError as e:
                print(f"Failed to load cog {filename[:-3]}. Reason: {e}")


# Bot Events
@bot.event
async def on_ready():
    load_db()  # Load database on startup
    await load_cogs()
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


# Example Command (Prefix)
@bot.command()
async def prefix_store(ctx, key: str, value: str):
    bot.db[f"prefix_{key}"] = value
    save_db()
    await ctx.send(f"Stored (prefix): {key} = {value}")


# Example Command (Hybrid - works as both prefix and slash)
@bot.hybrid_command(name="hybrid_store", description="Stores data (works as prefix and slash)")
async def hybrid_store(ctx: commands.Context, key: str, value: str):
    bot.db[f"hybrid_{key}"] = value
    save_db()
    await ctx.send(f"Stored (hybrid): {key} = {value}")


@bot.event
async def on_message(message):
    # This line is important for processing prefix commands
    await bot.process_commands(message)

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

bot.run(bot_token)