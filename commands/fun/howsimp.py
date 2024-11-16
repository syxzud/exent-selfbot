import holder
import random

exent = holder.bot

@exent.command()
async def howsimp(ctx, user: str):
    await ctx.message.delete()
    simpProcent = random.randint(1, 100)
    await ctx.send(f"{user} is {simpProcent}% simp!")
