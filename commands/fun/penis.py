import holder
import random

exent = holder.bot

@exent.command()
async def penis(ctx, User: str):
    await ctx.message.delete()
    dickSize = random.randint(1, 7)
    dick = "="*dickSize
    await ctx.send(f"{User}'s dick is 8{dick}D")
