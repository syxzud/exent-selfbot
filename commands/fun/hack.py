import holder
import requests

exent = holder.bot

@exent.command()
async def hack(ctx, userr: str):
    await ctx.message.delete()

    response = requests.get("https://randomuser.me/api/?results=1")

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response

        # Extract the relevant information
        user = data['results'][0]
        name = f"{user['name']['first']} {user['name']['last']}"
        gender = user['gender']
        address = f"{user['location']['street']['number']} {user['location']['street']['name']}, {user['location']['city']}, {user['location']['state']} {user['location']['postcode']}"
        county = user['location']['country']

    else:
        print("Failed to retrieve data from the API.")

    message = f"""
```ini
[syxz bot]
``````md
# User
{userr}

# Real Name
{name}

# Address
{address}

# Gender
{gender}

# County
{county}

``````css
[syxzbot v1.0.0]```
"""

    #await ctx.send(f"Name: {name}\nGender: {gender}\nAddress: {address}\nCounty: {county}\n##")
    await ctx.send(message)
