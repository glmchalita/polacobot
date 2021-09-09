import sys
from discord.ext import commands
from functions import red

def line():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    return exc_tb.tb_lineno

class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
       if isinstance(error, commands.CommandNotFound):
           print(red(f'{error}'))

def setup(client):
    client.add_cog(Error(client))