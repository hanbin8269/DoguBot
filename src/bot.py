import discord
from discord.ext import commands
from module.oranizeTeam import OranizeTeam

class DoguBot(commands.Bot):
    def __init__(self,**kwargs):
        super().__init__(command_prefix="", help_command=None, **kwargs)
    async def on_ready(self):
        print('봇 시작')
    async def on_message(self,message:discord.Message):
        content = message.content.split()
        author = message.author
        print(content)
        if content[1] == "팀짜줘":
            if content[2] == "티어로":
                channel_id = author.voice.channel.id # 메세지를 보낸 사람이 존재하는 음성채널의 id
                channel_members = message.guild.get_channel(channel_id).members # 메세지를 보낸 사람이 존재하는 음성채널의 모든 유저 
                members = []
                for i in channel_members: 
                    members.append(i.name)
                
                result = OranizeTeam.tier_organize_reform(members = members)
                embed=discord.Embed(title="팀 편성", color=0x00ff56)

                names = {
                    "1팀" : [],
                    "2팀" : []
                }
                for i,j in zip(result['1팀'],result['2팀']):
                    names['1팀'].append(i[0])
                    names['2팀'].append(j[0])
            
                embed.add_field(name="1팀", value=names['1팀'], inline=False)
                embed.add_field(name="2팀", value=names['2팀'], inline=False)
                print('names : {0}'.format(names))

                await message.channel.send(embed=embed)
            if content[2] == "그냥":
                channel_id = author.voice.channel.id # 메세지를 보낸 사람이 존재하는 음성채널의 id
                channel_members = message.guild.get_channel(channel_id).members # 메세지를 보낸 사람이 존재하는 음성채널의 모든 유저 
                member_list = []
                for i in channel_members: 
                    member_list.append(i.name)

                result = OranizeTeam.common_orgainze(members = member_list)
                embed=discord.Embed(title="팀 편성", color=0x00ff56)
                embed.add_field(name="1팀", value=result['1팀'], inline=False)
                embed.add_field(name="2팀", value=result['2팀'], inline=False)
                await message.channel.send(embed=embed)
        