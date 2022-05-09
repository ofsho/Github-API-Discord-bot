import discord
from ghapi.all import GhApi

from defaults import colors

from api.gr import gr
from api.commit import commit

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

        await message.channel.send(embed=embed)

    if message.content.startswith('!gh gr'):
        await message.channel.send(embed=gr(message))

    if message.content.startswith('!gh commit'):
        await message.channel.send(embed=commit(message))