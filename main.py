import discord
from discord.ext import commands
import json
import os

# Intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Path to store tokens
TOKEN_FILE = "bwah_users.json"

# Load existing tokens
if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, "r") as f:
        user_tokens = json.load(f)
else:
    user_tokens = {}

# Command to connect Bwah account
@bot.command(name="connect_bwah")
async def connect_bwah(ctx, token: str):
    user_tokens[str(ctx.author.id)] = token
    with open(TOKEN_FILE, "w") as f:
        json.dump(user_tokens, f, indent=2)
    await ctx.send(f"{ctx.author.mention}, your Bwah account token has been saved!")

# Example command using Bwah token
@bot.command(name="my_bwah_token")
async def my_bwah_token(ctx):
    token = user_tokens.get(str(ctx.author.id))
    if token:
        await ctx.send(f"{ctx.author.mention}, your saved Bwah token is: `{token[:5]}...`")
    else:
        await ctx.send(f"{ctx.author.mention}, you have not connected your Bwah account yet. Use `!connect_bwah <token>`")

# Run bot
bot.run(os.getenv("DISCORD_TOKEN"))
