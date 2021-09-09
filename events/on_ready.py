from discord.ext import commands
from functions import green

class Ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.remove_command('help')
        print(green(f'{self.client.user.name} is ready'))

def setup(client):
    client.add_cog(Ready(client))
