import holder
import random

exent = holder.bot

@exent.command()
async def iqtest(ctx):
    """Generate a random IQ score."""
    await ctx.message.delete()
    iq = random.randint(60, 200)
    await ctx.send(f"Your IQ is: {iq}")
