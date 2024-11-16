import holder
import requests
import asyncio

exent = holder.bot

@exent.command()
async def spam(ctx, amount: int, *message):
    await ctx.message.delete()
    
    # Join the message parts into a single string
    message = " ".join(message)
    
    for i in range(amount):
        await ctx.send(message)