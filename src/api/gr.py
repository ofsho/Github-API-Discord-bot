import discord
from ghapi.all import GhApi

from defaults import colors

api = GhApi()

def gr(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]
    branch = ''
    try:
        branch = message.content.split(' ')[4]
    except:
        branch = 'master'

    try:
        repo = api.git.get_ref(owner=repo_owner, repo=repo_name, ref='heads/' + branch)

        embed = discord.Embed(title=repo_name.title() + ' Repo URL', color=colors['blue'])
        embed.add_field(name='URL', value="[Website URL]('https://github.com/'" + repo_owner + '/' + repo_name + ")")
        embed.add_field(name='Ref URL', value="[Ref API URL]("+repo['url']+")")

        return embed
    except:
        embed = discord.Embed(title='', color=colors['red'])
        embed.add_field(name='Error', value='Repo ' + repo_owner + '/' + repo_name + ' not found')

        return embed