import holder
import requests
import globals
from colorama import Fore

exent = holder.bot


@exent.command()
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.session()
    headers = {
        'Authorization': globals.token,
        'Content-Type': 'application/json'
    }

    global payload
    
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}

    try:
        requests.post('https://discordapp.com/api/v9/hypesquad/online', headers=headers, json=payload)
        print(f"Attempted set your HypeSquad house to {house}!")
    except:
        print(f"Failed to set your HypeSquad house to {house}.")