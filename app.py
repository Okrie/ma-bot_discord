"""
    Discord Maple Story bot
    app.py
    Author : Okrie
"""

from dotenv import load_dotenv
from model.discord_model import DiscordClient
from config.log_w import LogClass
from module.date.date import get_now_times
import discord
import os

load_dotenv()
TOKEN = os.environ.get('TOKEN')

if __name__ == '__main__':
    logger = LogClass()
    logger.set_value(str(get_now_times(len=19)).replace(":", "-"))
    intents = discord.Intents.default()
    intents.message_content = True
    app = DiscordClient(intents=intents)
    app.run(TOKEN)
