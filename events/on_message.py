import json
from discord.ext import commands

class Message(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            pass
        # Long Beach
        elif message.guild.id == 696664282615513188:
            # Sugestões
            if message.channel.id == 739269608950857768 or message.channel.id == 700208889052004353:
                await message.add_reaction('✅')
                await message.add_reaction('❌')
        # LBPD
        elif message.guild.id == 865643871933038602:
            # Sugestões
            if message.channel.id == 865643875359391766 or message.channel.id == 865643872599408666:
                await message.add_reaction('✅')
                await message.add_reaction('❌')
            # Porte de Armas
            elif message.channel.id == 865643875846455310:
                await message.add_reaction('✅')
            # Medalha
            elif message.channel.id == 865643876865146942:
                with open('./database/medalhas.json') as medalhasid:
                    data = json.load(medalhasid)
                medalhas = []
                for x in data:
                    medalhas += x['captain']
                    medalhas += x['sergeant']
                    medalhas += x['corporal']

                medalha_id = message.content.strip('<').strip('>').replace('@', '').replace('&', '')
                if message.content.startswith('<@&'):
                    if not int(medalha_id) in medalhas:
                        await message.channel.send(f'{message.author.mention}, não existe esta medalha.', delete_after=3)
                        await message.delete(delay=3)
                    else:
                        await message.add_reaction('✅')
                        await message.add_reaction('❌')
                elif message.content != int:
                    await message.channel.send(f'{message.author.mention}, não existe esta medalha.', delete_after=3)
                    await message.delete(delay=3)
        #await self.client.process_commands(message)

def setup(client):
    client.add_cog(Message(client))
