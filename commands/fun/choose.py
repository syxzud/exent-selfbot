import holder
import random

exent = holder.bot

@exent.command()
async def choose(ctx, *options: str):
    """Choose a random option from the provided list."""
    await ctx.message.delete()
    await ctx.send(f"I choose: {random.choice(options)}!")
