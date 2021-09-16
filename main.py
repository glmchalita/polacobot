from functions import *

ensure = [
    'commands.whitelist',
    'commands.staff',
    'commands.police',
    'events.status',
    'events.on_message',
    'events.on_reaction',
    'events.on_member_join',
    'events.on_member_remove',
    'events.error',
    'events.booster',
    'events.on_ready'
]

if __name__ == '__main__':
    for ext in ensure:
        try:
            client.load_extension(ext)
            print(green(f'Loaded {ext}'))
        except Exception as e:
            print(yellow(f'Fail to load {ext}. {e}'))

@client.command()
@is_owner()
async def load(ctx, dirt, extension):
    try:
        client.load_extension(f'{dirt}.{extension}')
        await ctx.message.delete()
        await ctx.send(f'{str(extension)}.py loaded', delete_after=5)
    except Exception as x:
        await ctx.send(f'Fail to load {dirt}.{extension}\n{x}', delete_after=5)
    await ctx.message.delete()

@client.command()
@is_owner()
async def unload(ctx, dirt, extension):
    try:
        client.unload_extension(f'{dirt}.{extension}')
        await ctx.message.delete()
        await ctx.send(f'{str(extension)}.py unloaded', delete_after=3)
    except Exception as x:
        await ctx.send(f'Fail to unload {dirt}.{extension}\n{x}', delete_after=3)
    await ctx.message.delete()

@client.command()
@is_owner()
async def reload(ctx, dirt, extension):
    try:
        client.unload_extension(f'{dirt}.{extension}')
        client.load_extension(f'{dirt}.{extension}')
        await ctx.message.delete()
        await ctx.send(f'{str(extension)}.py reloaded', delete_after=3)
    except Exception as x:
        await ctx.send(f'Fail to reload {dirt}.{extension}\n{x}', delete_after=3)
    await ctx.message.delete()

    # CheckFailure from Main
    @load.error
    @unload.error
    @reload.error
    async def check_error(error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.delete()

client.run(read_token(), bot=True, reconnect=True)
