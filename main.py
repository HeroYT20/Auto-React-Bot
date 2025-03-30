from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file
TOKEN = os.getenv('DISCORD_TOKEN')  # Gets the token from Railway variables

from flask import Flask
from threading import Thread
import discord
from discord.ext import commands

# ==== CONFIGURATION ====
CHANNEL_IDS = [1326800912098005012, 1326801008239575080]
REACTIONS = ["<:Downvote:1341850508540907581>", "<:Upvote:1341850570214080582>"]

# ==== KEEP ALIVE ====
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ==== BOT SETUP ====
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id in CHANNEL_IDS:
        if message.attachments:
            for attachment in message.attachments:
                # Add code here to process the attachment
                print(f"Attachment found: {attachment.url}")
                # You can download or do something else with the attachment here
    await bot.process_commands(message)  # Make sure other commands are processed
