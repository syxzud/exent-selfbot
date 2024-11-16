import holder
import globals

exent = holder.bot

@exent.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('Pong! Delay: {0}'.format(round(exent.latency, 1)))