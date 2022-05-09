import discord
from ghapi.all import GhApi

from defaults import colors, webify

api = GhApi()

# last commit
def releases(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]

    releases = api.repos.list_releases(owner=repo_owner, repo=repo_name, per_page=5)

    try:
        # check if any releases
        if len(releases) == 0:
            embed = discord.Embed(title=repo_name.title() + ' Releases', color=colors['red'])
            embed.add_field(name='Error', value='No releases found')
        else:
            # release embed
            embed = discord.Embed(title=repo_name + ' Releases', color=colors['green'])
            
            for release in releases:
                embed.add_field(name=str(release['tag_name']), value='[Download]('+str(release['zipball_url'])+
                    ') • [URL]('+str(release['html_url'])+')', inline=False)

            embed.add_field(name="other", value="[View all releases](https://github.com/"+repo_owner+"/"+repo_name+"/releases)")

        return embed
    except:
        embed = discord.Embed(title=repo_name.title() + ' Releases', color=colors['red'])
        embed.add_field(name='Error', value='No releases found')
        return embed

def releaseBody(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]
    # check if added tag name
    tag_name = ""
    try:
        tag_name = message.content.split(' ')[4]
    except:
        pass

    try:
        releases = api.repos.list_releases(owner=repo_owner, repo=repo_name, per_page=5)

        # check if any releases
        if len(releases) == 0:
            embed = discord.Embed(title=repo_name.title() + ' Release Description', color=colors['red'])
            embed.add_field(name='Error', value='No releases found')
        else:
            # release embed
            embed = discord.Embed(title=repo_name.title() + ' Release Description', color=colors['green'])

            for release in releases:
                if tag_name == release['tag_name'] and tag_name != "":
                    embed.add_field(name=str(release['tag_name']), value=str(release['body'][0:100]), inline=False)
                    embed.add_field(name="More", value="[Click Here]("+release['html_url']+")", inline=False)
                elif tag_name == "":
                    embed.add_field(name=str(release['tag_name']), value=str(release['body'][0:100]), inline=False)
                    embed.add_field(name="More", value="[Click Here]("+release['html_url']+")", inline=False)
        
        return embed
    except:
        embed = discord.Embed(title=repo_name.title() + ' Releases', color=colors['red'])
        embed.add_field(name='Error', value='Release not found')
        return embed

def releaseInfo(message):
    repo_owner = message.content.split(' ')[2]
    repo_name = message.content.split(' ')[3]
    # check if added tag name
    tag_name = ""
    try:
        tag_name = message.content.split(' ')[4]
    except:
        pass

    releases = api.repos.list_releases(owner=repo_owner, repo=repo_name, per_page=1)

    # check if any releases
    if len(releases) == 0:
        embed = discord.Embed(title=repo_name.title() + ' ' + tag_name + ' Info', color=colors['red'])
        embed.add_field(name='Error', value='No releases found')
    else:
        # release embed
        embed = discord.Embed(title=repo_name.title() + ' ' + tag_name + ' Info', color=colors['green'])

        for release in releases:
            if tag_name == release['tag_name'] and tag_name != "":
                release_info_block(release, embed)
            elif tag_name == "":
                release_info_block(release, embed)
    
    return embed

def release_info_block(release, embed):
    embed.add_field(name="Release Date", value=str(release['published_at']))
    embed.add_field(name="Release Tag", value=str(release['tag_name']))
    embed.add_field(name="Release Description", value=str(release['body']), inline=False)
    embed.add_field(name="Release URL", value='[URL]('+str(release['html_url'])+')')
    embed.add_field(name="Release Assets", value=str('[URL]('+release['assets_url'])+')')
    embed.add_field(name="Release Author", value=str(release['author']['login']), inline=False)
    embed.add_field(name="Release Zip", value=str('[URL]('+release['zipball_url']+')'))
    embed.add_field(name="Release Tarball", value=str('[URL]('+release['tarball_url']+')'))

    # assets
    for asset in release['assets']:
        embed.add_field(
            name="\u200b——————————————————————————————————————",
            value="Asset" + asset['label'],
            inline=False
        )
        embed.add_field(name="Asset Name", value=str(asset['name']))
        embed.add_field(name="Asset Size", value=str(asset['size']))
        embed.add_field(name="Asset Type", value=str(asset['content_type']))
        embed.add_field(name="Asset Download", value=str('[URL]('+asset['browser_download_url']+')'), inline=False)

    return embed