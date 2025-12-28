import discord
import random
import os

# get token from environment variable
token = os.getenv('BOT_TOKEN')
if token is None:
    print("Token not found, define BOT_TOKEN environment variable with your bot token!")
    exit(1)

# create discord client intents
intents = discord.Intents.default()
intents.message_content = True

# create discord client
client = discord.Client(intents=intents)

# define choices of the loadout
words = ["Use a Shotgun", "Use a Assault Rifle", "Use a Sniper"]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('!ping'):
        await message.channel.send('Pong!')

    elif message.content.startswith("!loadout"):
        await message.channel.send (random.choice(words))

# run the client
client.run(token)
