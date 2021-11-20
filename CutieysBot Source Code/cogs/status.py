import discord
import json
from discord.ext import commands, tasks
from itertools import cycle

with open('config.json', 'r') as config:
    get = json.load(config)

status1 = get['status1']
status2 = get['status2']
status3 = get['status3']
status4 = get['status4']
status5 = get['status5']


class Status(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.status = cycle([status1, status2, status3, status4, status5])

    @tasks.loop(seconds=2.8)
    async def change_status(self):
        await self.client.change_presence(
            activity=discord.Game(next(self.status)))

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        self.change_status.start()


def setup(client):
    client.add_cog(Status(client))
