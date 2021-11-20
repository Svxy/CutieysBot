import os
import discord
import datetime
import json
from discord.ext import commands
from datetime import datetime

client = discord.Client()

with open('config.json', 'r') as config:
    get = json.load(config)

prefix = get['prefix']
token = get['token']

client = commands.Bot(command_prefix=prefix)
client.launch_time = datetime.utcnow()
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token, bot=True)