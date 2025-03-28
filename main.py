from flask import Flask
from threading import Thread
import discord
from discord.ext import commands

# ==== CONFIGURATION ====
TOKEN = ""
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
            for emoji in REACTIONS:
                await message.add_reaction(emoji)
    await bot.process_commands(message)

keep_alive()
bot.run(TOKEN)
