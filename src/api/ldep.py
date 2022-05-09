import discord
from ghapi.all import GhApi

from defaults import colors

api = GhApi()

# last commit
def ldep(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]

    try:
        deploy_list = api.repos.list_deployments(owner=repo_owner, repo=repo_name, per_page=15, page=1)

        # commit embed
        embed = discord.Embed(title=repo_name.title() + ' Deployment List', color=colors['white'])

        for deployment in deploy_list:
            embed.add_field(name='Deployment API URL', value="[API URL]("+deployment['url']+")")
            embed.add_field(name='Deployment Description', value=deployment['description'])
            embed.add_field(name='Deployment Sha', value=deployment['sha'])

        return embed
    except:
        embed = discord.Embed(title='', color=colors['red'])
        embed.add_field(name='Error', value='Repo Deployments not found')

        return embed