import discord
import json
from datetime import datetime, timedelta
from pytz import timezone
from discord.utils import get, find
from discord.ext import commands
from database.db_lb import *

class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            pass
        # LBPD
        elif payload.guild_id == 865643871933038602:
            # Ponto Eletronico
            if payload.channel_id == 877843977666166794:
                channel = self.client.get_channel(payload.channel_id)
                avatar = self.client.get_user(payload.user_id).avatar_url

                member_split = (payload.member.nick.split(' '))
                badge = int(member_split[0])
                j = len(member_split)
                nome = " ".join(member_split[1:j])

                await channel.purge(limit=1)
                hour = datetime.now(timezone('Brazil/East')).strftime("%H:%M:%S")

                # NEW OFFICER
                if get_pol_badge(badge) is None:
                    entrada = discord.Embed(description=f'`ENTRADA` {hour[0:5]}\n`TRABALHANDO NO MOMENTO`',
                                            color=discord.Color.from_rgb(255, 204, 0))
                    entrada.set_author(name=f'{badge} {nome}', icon_url=avatar)
                    msg = await channel.send(embed=entrada)
                    new_pol_officer(badge, hour, msg.id)

                # OFFICER
                elif get_pol_badge(badge) is not None:
                    # ENTRANDO SERVIÇO
                    if get_pol_status(badge) == 0:
                        entrada = discord.Embed(description=f'`ENTRADA` {hour[0:5]}\n`TRABALHANDO NO MOMENTO`',
                                                color=discord.Color.from_rgb(255, 204, 0))
                        entrada.set_author(name=f'{badge} {nome}', icon_url=avatar)
                        msg = await channel.send(embed=entrada)
                        pol_updt(badge, 1, hour, msg.id)
                    # SAINDO SERVIÇO
                    elif get_pol_status(badge) == 1:
                        servico = datetime.strptime(str(hour), '%H:%M:%S') - datetime.strptime(str(get_pol_hour(badge)), '%H:%M:%S')
                        if servico.days < 0:
                            servico = timedelta(days=0, seconds=servico.seconds, microseconds=servico.microseconds)

                        seconds = int(servico.total_seconds())
                        if seconds < 60:
                            saida = discord.Embed(
                                description=f':x: `{badge} {nome}`, seu ponto teve menos de **UM MINUTO**, sendo assim não válido.',
                                color=discord.Color.from_rgb(255, 0, 0))
                            await channel.send(embed=saida, delete_after=10)
                            dele = await channel.fetch_message(get_pol_msg(badge))
                            await dele.delete()
                        else:
                            expediente = seconds / 60
                            saida = discord.Embed(
                                description=f'`ENTRADA` {str(get_pol_hour(badge))[0:5]}\n`SAÍDA` {hour[0:5]}\n `EXPEDIENTE` **{int(expediente)}** minutos',
                                color=discord.Color.from_rgb(0, 198, 0))
                            saida.set_author(name=f'{badge} {nome}', icon_url=avatar)
                            await channel.send(embed=saida)
                            pol_updt(badge, 0, '00:00:00', 0)

                emb = discord.Embed(description='Reaja para **INICIAR** / **ENCERAR** seu turno', color=discord.Color.from_rgb(47, 49, 54))
                emb.set_author(name='Ponto Automático LBPD', icon_url='https://i.imgur.com/fwJ50Qh.png')
                text = await channel.send(embed=emb)
                await text.add_reaction('✅')
            # Porte de Armas OK
            elif payload.channel_id == 865643875846455310:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

                channel = self.client.get_channel(payload.channel_id)
                porte_channel = self.client.get_channel(871399643999793223)

                message = await channel.fetch_message(payload.message_id)
                role = find(lambda r: r.id == 865651613485367346, message.guild.roles)
                author = guild.get_member(payload.user_id)
                emoji = payload.emoji.name

                author_name = payload.member.nick

                if payload.emoji.name == '✅':
                    if role in author.roles:
                        await porte_channel.send(f'{message.content}Entregue por: **{author_name[3:]}**')
                    else:
                        await message.remove_reaction(emoji, author)
                else:
                    await message.remove_reaction(emoji, author)
            # Medalhas OK
            elif payload.channel_id == 865643876865146942:
                try:
                    channel = self.client.get_channel(payload.channel_id)
                    channel_log = self.client.get_channel(865643876865146944)
                    message = await channel.fetch_message(payload.message_id)
                    emoji = payload.emoji.name

                    guild_id = payload.guild_id
                    guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)

                    author = message.author  # Solicitante
                    user = self.client.get_user(payload.user_id)  # Outorgante

                    userid = payload.user_id
                    member = guild.get_member(userid)

                    roles = member.roles
                    roles.reverse()
                    top_role = roles[0]

                    captain = get(guild.roles, id=865649143523049492)
                    sergeant = get(guild.roles, id=865649052569305108)
                    corporal = get(guild.roles, id=865649020550381569)

                    medalha_id = message.content.strip('<').strip('>').replace('@', '').replace('&', '')
                    medalha = get(guild.roles, id=int(medalha_id))

                    with open('./database/medalhas.json') as medalhasid:
                        data = json.load(medalhasid)
                    captain_medalhas = []
                    sergeant_medalhas = []
                    corporal_medalhas = []
                    for x in data:
                        captain_medalhas = x['captain']
                        sergeant_medalhas = x['sergeant']
                        corporal_medalhas = x['corporal']

                    if author == user:
                        await message.remove_reaction(emoji, user)
                        await channel.send(f'{user.mention}, você não tem permissão para conceder medalha a si próprio. :sleeping:',
                                           delete_after=3)
                    elif int(medalha_id) in captain_medalhas:
                        if top_role >= captain:
                            if emoji == '✅':
                                await author.add_roles(medalha)
                                await channel_log.send(f'{user.mention} condeceu {medalha.mention} para {author.mention}')
                                await message.delete()
                            elif emoji == '❌':
                                await channel_log.send(f'{user.mention} não concedeu {medalha.mention} para {author.mention}')
                                await author.send(f'A solicitação da {medalha} não foi aprovada.')
                                await message.delete()
                        elif top_role < captain:
                            await message.remove_reaction(emoji, user)
                            await channel.send(f'{user.mention}, esta medalha pode ser apenas concedida por Captain +.', delete_after=3)
                    elif int(medalha_id) in sergeant_medalhas:
                        if top_role >= sergeant:
                            if emoji == '✅':
                                await author.add_roles(medalha)
                                await channel_log.send(f'{user.mention} condeceu {medalha.mention} para {author.mention}')
                                await message.delete()
                            elif emoji == '❌':
                                await channel_log.send(f'{user.mention} não concedeu {medalha.mention} para {author.mention}')
                                await author.send(f'A solicitação da {medalha} não foi aprovada.')
                                await message.delete()
                        elif top_role < sergeant:
                            await message.remove_reaction(emoji, user)
                            await channel.send(f'{user.mention}, esta medalha pode ser apenas concedida por Sergeant +.', delete_after=3)
                    elif int(medalha_id) in corporal_medalhas:
                        if top_role >= corporal:
                            if emoji == '✅':
                                await author.add_roles(medalha)
                                await channel_log.send(f'{user.mention} condeceu {medalha.mention} para {author.mention}')
                                await message.delete()
                            elif emoji == '❌':
                                await channel_log.send(f'{user.mention} não concedeu {medalha.mention} para {author.mention}')
                                await author.send(f'A solicitação da {medalha} não foi aprovada.')
                                await message.delete()
                        elif top_role < corporal:
                            await message.remove_reaction(emoji, user)
                            await channel.send(f'{user.mention}, esta medalha pode ser apenas concedida por Corporal +.', delete_after=3)
                except Exception as e:
                    print(e)

def setup(client):
    client.add_cog(Reaction(client))
