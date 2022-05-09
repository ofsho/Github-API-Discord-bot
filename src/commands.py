import discord
from ghapi.all import GhApi

from defaults import colors

from api.gr import gr
from api.commit import commit
from api.repo import repo
from api.lcont import lcont
from api.ldep import ldep
from api.getforks import getforks
from api.getlangs import getlangs
from api.releases import releases, releaseBody, releaseInfo

client = discord.Client()
api = GhApi()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!gh help'):
        embed = discord.Embed(title='Github API Command List', description="!gh __command__ ...args", color=colors['green'])
        embed.add_field(name='gr __owner__ __name__ (optional: __branch__)', value='Get Repo Url', inline=False)
        embed.add_field(name='commit __owner__ __name__ (optional: __sha__ __branch__)', value='Last Commit in repo', inline=False)
        embed.add_field(name='repo __owner__ __name__', value="Sends Repo Information", inline=False)
        embed.add_field(name='lcont __owner__ __name__', value="List of contributors for a repo", inline=False)
        embed.add_field(name='ldep __owner__ __name__', value="List of deployments of a repo", inline=False)
        embed.add_field(name='getforks __owner__ __name__', value="List of forks of a repo", inline=False)
        embed.add_field(name='releases __owner__ __name__', value="Get all releases from repo", inline=False)
        embed.add_field(name='reldesc __owner__ __name__ (optional: __tag-name__)', value="Get body from release", inline=False)
        embed.add_field(name='relinfo __owner__ __name__ (optional: __tag-name__)', value="Get ifno of release", inline=False)

        await message.channel.send(embed=embed)

    if message.content.startswith('!gh gr'):
        await message.channel.send(embed=gr(message))

    elif message.content.startswith('!gh commit'):
        await message.channel.send(embed=commit(message))

    elif message.content.startswith('!gh repo'):
        await message.channel.send(embed=repo(message))

    elif message.content.startswith('!gh lcont'):
        await message.channel.send(embed=lcont(message))

    elif message.content.startswith('!gh ldep'):
        await message.channel.send(embed=ldep(message))

    elif message.content.startswith('!gh getforks'):
        await message.channel.send(embed=getforks(message))

    elif message.content.startswith('!gh getlangs'):
        await message.channel.send(embed=getlangs(message))

    elif message.content.startswith('!gh releases'):
        await message.channel.send(embed=releases(message))

    elif message.content.startswith('!gh reldesc'):
        await message.channel.send(embed=releaseBody(message))

    elif message.content.startswith('!gh relinfo'):
        await message.channel.send(embed=releaseInfo(message))