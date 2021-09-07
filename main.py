from functions import *

ensure = [
    #'commands.whitelist',
    'commands.staff',
    #'commands.police',
    'events.status',
    #'events.on_message',
    #'events.on_reaction',
    #'events.on_member_join',
    #'events.on_member_remove',
    #'events.on_member_update',
    'events.on_ready'
]

if __name__ == '__main__':
    for ext in ensure:
        client.load_extension(ext)
        print(f'\033[32mLoaded {ext}\033[0m')

@client.command()
@is_owner()
async def load(ctx, dirt, extension):
    try:
        client.load_extension(f'{dirt}.{extension}')
        await ctx.message.delete()
        await ctx.send(f'{str(extension)}.py loaded', delete_after=3)
    except Exception as e:
        await ctx.send(f'Fail to load {dirt}.{extension}\n{e}', delete_after=3)

@client.command()
@is_owner()
async def unload(ctx, dirt, extension):
    try:
        client.unload_extension(f'{dirt}.{extension}')
        await ctx.message.delete()
        await ctx.send(f'{str(extension)}.py unloaded', delete_after=3)
    except Exception as e:
        await ctx.send(f'Fail to unload {dirt}.{extension}\n{e}', delete_after=3)

@client.command()
@is_owner()
async def reload(ctx, dirt, extension):
    try:
        client.unload_extension(f'{dirt}.{extension}')
        client.load_extension(f'{dirt}.{extension}')
        await ctx.message.delete()
        await ctx.send(f'{str(extension)}.py reloaded', delete_after=3)
    except Exception as e:
        await ctx.send(f'Fail to reload {dirt}.{extension}\n{e}', delete_after=3)

client.run(read_token(), bot=True, reconnect=True)
