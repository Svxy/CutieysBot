import psutil
import os
from datetime import datetime
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.process = psutil.Process(os.getpid())

    @commands.Cog.listener()
    async def on_command(self, ctx):
        try:
            print(
                f"{ctx.guild.name} > {ctx.author} > {ctx.message.clean_content}"
            )
        except AttributeError:
            print(
                f"Private message > {ctx.author} > {ctx.message.clean_content}"
            )

    @commands.Cog.listener()
    async def on_ready(self):
        if not hasattr(self.bot, "uptime"):
            self.bot.uptime = datetime.now()

        print(f"Ready: {self.bot.user} | Servers: {len(self.bot.guilds)}")


def setup(bot):
    bot.add_cog(Events(bot))
