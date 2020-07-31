import asyncio, discord
from discord.ext import commands

import os 
import json
from bot import DoguBot

token_path = os.path.dirname( os.path.abspath(__file__)) + "/config.json"
t = open(token_path,"r", encoding="utf-8")
token = json.loads(t.read())['token']

bot = DoguBot()

bot.run(token)