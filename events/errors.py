import sys

from discord.ext import commands
from main import load, unload, reload
from colorama import init

init()
def line():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    return exc_tb.tb_lineno

class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    # CheckFailure from Main
    @load.error
    @unload.error
    @reload.error
    async def check_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.delete()

def setup(client):
    client.add_cog(Errors(client))