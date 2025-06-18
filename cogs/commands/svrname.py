import discord
from discord.ext import commands

class Svrname(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="svrname", aliases=["Servername"])
    async def svrname(self, ctx):
        await ctx.send(
            f"**Server Name**: `{ctx.guild.name}`\n"
            f"**Server ID**: `{ctx.guild.id}`\n\nSPX OP"
        )

# Make sure to add the Cog
def setup(bot):
    bot.add_cog(Svrname(bot))