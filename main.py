import os
import discord
from discord.ext import commands
from discord import app_commands

# ---------------------------
# Intents
# ---------------------------
intents = discord.Intents.default()
intents.message_content = True

# ---------------------------
# Bot Setup
# ---------------------------
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# Only allow commands in this channel
ALLOWED_CHANNEL_ID = 1408116182942482442

# ---------------------------
# Slash Command
# ---------------------------
@tree.command(name="connect_bwah", description="Connect your Bwah account")
async def connect_bwah(interaction: discord.Interaction):
    if interaction.channel.id != ALLOWED_CHANNEL_ID:
        await interaction.response.send_message("You can't use this command here.", ephemeral=True)
        return

    # Simulate connection process
    # Replace this with your actual Bwah API interaction
    await interaction.response.send_message(f"{interaction.user.mention}, connected to Bwah account successfully!")

# ---------------------------
# Event: on_ready
# ---------------------------
@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user}")

# ---------------------------
# Start Bot
# ---------------------------
TOKEN = os.getenv("DISCORD_TOKEN")  # Set this in Railway's ENV variables
bot.run(TOKEN)
