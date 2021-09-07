from discord.ext import commands
from colorama import init

init()
class Ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.remove_command('help')
        print(f'\n\033[32m{self.client.user.name} is ready\033[0m')

def setup(client):
    client.add_cog(Ready(client))
