import discord
from discord.ext import commands
from asyncio import sleep
from functions import client

class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def random_status(self):
        while True:
            await client.wait_until_ready()
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Long Beach RP'))
            await sleep(8)
            await client.change_presence(status=discord.Status.online, activity=discord.Game(name='discord.gg/longbeachrp'))
            await sleep(8)
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='DEV Chali#3955'))
            await sleep(8)
    client.loop.create_task(random_status(client))

def setup(client):
    client.add_cog(Status(client))
