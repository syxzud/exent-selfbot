import asyncio
import datetime
import sys
from pathlib import Path

import holder
import globals
import dateutil.parser as du_parser
from docopt import docopt


exent = holder.bot


@exent.command()
async def purge(ctx, target: str, limit: int = 100, after: str = None, before: str = None):
    try:
        # Parse target argument into name and number
        try:
            name, number = target.split("#")
        except ValueError:
            await ctx.send("Error: target must be supplied as 'name#number'")
            return
        
        # Parse the optional after and before arguments
        after_dt = _dt_parse(after) if after else datetime.datetime(2015, 5, 13)
        before_dt = _dt_parse(before) if before else datetime.datetime.utcnow().replace(microsecond=0)

        # Get DM channels
        dm_channels = (c for c in exent.private_channels if isinstance(c, holder.discord.DMChannel))
        
        # Identify DM channel by recipient
        dm_channel = list(c for c in dm_channels
                          if c.recipient.name == name and c.recipient.discriminator == number)
        
        if not dm_channel:
            await ctx.send(f"Error: No recipient '{name}#{number}' found in DMs")
            return
        
        dm_channel = dm_channel[0]

        counter = 0
        await ctx.send(f"Purging messages sent between '{after_dt} UTC' and '{before_dt} UTC'...")
        
        async for msg in dm_channel.history(limit=limit, after=after_dt, before=before_dt):
            if msg.author == exent.user and msg.type == holder.discord.MessageType.default:
                counter += 1
                await msg.delete()

        await ctx.send(f"Purged {counter} messages.", delete_after=5)

    except Exception as e:
        await ctx.send(f"Error: {str(e)}")


def _dt_parse(dts):
    try:
        return du_parser.parse(dts, ignoretz=True)
    except du_parser._parser.ParserError:
        print(f"Error: could not parse datetime '{dts}'")
        sys.exit(1)
