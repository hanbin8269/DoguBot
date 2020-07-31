import discord

def get_embed(title,result):
    embed=discord.Embed(title=title, color=0x00ff56)
    print(result)
    for field_name in result:
        embed.add_field(name=field_name, value=result[field_name])
    
    return embed