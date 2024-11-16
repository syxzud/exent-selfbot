import holder
import requests
import json

exent = holder.bot

@exent.command()
async def insult(ctx):
    await ctx.message.delete()
    
    insultURL = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    insult = insultURL.json()["insult"]

    await ctx.send(insult)