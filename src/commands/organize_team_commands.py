import discord
from module.extract_team import ExtractTeam
from utils.create_embed import get_embed
class OrganizeTeamCommands:
    @staticmethod
    async def organize_team_common(message):
        content = message.content.split()
        author = message.author

        channel_id = author.voice.channel.id # 메세지를 보낸 사람이 존재하는 음성채널의 id
        channel_members = message.guild.get_channel(channel_id).members # 메세지를 보낸 사람이 존재하는 음성채널의 모든 유저 

        member_list = []
        for i in channel_members: 
            member_list.append(i.name)

        result = ExtractTeam.get_team_common(members = member_list)
        embed = get_embed('무작위 팀 편성',result)
        
        await message.channel.send(embed=embed)
    @staticmethod
    async def organize_team_with_tier(message):
        content = message.content.split()
        author = message.author
        try:
            channel_id = author.voice.channel.id # 메세지를 보낸 사람이 존재하는 음성채널의 id
        except AttributeError as e:
            result = {
                "message" : ['음성채널에 들어간 후 사용해주세요']
            }
            embed = get_embed("Error",result)

            await message.channel.send(embed=embed)
            return
        
        channel_members = message.guild.get_channel(channel_id).members # 메세지를 보낸 사람이 존재하는 음성채널의 모든 유저 

        if len(channel_members) % 2 == 1:
            result = {
                'message' : ['짝수의 인원으로 다시 시도해주세요']
            }
            embed = get_embed("Error",result)
            await message.channel.send(embed=embed)

            return

        channel_members_name = [channel_member.name for channel_member in channel_members]
            
        result = ExtractTeam.get_team_with_tier(members = channel_members_name)

        names = {
            "1팀" : [name for name in result['1팀']],
            "2팀" : [name for name in result['2팀']]
        }
        
        embed = get_embed("티어 밸런스 팀 편성",names)

        await message.channel.send(embed=embed)