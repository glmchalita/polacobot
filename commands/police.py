import discord
from discord.ext import commands
from discord.utils import find

class Police(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def embed(self, ctx, arg):
        try:
            await ctx.message.delete()
            if arg == 'mapa':
                text = discord.Embed(title='MAPEAMENTO', description='EM BREVE', color=discord.Color.from_rgb(47, 49, 54))
                await ctx.send(embed=text)

            if arg == 'mapa1':
                text = discord.Embed(title='Cidade', color=discord.Color.from_rgb(47, 49, 54))
                text.set_image(url='https://i.imgur.com/VFiUHI5.png')
                await ctx.send(embed=text)

                text = discord.Embed(title='Banco Central', color=discord.Color.from_rgb(47, 49, 54))
                text.set_image(url='https://i.imgur.com/Ef2Rt2f.png')
                await ctx.send(embed=text)

                text = discord.Embed(title='Banco de Paleto', color=discord.Color.from_rgb(47, 49, 54))
                text.set_image(url='https://i.imgur.com/6azvMFI.png')
                await ctx.send(embed=text)

                text = discord.Embed(title='Joalheria', color=discord.Color.from_rgb(47, 49, 54))
                text.set_image(url='https://i.imgur.com/W8fPPor.png')
                await ctx.send(embed=text)

                text = discord.Embed(title='Zona Echo Amarela', color=discord.Color.from_rgb(47, 49, 54))
                text.set_image(url='https://i.imgur.com/6mMVrjE.png')
                await ctx.send(embed=text)

                text = discord.Embed(title='Zona Echo Vermelha', color=discord.Color.from_rgb(47, 49, 54))
                text.set_image(url='https://i.imgur.com/qh5UdPi.png')
                await ctx.send(embed=text)

                text = discord.Embed(title='Zona Echo Verde', color=discord.Color.from_rgb(47, 49, 54))
                text.set_image(url='https://i.imgur.com/adns0nc.png')
                await ctx.send(embed=text)

                text = discord.Embed(title='Zona Echo Roxa', description='Em breve...', color=discord.Color.from_rgb(47, 49, 54))
                await ctx.send(embed=text)

            if arg == 'site':
                text = discord.Embed(
                    title='Apostilas',
                    description=
                    '[**Curso de Noções Básicas (NB)**](https://docs.google.com/document/d/1f8SvODKBwAEsG-TCEAHmbt6VOU3Pn0b2)\n\n'
                    '[**Curso de Modulação na Central (MC)**](https://docs.google.com/document/d/1HRWS97M5jQ2gWkFOnvSk_tng9eH_5kCa)\n\n'
                    '[**Curso de Abordagem (AB)**](https://docs.google.com/document/d/1Xpwlpq7jGOIDzOkW0hSw9YcgyjQlnRNa)\n\n'
                    '[**Curso de Armas (AR)**](https://docs.google.com/document/d/1TKPm6ESW29ZT8270ZPHuObv7nylN1CO9)\n\n'
                    '[**Curso de Perseguição (P)**](https://docs.google.com/document/d/1_AIg68UASqPm11MOTozLoXOGFcK2-WX4)\n\n'
                    '[**Manual de Conduta**](https://docs.google.com/document/d/1L5D_U4u_2lIDEy5QXTOW6hSIPAWZiCcR)\n\n'
                    '[**Manual do Oficial**](https://docs.google.com/document/d/1Flzj3PrEmWEEjTbUgNU3Y5t9pcv9EAuh)\n\n'
                    '[**Manual da F.T.O**](https://docs.google.com/document/d/1p0DJWG7GrfATSotNwvZvf8eLkvINrTRY)\n\n'
                    '[**Manual da S.I.D**](https://docs.google.com/document/d/15hc51LJB7wSWabiNqNxUCfcIBVNc7Muc)\n\n'
                    '[**Manual da S.T.D**](https://docs.google.com/document/d/1lDbTmpkhhD7kXTOgY3EQ6z742SVn-zTA)\n\n'
                    '[**Manual da A.S.D**](https://docs.google.com/document/d/1WxwqUAE5ffM7gM2vfzId1bhE3rZDDQHN)\n\n',
                    color=discord.Color.from_rgb(47, 49, 54))

                text1 = discord.Embed(
                    title='Registros',
                    description=
                    '[**Registro Patrol**](https://docs.google.com/spreadsheets/d/1slFKYo3dGepb1nZzwF-lgbsymx0-bxD4DvsXDZ6t2sE/edit#gid=163132170)\n\n'
                    '[**Código Penal**](https://docs.google.com/document/d/1_dIgIOH7SszUnQKctKTLcNCDtUKPGJBpCbszMMSiBUc/edit)',
                    color=discord.Color.from_rgb(47, 49, 54))
                await ctx.send(embed=text)
                await ctx.send(embed=text1)

            if arg == 'medalha':
                role = find(lambda r: r.id == 878028131636748299, ctx.guild.roles)
                emb = discord.Embed(title='🏅 Solicitação de Medalhas',
                                    description='Para solicitar medalha, basta menciona-la no chat.\nApenas uma medalha por mensagem.',
                                    color=discord.Color.from_rgb(47, 49, 54))
                emb.add_field(name='Exemplo', value=f'{role.mention}')
                await ctx.send(embed=emb)

            if arg == 'ponto':
                emb = discord.Embed(description='Reaja para **INICIAR** / **ENCERAR** seu turno', color=discord.Color.from_rgb(47, 49, 54))
                emb.set_author(icon_url='https://i.imgur.com/fwJ50Qh.png', name='Ponto Automático LBPD')
                text = await ctx.send(embed=emb)
                await text.add_reaction('✅')
        except Exception as e:
            print(e)

    @commands.command()
    @commands.has_role('High Command')
    async def porte(self, ctx, user):
        await ctx.message.delete()
        try:
            channel = self.client.get_channel(871399643999793223)
            lb = self.client.get_guild(696664282615513188)
            lbid = (lb.get_member(int(user.strip('<').strip('>').replace('@!', '')))).nick.split(' ')

            i = (len(lbid)) - 1
            name = ctx.guild.get_member(int(user.strip('<').strip('>').replace('@!', ''))).nick.split(' ')

            o = len(name)

            author = ctx.author.display_name.split(' ')
            j = len(author)

            await channel.send(f'```md\n[{" ".join(name[1:o])}][{lbid[i]}]\n'
                               '[NÚMERO DA REQUISIÇÃO][PORTE MILITAR]\n'
                               '[RENOVAÇÃO EM:][Enquanto estiver servindo a corporação]\n'
                               '[STATUS][AUTORIZADO✅]```'
                               f'Entregue por: **{" ".join(author[1:j])}**')
        except Exception as e:
            print(e)

def setup(client):
    client.add_cog(Police(client))