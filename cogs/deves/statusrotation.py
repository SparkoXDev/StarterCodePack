import discord
from discord.ext import commands, tasks
import itertools
import random

class StatusSetter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_status.start()

    def cog_unload(self):
        self.update_status.cancel()

    @tasks.loop(seconds=4)
    async def update_status(self):
        total_users = sum(g.member_count or 0 for g in self.bot.guilds)
        total_guilds = len(self.bot.guilds)

        # Dynamically rotate between multiple status types
        statuses = [
            discord.Game("With Channels"),
            discord.Activity(type=discord.ActivityType.watching, name=f"{total_guilds} Servers."),
            discord.Activity(type=discord.ActivityType.listening, name=f"{total_users} Users."),
            discord.Streaming(name="Channel Manager.", url="https://twitch.tv/lol")
        ]

        await self.bot.change_presence(activity=random.choice(statuses))

    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()