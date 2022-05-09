import discord
from ghapi.all import GhApi

from defaults import colors

api = GhApi()

# last commit
def repo(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]

    try:
        repo = api.repos.get(owner=repo_owner, repo=repo_name)

        # commit embed
        embed = discord.Embed(title=repo_name.title() + ' Info', color=colors['yellow'])

        embed.set_image(url=repo['owner']['avatar_url'])

        embed.add_field(name='Name', value=repo['name'])
        embed.add_field(name='Owner', value=repo['owner']['login'])
        embed.add_field(name='Description', value=repo['description'])
        embed.add_field(name='Is Fork', value=repo['fork'])
        embed.add_field(name='Forks', value=repo['forks_count'])
        embed.add_field(name='Is Template', value=repo['is_template'])
        embed.add_field(name='Stars', value=repo['stargazers_count'])
        embed.add_field(name='Open Issues', value=repo['open_issues'])
        embed.add_field(name='Topics', value=', '.join(repo['topics']))
        embed.add_field(name='URL', value="[Website URL]("+repo['html_url']+")")
        embed.add_field(name='Ref URL', value="[Ref API URL]("+repo['url']+")")

        return embed
    except:
        embed = discord.Embed(title='', color=colors['red'])
        embed.add_field(name='Error', value='Repo ' + repo_owner + '/' + repo_name + ' not found')

        return embed