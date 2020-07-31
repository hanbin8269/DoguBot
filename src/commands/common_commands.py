import discord
from module.extract_team import ExtractTeam
from utils.create_embed import get_embed

class CommonCommands:
    @staticmethod
    async def help(message):
        embed = get_embed('도움말',{"팀짜기" : ['도구야 팀짜줘 그냥','도구야 팀짜줘 티어로']})
        await message.channel.send(embed=embed)