import discord
from discord.ext import commands
from colorama import init

init()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', case_insensitive=True, intents=intents)

def ensure_commands(extension):
    try:
        client.load_extension(f'commands.{extension}')
    except Exception as e:
        print(f'\033[93mFail to load command {extension}:\033[0m \033[91m{e}\033[0m')

def ensure_events(extension):
    try:
        client.load_extension(f'events.{extension}')
    except Exception as e:
        print(f'\033[93mFail to load event {extension}:\033[0m \033[91m{e}\033[0m')

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 330102349425016842
    return commands.check(predicate)