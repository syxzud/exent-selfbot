import holder
import globals

exent = holder.bot

@exent.command()
async def ping(ctx):
    await ctx.message.delete()

    afk = globals.afk

    if afk == False:
        afk = True
    else:
        afk = False

    await ctx.send(f"afk set to {afk}")