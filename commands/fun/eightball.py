import holder
import random

exent = holder.bot

@exent.command()
async def eightball(ctx, *question: str):
    await ctx.message.delete()
    responses = [
        "It is certain",
        "It is decidedly so",
        "Yes – definitely",
        "You may rely on it",
        "Yes",
        "Signs point to yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"

    ]

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


