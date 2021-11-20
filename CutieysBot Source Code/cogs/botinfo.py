import discord
import datetime
import json
from datetime import datetime
from discord.ext import commands

with open('config.json', 'r') as config:
    get = json.load(config)

prefix = get['prefix']
code = get['code']
github = get['github']
inv = get['inv']


class BotInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def help(self, ctx):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.add_field(
            name="Moderation:",
            value=
            "`$clear <amount>` - Clear messages from chat\n`$kick <user> <reason>` - Kick a user from the server\n`$ban <user> <reason>` - Ban a user from the server\n`$unban <user>` - Unban a user from the server\n`$mute <user>` -  Mute a user in text & voice channels\n`$unmute <user>` - Unmute a user\n`$nick <user> <nickname>` - Change a users nickname",
            inline=False)
        embed.add_field(
            name="Information:",
            value=
            "`$whois <user>` -  Display server info about a user\n`$av <user>` Display a users pfp\n`$serverinfo` - Display information about the server\n`$users` - Display the number of users in the server",
            inline=False)
        embed.add_field(
            name="Games & Misc:",
            value=
            "`$8ball <question>` - Ask the bot a question\n`$coinflip <heads/tails>` - Flip a coin\n`$rps <choice>` - Play a game of rock paper scissors\n`$F` - Press F to pay respects\n`$calculate <equasion>` - Calculate an equasion",
            inline=False)
        embed.add_field(
            name="Bot-Related:",
            value=
            "`$help` - Display all commands and what they do\n`$uptime` - The amount of time since last restart\n`$ping` - The bots latency / response time\n`$twitch` -  Get a link to owners Twitch",
            inline=False)
        embed.add_field(
            name="↓Recommended↓",
            value=
            "`$invite` - Invite Cutiey's Bot to your server!\n`$customcss` - Get custom OTF CSS & my favorite plugins!",
            inline=False)
        embed.add_field(name="↑Recommended↑", value="ㅤㅤㅤ", inline=False)
        return await ctx.reply(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.reply(
            f'Pong bitch! \({round(self.client.latency * 1000)}ms\)')

    @commands.command()
    @commands.guild_only()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.reply(f"{days}d, {hours}h, {minutes}m, {seconds}s")

    @commands.command(aliases=["code"])
    @commands.guild_only()
    async def twitch(self, ctx):
        embed = discord.Embed(colour=discord.Color.red())
        embed.description = f"[Click here to view bot owners Twitch!]({code})"
        return await ctx.reply(embed=embed)

    @commands.command(aliases=["github"])
    @commands.guild_only()
    async def customcss(self, ctx):
        embed = discord.Embed(colour=discord.Color.red())
        embed.description = f"[Click here for custom OTF CSS, and my favorite plugins!]({github})"
        return await ctx.reply(embed=embed)

    @commands.command(aliases=["inv"])
    @commands.guild_only()
    async def invite(self, ctx):
        embed = discord.Embed(colour=discord.Color.red())
        embed.description = f"Thank you![Click here to invite bot to your server!]({inv})"
        return await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(BotInfo(client))
