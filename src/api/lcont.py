import discord
from ghapi.all import GhApi

from defaults import colors

api = GhApi()

# last commit
def lcont(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]

    try:
        contributor_list = api.repos.list_contributors(owner=repo_owner, repo=repo_name, per_page=15, page=1)

        # commit embed
        embed = discord.Embed(title=repo_name.title() + ' Contributor List', color=colors['yellow'])

        for contributor in contributor_list:
            embed.add_field(name=contributor['login'], value="[Website URL]("+contributor['html_url']+")")

        return embed
    except:
        embed = discord.Embed(title='', color=colors['red'])
        embed.add_field(name='Error', value='Repo Contributors not found')

        return embed