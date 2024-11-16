from discord.ext import commands
import discord
import globals
import datetime
import requests
import re
from colorama import Fore

bot = commands.Bot(command_prefix=globals.prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(Fore.WHITE+f"\n\n\n["+Fore.GREEN+"+"+Fore.WHITE+"]"+Fore.WHITE+"    Logged in as "+Fore.YELLOW+f"{bot.user}"+Fore.WHITE+"  |   ID: "+Fore.YELLOW+f"{bot.user.id}"+Fore.WHITE)
