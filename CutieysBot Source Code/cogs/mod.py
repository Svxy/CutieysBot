import discord
from discord.ext import commands


class Moderator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Deleted {amount} messages')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.kick(reason=reason)
        await ctx.send(f':hammer: {member.mention} has been kicked.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.ban(reason=reason)
        await ctx.send(f':hammer: {member.mention} has been banned.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} has been unbanned.')

    @commands.command(aliases=["nick"])
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, name: str = None):
        await member.edit(nick=name)
        message = f"Changed {member.mention}'s nickname to **{name}**"
        if name is None:
            message = f"Reset {member.mention}'s nickname"
        await ctx.reply(message)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason: str = None):
        muted_role = next((g for g in ctx.guild.roles if g.name == "Muted"),
                          None)
        if not muted_role:
            return await ctx.send("There is no role called **Muted**")
        try:
            await member.add_roles(muted_role, reason=reason)
            await ctx.send(f"{member.mention} has been muted lmaoo.")
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason: str = None):
        muted_role = next((g for g in ctx.guild.roles if g.name == "Muted"),
                          None)
        if not muted_role:
            return await ctx.send("There is no role called **Muted**")
        try:
            await member.remove_roles(muted_role, reason=reason)
            await ctx.send(
                f"{member.mention} has been unmuted. now dont be dumb...")
        except Exception as e:
            await ctx.send(e)


def setup(client):
    client.add_cog(Moderator(client))
