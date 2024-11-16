import holder
import random

exent = holder.bot

@exent.command()
async def randomemoji(ctx):
    await ctx.message.delete()
    emojis = ["😀", "😂", "😍", "😎", "😢", "😡"]
    await ctx.send(random.choice(emojis))
