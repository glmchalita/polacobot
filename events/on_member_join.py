from discord.ext import commands

class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Long Beach
        if member.guild.id == 696664282615513188:
            role = member.guild.get_role(699108448008405002)
            await member.add_roles(role)
            channel = member.guild.get_channel(880867172262498365)
            await channel.send(f'> {member.mention} entrou.')
        # LBPD
        if member.guild.id == 865643871933038602:
            role = member.guild.get_role(872270783446147102)
            await member.add_roles(role)
            channel = member.guild.get_channel(865643872151797774)
            await channel.send(f'> {member.mention} entrou.')
        # FTO
        if member.guild.id == 866729056203702284:
            role = member.guild.get_role(871412869420429323)
            await member.add_roles(role)
            channel = member.guild.get_channel(871405947753492521)
            await channel.send(f'> {member.mention} entrou.')
        # SID
        if member.guild.id == 871441311788580905:
            role = member.guild.get_role(871441311788580907)
            await member.add_roles(role)
            channel = member.guild.get_channel(871441314980442192)
            await channel.send(f'> {member.mention} entrou.')
        # STD
        if member.guild.id == 871447558248083456:
            role = member.guild.get_role(871447558248083458)
            await member.add_roles(role)
            channel = member.guild.get_channel(871447558248083464)
            await channel.send(f'> {member.mention} entrou.')
        # ASD
        if member.guild.id == 872100014883733505:
            role = member.guild.get_role(872100014883733507)
            await member.add_roles(role)
            channel = member.guild.get_channel(872100015567429632)
            await channel.send(f'> {member.mention} entrou.')

def setup(client):
    client.add_cog(Join(client))