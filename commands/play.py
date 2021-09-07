import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionEventType

class Play(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def connect(self, ctx):
        await ctx.message.delete()

        fivem = Button(style=ButtonStyle.URL, label="FiveM", url="http://131.196.198.119:3554/Connect/Fivem.php")
        ts = Button(style=ButtonStyle.URL, label="TeamSpeak", url="http://131.196.198.119:3554/Connect/Teamspeak.php")

        play = discord.Embed(color=discord.Color.from_rgb(47, 49, 54), title='LONG BEACH 🏖')
        play.add_field(name='Servidor:', value='```connect 131.196.198.119```', inline=False)
        play.add_field(name='TeamSpeak:', value='```135.148.97.184:16450```', inline=False)
        play.set_image(url='https://i.imgur.com/Prkr3ju.png')
        await ctx.send(embed=play, components=[[fivem, ts]])

    @commands.command()
    async def social(self, ctx):
        await ctx.message.delete()

        ig = Button(style=ButtonStyle.URL, label="Instagram", url="https://www.instagram.com/longbeachrp/")
        tik = Button(style=ButtonStyle.URL, label="Tik Tok", url="https://www.tiktok.com/@longbeachrplay?")
        yt = Button(style=ButtonStyle.URL, label="Youtube", url="https://www.youtube.com/channel/UCYAepx35_ukBYE8rYCBdQOA")

        play = discord.Embed(color=discord.Color.from_rgb(47, 49, 54), title='MIDIAS SOCIAIS')
        play.set_image(url='https://i.imgur.com/peyFqF8.gif')
        await ctx.send(embed=play, components=[[ig, tik, yt]])

def setup(client):
    client.add_cog(Play(client))
