import discord
from discord.ext import commands

ALLOWED_CHANNEL_ID = 1408116182942482442

bot = commands.Bot(command_prefix="!")

# Store user tokens securely (in-memory example)
linked_accounts = {}  # {discord_user_id: user_token}

@bot.command(name="connect_bwah")
async def connect_bwah(ctx, token: str):
    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        await ctx.send("You can't use this command in this channel.")
        return

    linked_accounts[ctx.author.id] = token
    await ctx.send(f"{ctx.author.display_name}, your Bwah account is now linked! ✅")

@bot.command(name="status_bwah")
async def status_bwah(ctx):
    if ctx.author.id in linked_accounts:
        await ctx.send(f"{ctx.author.display_name}, you are connected! ✅")
    else:
        await ctx.send(f"{ctx.author.display_name}, you are not connected. ❌")

bot.run("YOUR_DISCORD_BOT_TOKEN")
