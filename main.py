import discord
from discord import app_commands
from discord.ext import commands
import os

# -------------------------
# Bot Setup
# -------------------------
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# -------------------------
# On Ready
# -------------------------
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔗 Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

# -------------------------
# Slash Command
# -------------------------
@bot.tree.command(name="use", description="Get instructions for using Bwah Tool's")
async def use(interaction: discord.Interaction):
    await interaction.response.send_message(
        "To use **Bwah Tool's** click [here](https://drive.google.com/drive/u/0/folders/1alck_TnS4O34Y3q2nWal9p0bFmMeAfq8) "
        "to download, and then run `index.html` in the folder."
    )

# -------------------------
# Run Bot
# -------------------------
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
