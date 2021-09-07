import discord
from discord.ext import commands
from database.db_lb import *

class Staff(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role(715745604340416532, 696704111185363014, 696780472268619778)
    async def checkban(self, ctx, arg):
        await ctx.message.delete()
        identifier = check_ban(arg)
        for i in identifier:
            if str(i[0]).startswith('steam'):
                await ctx.send(i[0])

    @commands.command()
    @commands.has_any_role(715745604340416532, 696704111185363014, 696780472268619778)
    async def rename(self, ctx, id, age, name, *, args):
        await ctx.message.delete()
        rename_db(id, age, name, args)
        await ctx.send('Renomeado com sucesso.', delete_after=5)

    @commands.command()
    @commands.has_any_role('🔰┃Staff')
    async def vip(self, ctx, id):
        await ctx.message.delete()

        embed = discord.Embed(title='Selecione o tipo do VIP', description='**1.** Ruby\n**2.** Diamante\n**3.** Ouro',
                              color=discord.Color.from_rgb(47, 49, 54))
        msg = await ctx.send(embed=embed)
        emojis = ['1️⃣', '2️⃣', '3️⃣']
        for i in emojis:
            await msg.add_reaction(i)

        phone = ''
        rg = ''
        vehs_list = []

        try:
            reaction, user = await self.client.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and reaction.emoji in ['1️⃣', '2️⃣', '3️⃣'])
        except Exception as e:
            await ctx.channel.send('Falha inesperada')
            print(e)
        else:
            # Ruby
            if reaction.emoji == '1️⃣':
                vip = 'VIP Ruby'
                await msg.delete()

                # Número personalizado
                embed = discord.Embed(color=discord.Color.from_rgb(47, 49, 54))
                embed.add_field(name='NÚMERO PERSONALIZADO', value='Digite o número desejado, no formato a seguir:\n\n`XXX-XXX`')
                phone_msg = await ctx.send(embed=embed)
                ok = 0
                while ok == 0:
                    try:
                        message = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                    except Exception as e:
                        await ctx.channel.send('Falha inesperada')
                        print(e)
                    else:
                        if len(message.content) <= 6 or len(message.content) >= 8:
                            await message.delete()
                            await ctx.channel.send('Números devem conter seis (6) digitos mais o separador (-) no meio.', delete_after=3)

                        elif int(message.content.replace('-', '')) != int:
                            await message.delete()
                            await ctx.channel.send('Deve-se conter apenas números.')
                        else:
                            if check_num(message.content) == 0:
                                await message.delete()
                                phone = message.content
                                ok = 1
                            elif check_num(message.content) == 1:
                                await message.delete()
                                await ctx.channel.send('Número indisponível ou inválido, por favor enviar novamente.', delete_after=3)
                await phone_msg.delete()

                # Registro Personalizado
                embed = discord.Embed(color=discord.Color.from_rgb(47, 49, 54))
                embed.add_field(name='REGISTRO PERSONALIZADO', value='Digite o registro desejado, no formato a seguir:\n\n`12345678`')
                embed.set_footer(text='Lembre-se que o registro deve conter oito (8) caracteres, sendo eles apenas letras e números.')
                rg_msg = await ctx.send(embed=embed)
                ok = 0
                while ok == 0:
                    try:
                        message = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                    except Exception as e:
                        await ctx.channel.send('Falha inesperada')
                        print(e)
                    else:
                        if len(message.content) <= 7 or len(message.content) >= 9:
                            await message.delete()
                            await ctx.channel.send('Registros devem conter oito (8) caracteres.', delete_after=3)
                        else:
                            if check_rg(message.content) == 0:
                                await message.delete()
                                rg = message.content
                                ok = 1
                            elif check_rg(message.content) == 1:
                                await message.delete()
                                await ctx.channel.send('Registro indisponível ou inválido, por favor enviar novamente.', delete_after=3)

                vehs_choices = ['amarok', 'audirs6', 'bmwm3f80', 'bmwm8', 'fc15', 'ferrariitalia', 'lamborghinihuracan', 'lamtmc',
                                'lancerevolutionx', 'fordmustang',
                                'nissangtr', '911r', '18macan', 'teslaprior', 'nissanskyliner34', 'cla45', '2019zr1c', '19tundra',
                                'africat', 's1000rr', 'r1250', 'zx10r', 'f850gs']
                await rg_msg.delete()

                # Veículos
                embed = discord.Embed(color=discord.Color.from_rgb(47, 49, 54))
                embed.add_field(name='VEÍCULOS', value='Informe os veículos de acordo com a lista abaixo, no modelo a seguir:\n\n`1 2 3`',
                                inline=False)
                embed.add_field(name='A', value=f'1. {vehs_choices[0]}\n2. {vehs_choices[1]}\n3. {vehs_choices[2]}\n4. {vehs_choices[3]}',
                                inline=True)
                embed.add_field(name='B', value=f'5. {vehs_choices[4]}\n6. {vehs_choices[5]}\n7. {vehs_choices[6]}\n8. {vehs_choices[7]}',
                                inline=True)
                embed.add_field(name='C',
                                value=f'9. {vehs_choices[8]}\n10. {vehs_choices[9]}\n11. {vehs_choices[10]}\n12. {vehs_choices[11]}',
                                inline=True)

                embed.add_field(name='D',
                                value=f'13. {vehs_choices[12]}\n14. {vehs_choices[13]}\n15. {vehs_choices[14]}\n16. {vehs_choices[15]}',
                                inline=True)
                embed.add_field(name='E',
                                value=f'17. {vehs_choices[16]}\n18. {vehs_choices[17]}\n19. {vehs_choices[18]}\n20. {vehs_choices[19]}',
                                inline=True)
                embed.add_field(name='F', value=f'21. {vehs_choices[20]}\n22. {vehs_choices[21]}\n23. {vehs_choices[22]}', inline=True)
                embed.set_footer(
                    text='Informe os veículos de acordo com os números representantes de cada modelo, separando cada por um espaço.')
                vehs_msg = await ctx.send(embed=embed)
                ok = 0
                while ok == 0:
                    try:
                        message = await self.client.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                    except Exception as e:
                        await ctx.channel.send('Falha inesperada')
                        print(e)
                    else:
                        contexto = message.content.replace(' ', '')
                        if int(contexto) != int:
                            cars = message.content.split(' ')
                            veh = ''
                            for i in cars:
                                if int(i) == 1: veh = 'amarok'
                                if int(i) == 2: veh = 'audirs6'
                                if int(i) == 3: veh = 'bmwm3f80'
                                if int(i) == 4: veh = 'bmwm8'
                                if int(i) == 5: veh = 'fc15'
                                if int(i) == 6: veh = 'ferrariitalia'
                                if int(i) == 7: veh = 'lamborghinihuracan'
                                if int(i) == 8: veh = 'lamtmc'
                                if int(i) == 9: veh = 'lancerevolutionx'
                                if int(i) == 10: veh = 'fordmustang'
                                if int(i) == 11: veh = 'nissangtr'
                                if int(i) == 12: veh = '911r'
                                if int(i) == 13: veh = '18macan'
                                if int(i) == 14: veh = 'teslaprior'
                                if int(i) == 15: veh = 'nissanskyliner34'
                                if int(i) == 16: veh = 'cla45'
                                if int(i) == 17: veh = '2019zr1c'
                                if int(i) == 18: veh = '19tundra'
                                if int(i) == 19: veh = 'africat'
                                if int(i) == 20: veh = 's1000rr'
                                if int(i) == 21: veh = 'r1250'
                                if int(i) == 22: veh = 'zx10r'
                                if int(i) == 23: veh = 'f850gs'
                                vehs_list.append(veh)

                            if check_vehs(id, vehs_list[0]) == 1:
                                await message.delete()
                                await ctx.channel.send(
                                    f'O veículo {vehs_list[0]} já se encontra na garagem do ID {id}. Envie novamente os veículos desejados.',
                                    delete_after=3)
                                vehs_list.clear()

                            elif check_vehs(id, vehs_list[1]) == 1:
                                await message.delete()
                                await ctx.channel.send(
                                    f'O veículo {vehs_list[1]} já se encontra na garagem do ID {id}. Envie novamente os veículos desejados.',
                                    delete_after=3)
                                vehs_list.clear()

                            elif check_vehs(id, vehs_list[2]) == 1:
                                await message.delete()
                                await ctx.channel.send(
                                    f'O veículo {vehs_list[2]} já se encontra na garagem do ID {id}. Envie novamente os veículos desejados.',
                                    delete_after=3)
                                vehs_list.clear()

                            elif check_vehs(id, vehs_list[0]) == 0 and check_vehs(id, vehs_list[1]) == 0 and check_vehs(id, vehs_list[2]) == 0:
                                vehs_list.append(veh)
                                ok = 1
                                await message.delete()
                await vehs_msg.delete()

                # Confirmação
                embed = discord.Embed(color=discord.Color.from_rgb(47, 49, 54))
                embed.add_field(name='BENEFÍCIOS ESCOLHIDOS',
                                value=f'**Número:** {phone}\n**Registro:** {rg}\n**Veículos:** {vehs_list[0]} / {vehs_list[1]} / {vehs_list[2]}')
                confirm_msg = await ctx.send(embed=embed)
                confirm_emojis = ['✅', '❌']
                for i in confirm_emojis:
                    await confirm_msg.add_reaction(i)
                try:
                    reaction, user = await self.client.wait_for('reaction_add',
                                                           check=lambda reaction, user: user == ctx.author and reaction.emoji in ['✅', '❌'])
                except Exception as e:
                    await ctx.channel.send('Falha inesperada')
                    print(e)
                else:
                    if reaction.emoji == '✅':
                        await confirm_msg.delete()
                        entrega_log = self.client.get_channel(880411785235140631)
                        text = f'```Entregue por: {ctx.author.display_name}\nTicket: {ctx.channel.name[7:13]}\nPlayer: {get_name(id)}\nSteamHEX: {get_steam(id)}\n' \
                               f'Benefício: {vip}\nNúmero: {phone}\nRegistro: {rg}\nVeículos: {vehs_list[0]} / {vehs_list[1]} / {vehs_list[2]}```'
                        await entrega_log.send(text)

            elif reaction.emoji == '2️⃣':
                await ctx.channel.send('Diamante')
            elif reaction.emoji == '3️⃣':
                await ctx.channel.send('Ouro')

def setup(client):
    client.add_cog(Staff(client))
