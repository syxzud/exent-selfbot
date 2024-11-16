import holder
import globals

exent = holder.bot

prefix = globals.prefix

@exent.command()
async def help(ctx):
    await ctx.message.delete()

    help = f"""
```ini
[syxz bot] [help]```
```md
ExentBot v1.0.0 Help
Amount of Commands: idk, <> is required, [] is optional
**Categories**
Fun            - Fun commands
Trolling       - Trolling commands
Memegen        - Generate memes using imgflip
Misc           - Misc commands
Raiding        - Raiding commands
Config         - Change the bot's config```
```ansi
Use {prefix}help <category name> or {prefix}help <command name> to get more info.
Use {prefix}search <query> to search commands.
Use {prefix}repeat to repeat the last command.
``````css
[syxzbot v1.0.0]```
"""


    await ctx.send(help)


@exent.command()
async def fun(ctx):
    await ctx.message.delete()

    fun = f"""
```ini
[syxz bot] [fun]
``````md
<> is required, [] is optional

Amount of Fun commands: 8
``````md
# Commands
{prefix}eightball <question> - Asks the 8-Ball a question
{prefix}howgay <user> - See how gay a person is
{prefix}howsimp <user> - See how simp a person is
{prefix}penis <user> - See how big a person's penis is
{prefix}iqtest <user> - Test a person's IQ
{prefix}hack <user> - Fake hack a person
{prefix}dadjoke - Send a random dad joke
{prefix}choose <option1> <option2> ... - Choose a random item from the list of items


``````css
[syxzbot v1.0.0]```
"""

    await ctx.send(fun)

@exent.command()
async def trolling(ctx):
    await ctx.message.delete()

    trolling = f"""
```ini
[syxz bot] [trolling]
``````md
<> is required, [] is optional

Amount of Fun commands: 2
``````md
# Commands
{prefix}hiddeneveryone <text> - Hides an @everyone behind text
{prefix}token <user> - Shows the first part of a users discord token
``````css
[syxzbot v1.0.0]```
"""

    await ctx.send(trolling)

@exent.command()
async def raiding(ctx):
    await ctx.message.delete()

    raiding = f"""
```ini
[syxz bot] [raiding]
``````md
<> is required, [] is optional

Amount of Fun commands: 1
``````md
# Commands
{prefix}spam <amount> <message> - spams an message
``````css
[syxzbot v1.0.0]```
"""

    await ctx.send(raiding)

@exent.command()
async def misc(ctx):
    await ctx.message.delete()

    misc = f"""
```ini
[syxz bot] [misc]
``````md
<> is required, [] is optional

Amount of Fun commands: 1
``````md
# Commands
{prefix}purge <amount> - deletes messages
{prefix}ping - shows bot latency
{prefix}hypesquad <house> - set your hypesquad
``````css
[syxzbot v1.0.0]```
"""

    await ctx.send(misc)

