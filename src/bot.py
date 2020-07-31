import discord
from discord.ext import commands
from module.extract_team import ExtractTeam
from commands.organize_team_commands import OrganizeTeamCommands
from commands.common_commands import CommonCommands
class DoguBot(commands.Bot):
    def __init__(self,**kwargs):
        super().__init__(command_prefix="", help_command=None, **kwargs)
    async def on_ready(self):
        print('봇 시작')
    async def on_message(self,message:discord.Message):
        content = message.content.split()
        print(content)
        if not message.author.bot:
            if content[1] == "팀짜줘":
                print('enter the first if')
                if content[2] == "티어로":
                    await OrganizeTeamCommands.organize_team_with_tier(message)
                if content[2] == "그냥":
                    await OrganizeTeamCommands.organize_team_common(message)
            if content[1] == "도움말":
                await CommonCommands.help(message)