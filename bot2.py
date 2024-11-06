import discord
from discord.ext import commands
import random

# Replace with your actual tokens
DISCORD_TOKEN = ''

# Set up intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable the message content intent

# Set up the bot with the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # List of responses
    responses = [
        "Made by changcheng967 (xqqzldh), Have a Nice Day!",
        "Made by changcheng967 (xqqzldh), Shut up!",
        "Made by changcheng967 (xqqzldh), What the f*** B****, shut up!"
        "Made by changcheng967 (xqqzldh), Fuck you! "
        "Made by changcheng967 (xqqzldh), Fuck Off N*gger!"
    ]

    # Pick a random response
    response = random.choice(responses)

    # Append the username of the message author
    response += f" {message.author.name}"

    # Respond to any message
    await message.channel.send(response)

# Run the bot
bot.run(DISCORD_TOKEN)
