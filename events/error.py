from discord.ext import commands
from functions import red

class Error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
       if isinstance(error, commands.CommandNotFound):
           print(red(f'{error}'))

def setup(client):
    client.add_cog(Error(client))