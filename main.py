import discord
from discord.ext import commands

from cmds import *

TOKEN="MTEwNDk2ODU1MDUzMzMxMjYyNA.GlaTTW.cKDsg6zd39bdYJH35yuMhh-JW0QVJ4ZweVCcGE"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(intents=intents, command_prefix='!')

@client.event
async def on_ready():
    print("READY")

kick.kick(client, discord)
ban.ban(client, discord)

client.run(TOKEN)