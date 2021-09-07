from discord.ext import commands
from database.db_lb import *

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='check')
    async def check_ban(self, ctx):
        await ctx.message.delete()
        get_banned()

def setup(client):
    client.add_cog(Test(client))

