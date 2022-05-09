import discord
from ghapi.all import GhApi

from defaults import colors

api = GhApi()

# last commit
def getforks(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]

    try:
        list = api.repos.list_forks(owner=repo_owner, repo=repo_name, per_page=24, page=1)

        # commit embed
        embed = discord.Embed(title=repo_name.title() + ' Fork List', color=colors['d_blue'])

        for item in list:
            embed.add_field(name=item['owner']['login'], value="["+item['name']+"]("+item['html_url']+")")

        return embed
    except:
        embed = discord.Embed(title='', color=colors['red'])
        embed.add_field(name='Error', value='No forks not found')

        return embed