import discord

from discord.ext import commands
from discord.utils import find
from colorama import init

def get_data():
    data = []
    with open('./database/wl.txt', mode='r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.split(' ')
        return data

def write(arg):
    with open('./database/wl.txt', mode='a') as file:
        file.write(arg)

def remove(arg):
    data = get_data()
    data.remove(f'{arg}')
    with open('./database/wl.txt', mode='w') as file:
        new_data = ''
        for i in data:
            new_data += f'{i} '
        file.write(new_data.rstrip())

def clear():
    with open('./database/wl.txt', mode='w') as file:
        file.write('')

init()
class Whitelist(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role(715745604340416532, 696704111185363014, 696780472268619778)
    async def wl(self, ctx, *, args):
        await ctx.message.delete()
        guild = discord.utils.find(lambda g: g.id == ctx.guild.id, self.client.guilds)
        ids = args.split(' ')
        try:
            for i in ids:
                user = guild.get_member(int(i))
                if guild.get_member(int(i)) is not None:
                    if len(get_data()) == 0:
                        write(i)
                        await ctx.send(f'{user.mention} adicionado na lista.', delete_after=5)
                    else:
                        if i in get_data():
                            await ctx.send(f'Usuário {user.mention} ({i}) já está na lista de aprovação.', delete_after=5)
                        else:
                            write(f' {i}')
                            await ctx.send(f'{user.mention} adicionado na lista.', delete_after=5)
                else:
                    await ctx.send(f'ID {i} não encontrado.', delete_after=3)
        except ValueError:
            await ctx.send('**Error:** Informe apenas os números do ID.', delete_after=3)
        except Exception as e:
            await ctx.send('Erro inesperado.', delete_after=5)
            print(f'\033[93mError at WL command in whitelist.py:\033[0m \033[91m{e}\033[0m')

    @commands.command()
    @commands.has_any_role(715745604340416532, 696704111185363014, 696780472268619778)
    async def preview(self, ctx):
        await ctx.message.delete()

        guild = discord.utils.find(lambda g: g.id == ctx.guild.id, self.client.guilds)
        if len(get_data()) == 0:
            await ctx.send('A lista está vazia.', delete_after=5)
        else:
            await ctx.send('Aprovados até o momento:\n', delete_after=15)
            for i in get_data():
                try:
                    user = guild.get_member(int(i))
                    if user is None:
                        await ctx.send(f'Usuário **{i}** não encontrado no Discord.', delete_after=15)
                    else:
                        await ctx.send(f'{user.mention}', delete_after=15)
                except Exception as e:
                    await ctx.send(f'Erro inesperado.')
                    print(f'\033[93mError at PREVIEW command in whitelist.py:\033[0m \033[91m{e}\033[0m')

    @commands.command()
    @commands.has_any_role(715745604340416532, 696704111185363014, 696780472268619778)
    async def remove(self, ctx, arg):
        await ctx.message.delete()
        guild = discord.utils.find(lambda g: g.id == ctx.guild.id, self.client.guilds)

        try:
            if arg in get_data():
                user = guild.get_member(int(arg))
                if user is None:
                    await ctx.send(f'Usuário não encontrado no Discord, removido automaticamente da lista.', delete_after=5)
                    remove(arg)
                else:
                    await ctx.send(f'{user.mention} removido da lista.',delete_after=5)
                    remove(arg)
            else:
                await ctx.send(f'ID {arg} não encontrado na lista.',delete_after=5)
        except ValueError:
            await ctx.send('**Error:** Informe apenas o número do ID.', delete_after=5)
        except Exception as e:
            print(f'\033[93mError at REMOVE command in whitelist.py:\033[0m \033[91m{e}\033[0m')

    @commands.command()
    @commands.has_any_role(715745604340416532, 696704111185363014, 696780472268619778)
    async def soltarwl(self, ctx):
        await ctx.message.delete()

        guild = discord.utils.find(lambda g: g.id == ctx.guild.id, self.client.guilds)
        entrevista = find(lambda r: r.id == 705983623605649408, guild.roles)
        visitante = find(lambda r: r.id == 699108448008405002, guild.roles)
        resultado = self.client.get_channel(794221059653763103)
        suporte = self.client.get_channel(765547260686630933)
        not_found = []

        for i in get_data():
            try:
                user = guild.get_member(int(i))
                if user is None:
                    not_found.append(i)
                else:
                    await resultado.send(f'Parabéns {user.mention}! Você foi aprovado! <:nha:745948202028630066>')
                    if visitante in user.roles:
                        await user.remove_roles(visitante)
                        await user.add_roles(entrevista)
                    elif visitante not in user.roles:
                        await user.add_roles(entrevista)
            except Exception as e:
                print(f'\033[93mError at SOLTARWL command in whitelist.py:\033[0m \033[91m{e}\033[0m')

        for i in not_found:
            await suporte.send(f'ID {i} aprovado, mas não foi encontrado no Discord.')

        clear()
        not_found.clear()

    @wl.error
    @preview.error
    @remove.error
    @soltarwl.error
    async def check_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.message.delete()
            await ctx.send(f'Você não tem permissão para utilizar este comando.', delete_after=3)

def setup(client):
    client.add_cog(Whitelist(client))