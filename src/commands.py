import discord
from ghapi.all import GhApi

from defaults import colors
from api.gr import gr

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
        embed = discord.Embed(title='Github API Command List', color=colors['green'])
        embed.add_field(name='!gh gr __owner__ __name__', value='Get Repo Url', inline=False)
        embed.add_field(name='!gh gc', value='Get Commit Url', inline=False)

        await message.channel.send(embed=embed)

    if message.content.startswith('!gh gr'):
        await message.channel.send(embed=gr(message))