import discord, os
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Allowed channel for the /use command
ALLOWED_CHANNEL_ID = 1408116182942482442  

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"✅ Logged in as {bot.user}")
    print(f"🔗 Synced commands: {[cmd.name for cmd in synced]}")

@bot.tree.command(name="use", description="Get instructions for using Bwah Tool's")
async def use(interaction: discord.Interaction):
    if interaction.channel_id != ALLOWED_CHANNEL_ID:
        await interaction.response.send_message(
            "❌ You can only use this command in <#1408116182942482442>.",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        "To use **Bwah Tool's** click "
        "[here](https://drive.google.com/drive/u/0/folders/1alck_TnS4O34Y3q2nWal9p0bFmMeAfq8) "
        "to download, and then run `index.html` in the folder."
    )

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
