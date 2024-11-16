import holder
import requests
import asyncio
import base64

exent = holder.bot

@exent.command()
async def token(ctx, user: str):
    await ctx.message.delete()
    
    # Get the user ID from the mentioned user
    user_id = ctx.message.mentions[0].id if ctx.message.mentions else None
    
    if user_id:
        # Encrypt the user ID with Base64
        encoded_user_id = base64.b64encode(str(user_id).encode()).decode()
        
        # Send the encoded user ID back to the channel
        await ctx.send(f"Start of Token: {encoded_user_id}")
    else:
        await ctx.send("User not found.")
    
    