import asyncio, discord
from discord.ext import commands

import os 
import json

token_path = os.path.dirname( os.path.abspath(__file__)) + "/config.json"
t = open(token_path,"r", encoding="utf-8")
token = json.loads(t.read())['token']

game = discord.Game("명령어 : 도구야")

bot = commands.Bot(command_prefix='도구야 ', status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
    print('봇 시작')

@bot.command()
async def 팀짜줘(ctx):
    await ctx.send("팀짜기 시작합니다")

bot.run(token)

