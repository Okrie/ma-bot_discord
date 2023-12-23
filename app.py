"""
    Discord Maple Story bot
    app.py
    Author : Okrie
"""

from dotenv import load_dotenv
from datetime import datetime
from model.discord_model import DiscordClient
import discord
import os

load_dotenv()
TOKEN = os.environ.get('TOKEN')

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    app = DiscordClient(intents=intents)
    app.run(TOKEN)
