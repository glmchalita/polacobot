from discord.ext import commands

class Remove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # LBPD
        if member.guild.id == 865643871933038602:
            channel = member.guild.get_channel(865643872151797774)
            await channel.send(f'> {member.mention} saiu.')
        # FTO
        if member.guild.id == 866729056203702284:
            channel = member.guild.get_channel(871405947753492521)
            await channel.send(f'> {member.mention} saiu.')
        # SID
        if member.guild.id == 871441311788580905:
            channel = member.guild.get_channel(871441314980442192)
            await channel.send(f'> {member.mention} saiu.')
        # STD
        if member.guild.id == 871447558248083456:
            channel = member.guild.get_channel(871447558248083464)
            await channel.send(f'> {member.mention} saiu.')
        # ASD
        if member.guild.id == 872100014883733505:
            channel = member.guild.get_channel(872100015567429632)
            await channel.send(f'> {member.mention} saiu.')

def setup(client):
    client.add_cog(Remove(client))