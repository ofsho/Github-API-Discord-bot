import discord
from ghapi.all import GhApi

from defaults import colors, webify

api = GhApi()

# last commit
def getlangs(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]

    try:
        items = api.repos.list_languages(owner=repo_owner, repo=repo_name)
        langs = []
        total = 0

        # commit embed
        embed = discord.Embed(title=repo_name.title() + ' Languages', color=colors['pink'])

        for item in items:
            langs.append(item + '/' + str(items[item]))
            total += items[item]
        
        # check percentage
        for lang in langs:
            lang_percentage = (int(lang.split('/')[1]) / total) * 100
            embed.add_field(name=lang.split('/')[0], value='['+str("%.2f" % lang_percentage)
                +'](https://github.com/'+repo_owner+'/'+repo_name+'/search?l='+webify(lang.split('/')[0])+')' + '%')

        return embed
    except:
        embed = discord.Embed(title='', color=colors['red'])
        embed.add_field(name='Error', value='No languages not found')

        return embed