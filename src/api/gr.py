import discord
from ghapi.all import GhApi

from defaults import colors

api = GhApi()

def gr(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]

    try:
        repo = api.git.get_ref(owner=repo_owner, repo=repo_name, ref='heads/master')

        embed = discord.Embed(title=repo_name.title() + ' Repo URL', color=colors['blue'])
        embed.add_field(name='URL', value='https://github.com/' + repo_owner + '/' + repo_name, inline=False)
        embed.add_field(name='Ref URL', value=repo['url'])

        return embed
    except:
        embed = discord.Embed(title='', color=colors['red'])
        embed.add_field(name='Error', value='Repo ' + repo_owner + '/' + repo_name + ' not found', inline=False)

        return embed