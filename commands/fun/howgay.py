import holder
import random

exent = holder.bot

@exent.command()
async def howgay(ctx, user: str):
    """Determine how gay a user is."""
    await ctx.message.delete()
    gayProcent = random.randint(1, 100)
    await ctx.send(f"{user} is {gayProcent}% gay!")
