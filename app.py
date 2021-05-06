import os
import asyncio
from dotenv import load_dotenv

import discord
import asyncpg

# Load the dotenv file if it exists
try: load_dotenv()
except: pass

# Get environment variables
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

# Create the client
client = discord.Client()

# Connect to the DB
# ...



# Database functions



# Discord handler functions

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# Run the discord client
if __name__ == '__main__':
    client.run(DISCORD_TOKEN)
