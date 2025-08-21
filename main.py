from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

tree = bot.tree  # For slash commands

ALLOWED_CHANNEL_ID = 1408116182942482442
linked_accounts = {}

@tree.command(name="connect_bwah", description="Link your Bwah account")
async def connect_bwah(interaction: discord.Interaction, token: str):
    if interaction.channel.id != ALLOWED_CHANNEL_ID:
        await interaction.response.send_message("You can't use this here.", ephemeral=True)
        return
    linked_accounts[interaction.user.id] = token
    await interaction.response.send_message(f"{interaction.user.display_name}, linked! ✅", ephemeral=True)

@tree.command(name="status_bwah", description="Check if your Bwah account is linked")
async def status_bwah(interaction: discord.Interaction):
    if interaction.user.id in linked_accounts:
        await interaction.response.send_message(f"{interaction.user.display_name}, you are connected! ✅", ephemeral=True)
    else:
        await interaction.response.send_message(f"{interaction.user.display_name}, not connected. ❌", ephemeral=True)

@bot.event
async def on_ready():
    await tree.sync()  # Registers the slash commands with Discord
    print(f"Logged in as {bot.user}")

bot.run("YOUR_DISCORD_BOT_TOKEN")
