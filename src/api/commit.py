import discord
from ghapi.all import GhApi

from defaults import colors

api = GhApi()

# last commit
def commit(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]
    # find if the user set a specific branch
    branch = ''
    try:
        branch = message.content.split(' ')[5]
    except:
        branch = 'master'

    repo = api.git.get_ref(owner=repo_owner, repo=repo_name, ref='heads/' + branch)
    
    # find if user set a specific sha
    sha = ""
    try:
        sha = message.content.split(' ')[4]
    except:
        sha = repo['object']['sha']

    commit = api.git.get_commit(owner=repo_owner, repo=repo_name, commit_sha=sha)

    # commit embed
    embed = discord.Embed(title=repo_name.title() + ' Repo URL', color=colors['pink'])
    embed.add_field(name='Sha', value=repo['object']['sha'])
    embed.add_field(name='URL', value=commit['html_url'])
    embed.add_field(name='URL Ref', value=repo['object']['url'])
    embed.add_field(name="Committer", value=commit['committer']['name'])
    embed.add_field(name="Message", value=commit['message'])

    return embed