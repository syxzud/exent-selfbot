import discord
import globals
from discord.ext import commands
import holder
import logging
import warnings  # Import warnings module

from colorama import Fore
from pystyle import Colors, Colorate
from os import system

from commands import help

#trolling commands ====================
from commands.trolling import token
from commands.trolling import hiddeneveryone

# Misc commands ========================
from commands.misc import ping
from commands.misc import purge
from commands.misc import hypesquad


# raiding commands ====================
from commands.raiding import spam

# fun commands ==========================
from commands.fun import mines
from commands.fun import choose
from commands.fun import howgay
from commands.fun import penis
from commands.fun import randomemoji
from commands.fun import dadjoke
from commands.fun import eightball
from commands.fun import howsimp
from commands.fun import hack
from commands.fun import insult

DEBUG = False

# Suppress all runtime warnings

system("title exent ^| v1.0.0")
system("cls")
banner ="""
    _______  __ _______   ________   ____  ____  ______
   / ____/ |/ // ____/ | / /_  __/  / __ )/ __ \/_  __/
  / __/  |   // __/ /  |/ / / /    / __  / / / / / /   
 / /___ /   |/ /___/ /|  / / /    / /_/ / /_/ / / /    
/_____//_/|_/_____/_/ |_/ /_/    /_____/\____/ /_/     
             -syxz                                                       
"""
gradient = Colorate.Horizontal(Colors.red_to_yellow, banner, 1)
print(gradient)


# Set up logging
if not DEBUG:
    warnings.filterwarnings("ignore")
    # Suppress all loggers with 'discord' in their name
    for name in logging.root.manager.loggerDict.keys():
        if 'discord' in name:
            logger = logging.getLogger(name)
            logger.setLevel(logging.CRITICAL)
            for handler in logger.handlers:
                logger.removeHandler(handler)

# calls ==================================================

# help calls
help.help(None)
help.fun(None)
help.misc(None)
help.trolling(None)
help.raiding(None)

# Misc
ping.ping(None)
hypesquad.hypesquad(None)
#purge.purge(None, None)

# fun
mines.mines(None)
choose.choose(None)
howgay.howgay(None)
penis.penis(None)
randomemoji.randomemoji(None)
dadjoke.dadjoke(None)
eightball.eightball(None)
howsimp.howsimp(None)
hack.hack(None)
insult.insult(None)


# Raiding
spam.spam(None)

# Trolling
hiddeneveryone.hiddeneveryone(None)
token.token(None)

#       ==================================================


# Run the bot
holder.bot.run(globals.token)
