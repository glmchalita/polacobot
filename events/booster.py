import json
import yaml

from colorama import init
from discord.ext import commands
from discord.utils import find
from database.db_lb import *
from events.error import line
from functions import yellow, red

init()
class Booster(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # Long Beach
        lb_guild = self.client.get_guild(696664282615513188)
        logs = self.client.get_channel(877719255871799316)

        if before.guild == lb_guild:
            booster = find(lambda r: r.id == 804147778271313920, lb_guild.roles)  # BoosterID 700877452481921095
            citizen = find(lambda r: r.id == 696705832489975839, lb_guild.roles)

            try:
                # Role adicionada
                if len(before.roles) < len(after.roles):
                    if citizen in after.roles:
                        for x in after.roles:
                            if not x in before.roles:
                                if x == booster:
                                    try:
                                        lb_id = before.display_name.split(' ')
                                        j = len(lb_id) - 1
                                        if isinstance(int(lb_id[j]), int):
                                            user = users_data(lb_id[j])
                                            for y in user:
                                                datatable = yaml.load(y, Loader=yaml.SafeLoader)
                                                groups = datatable['groups']
                                                print(groups)
                                                groups['Booster'] = True
                                                datatable['groups'] = groups
                                                s = json.dumps(dict(datatable))
                                                print(s)
                                                updt_group(lb_id[j], s)
                                                await logs.send(f'> {before.mention} setado no grupo Booster')
                                    except ValueError:
                                        print(f'\033[93mError at on_member_update:\033[0m \033[91m{before.display_name}, usuário Booster sem ID no apelido.\033[0m')
                                    except Exception as e:
                                        print(yellow('Error at on_member_update add_role: '), red(e))
                                        #print(f'\033[93m\033[0m \033[91m{e}\033[0m')

                # Role removida
                if len(before.roles) > len(after.roles):
                    if citizen in after.roles:
                        for x in before.roles:
                            if not x in after.roles:
                                if x == booster:
                                    try:
                                        lb_id = before.display_name.split(' ')
                                        j = len(lb_id) - 1
                                        if isinstance(int(lb_id[j]), int):
                                            user = users_data(lb_id[j])
                                            for y in user:
                                                datatable = yaml.load(y, Loader=yaml.SafeLoader)
                                                groups = datatable['groups']
                                                role = ''
                                                for key in groups:
                                                    if key == 'Booster':
                                                        role = key
                                                del groups[role]
                                                datatable['groups'] = groups
                                                s = json.dumps(dict(datatable))
                                                updt_group(lb_id[j], s)
                                                await logs.send(f'> {before.mention} retirado do grupo Booster')
                                    except ValueError:
                                        print(f'\033[93mError at on_member_update:\033[0m \033[91m{before.display_name}, usuário Booster sem ID no apelido.\033[0m')

                                    except Exception as e:
                                        print(f'\033[93mError at on_member_update rem_role:\033[0m \033[91m{e} / line {line()}\033[0m')

            except Exception as e:
                print(f'\033[93mError at on_member_update:\033[0m \033[91m{e} / line {line()}\033[0m')

def setup(client):
    client.add_cog(Booster(client))
