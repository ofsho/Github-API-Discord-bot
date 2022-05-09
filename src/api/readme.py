from calendar import c
import discord
from ghapi.all import GhApi
import urllib.request

from defaults import colors

api = GhApi()

# last commit
def readme(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]

    try:
        # commit embed
        embed = discord.Embed(title='README.MD', color=colors['yellow'])

        content_url = "https://raw.githubusercontent.com/"+repo_owner+"/"+repo_name+"/master/README.md"
        fp = urllib.request.urlopen(content_url)
        ByBytes = fp.read()
        content = ByBytes.decode("utf8")
        fp.close()

        embed.add_field(name='README CONTENT', value=content[0:1024], inline=False)
        embed.add_field(name='...', value=content[1024:2048], inline=False)
        embed.add_field(name='...', value=content[2048:3072], inline=False)
        embed.add_field(name='...', value=content[3072:4096], inline=False)
        embed.add_field(name='...', value=content[4096:5120], inline=False)

        return embed
    except:
        embed = discord.Embed(title='README.MD', color=colors['red'])
        embed.add_field(name='Error', value='No README.MD found')
        return embed