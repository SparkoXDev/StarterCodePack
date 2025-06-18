import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogs import setup
from colorama import init as colorama_init
colorama_init()
from colorama import Fore, Style

# Load .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"""{Fore.YELLOW}
    
   _____ _______   __
  / ____|  __ \ \ / /
 | (___ | |__) \ V / 
  \___ \|  ___/ > <  
  ____) | |    / . \ 
 |_____/|_|   /_/ \_\
                     
                     

    {Style.RESET_ALL}""")
    print(f"✅ Logged in as {bot.user}")


async def main():
    async with bot:
        await setup(bot)
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())