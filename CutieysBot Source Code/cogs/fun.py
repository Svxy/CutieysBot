import random
import json
from discord.ext import commands

with open('config.json', 'r') as config:
    get = json.load(config)

response_one = get['8ball_response_one']
response_two = get['8ball_response_two']
response_three = get['8ball_response_three']
response_four = get['8ball_response_four']
response_five = get['8ball_response_five']
response_six = get['8ball_response_six']
response_seven = get['8ball_response_seven']
response_eight = get['8ball_response_eight']
response_nine = get['8ball_response_nine']
response_ten = get['8ball_response_ten']


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    @commands.guild_only()
    async def _8ball(self, ctx, *, question):
        responses = [
            f'{response_one}',
            f'{response_two}',
            f'{response_three}',
            f'{response_four}',
            f'{response_five}',
            f'{response_six}',
            f'{response_seven}',
            f'{response_eight}',
            f'{response_nine}',
            f'{response_ten}',
        ]
        await ctx.reply(f'{random.choice(responses)}')

    @commands.command(aliases=['rps'])
    @commands.guild_only()
    async def rockpaperscissors(self, ctx, *, player_choice):
        options = ["rock", "paper", "scissors"]
        choice = random.choice(options)
        if player_choice in options:
            if player_choice == choice:
                await ctx.reply(
                    f'**Draw! Nobody wins.** Bot chose {choice} and you chose {player_choice}'
                )
            elif player_choice == "rock" and choice == "scissors":
                await ctx.reply(
                    f'**You win!** Bot chose {choice} and you chose {player_choice}'
                )
            elif player_choice == "paper" and choice == "rock":
                await ctx.reply(
                    f'**You win!** Bot chose {choice} and you chose {player_choice}'
                )
            elif player_choice == "scissors" and choice == "paper":
                await ctx.reply(
                    f'**You win!** Bot chose {choice} and you chose {player_choice}'
                )
            else:
                await ctx.reply(
                    f'**You Lose! ..to a bot lmao** Bot chose {choice} and you chose {player_choice}'
                )
        else:
            await ctx.reply(
                f"Invalid syntax\nUsage: `$rps rock` `$rps paper` `$rps scissors`"
            )

    @commands.command(aliases=['cf'])
    @commands.guild_only()
    async def coinflip(self, ctx):
        responses = ['Heads', 'Tails']
        await ctx.reply(f'{random.choice(responses)}')

    @commands.command()
    @commands.guild_only()
    async def f(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**{ctx.author.name}** has paid their respect")

    @commands.command(aliases=['calc'])
    @commands.guild_only()
    async def calculate(self, ctx, *, question):
        try:
            await ctx.reply(f'{str(eval(question))}')
        except:
            await ctx.reply(
                "Error\n\nPlease make sure to enter a possible question containing only number and  `+` `-` `*` `/` `.`"
            )


def setup(client):
    client.add_cog(Fun(client))
