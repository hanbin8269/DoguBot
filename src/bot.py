import discord
from discord.ext import commands

class DoguBot(commands.Bot):
    async def on_ready(self):
        activity = discord.Game(game='도구야 도움말')
    async def on_message(self,message: discord.Message):
        await self.wait_until_ready()
        