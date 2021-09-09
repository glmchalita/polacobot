import discord
from discord.ext import commands
from asyncio import sleep

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.loop.create_task(self.random_status(client))

    @commands.Cog.listener()
    async def random_status(self, client):
        while True:
            await client.wait_until_ready()
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Long Beach RP'))
            await sleep(8)
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name='discord.gg/longbeachrp'))
            await sleep(8)
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='DEV Chali#3955'))
            await sleep(8)

def setup(client):
    client.add_cog(Status(client))
