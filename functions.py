import discord
from discord.ext import commands
from colorama import init

init()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', case_insensitive=True, intents=intents)

def red(arg): return f'\033[91m{arg}\033[0m'
def yellow(arg): return f'\033[93m{arg}\033[0m'
def green(arg): return f'\033[32m{arg}\033[0m'

def ensure_commands(extension):
    try:
        client.load_extension(f'commands.{extension}')
    except Exception as e:
        print(yellow(f'Fail to load command {extension}:'), red(e))

def ensure_events(extension):
    try:
        client.load_extension(f'events.{extension}')
    except Exception as e:
        print(yellow(f'Fail to load command {extension}:'), red(e))

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 330102349425016842
    return commands.check(predicate)

