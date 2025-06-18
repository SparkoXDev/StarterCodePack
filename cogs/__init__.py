import os
from colorama import Fore, Style, init

init(autoreset=True)

from .commands.ping import Ping
from .commands.svrname import Svrname
from .deves.statusrotation import StatusSetter

async def load_cog(bot, cog_cls):
    await bot.add_cog(cog_cls(bot))
    
    name = cog_cls.__name__.lower()

    if "status" in name:
        color = Fore.RED
        status = "Started"
    else:
        color = Fore.GREEN
        status = "Loaded"

    print(f"{color}{status}: {cog_cls.__name__}{Style.RESET_ALL}")

async def setup(bot):
    os.system('cls' if os.name == 'nt' else 'clear')

    await load_cog(bot, Ping)
    await load_cog(bot, Svrname)
    await load_cog(bot, StatusSetter)