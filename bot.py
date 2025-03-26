import discord
from discord.ext import commands

TOKEN = "MTM0MTUxMDQ2ODk0MjA0MTE5OQ.GCJxxz.PtAE0ZnYQ8KAB1eIDcTXYYfsGHWpcz-lRfNpvA"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(MTM0MTUxMDQ2ODk0MjA0MTE5OQ.GCJxxz.PtAE0ZnYQ8KAB1eIDcTXYYfsGHWpcz-lRfNpvA)
