import discord
from discord.ext import commands
import os

# Set the bot's prefix
prefix = "!"

# Create an instance of the bot
bot = commands.Bot(command_prefix=prefix)

# Event: When the bot is ready and connected to the server
@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user.name}")

# Load all plugins from the 'plugins' folder
def load_plugins():
    for filename in os.listdir("./plugins"):
        if filename.endswith(".py"):
            bot.load_extension(f"plugins.{filename[:-3]}")

# Load plugins on bot startup
@bot.event
async def on_connect():
    load_plugins()

# Command: Ping the bot and get a response
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Command: Echo back the user's message
@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

# Run the bot with your Discord bot token
bot.run("YOUR_DISCORD_TOKEN")
