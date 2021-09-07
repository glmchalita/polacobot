import mysql.connector

def db(arg):
    with open("./database/db_user.txt", "r") as f:
        lines = f.readlines()
        return lines[arg].strip()
con = mysql.connector.connect(host=f'{db(0)}', port= f'{db(1)}', user=f'{db(2)}', password=f'{db(3)}')

def users_data(id):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute("SELECT `dvalue` FROM `lbdbs4`.`vrp_user_data` "
                       f"WHERE  `user_id`={id} AND `dkey`='vRP:datatable';")
        user_data = cursor.fetchone()
        cursor.close()
        con.close()
        return user_data

def updt_group(id, groups):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"UPDATE `lbdbs4`.`vrp_user_data` SET `dvalue` = '{groups}' WHERE  `user_id`= {id} AND `dkey`= 'vRP:datatable';")
        con.commit()
        cursor.close()
        con.close()

def get_banned():
    con.connect()
    if con.is_connected():
        cursor = con.cursor()

        ################ BAN SEASON 3 ####################
        ban_s3 = []
        cursor.execute(f"SELECT `id` FROM `lbdb`.`vrp_users` WHERE `banned`=1;")
        for i in cursor:
            ban_s3.append(i[0])
        ban_s3.sort()
        #print(len(ban_s3))

        ################# GET IDENTIFIERS ###############
        idd_s3 = []
        for i in ban_s3:
            cursor.execute(f"SELECT `identifier` FROM `lbdb`.`vrp_user_ids` WHERE `user_id`={i};")
            idd_s3.append(cursor.fetchall())

        ############## ID_S4 FROM BANNED ID_S3 ###########
        ids_s4 = []
        for i in idd_s3:
            y = len(i)
            for j in range(y):
                cursor.execute(f"SELECT `user_id` FROM `lbdbs4`.`vrp_user_ids` WHERE `identifier`='{i[j][0]}';")
                for x in cursor:
                    if x[0] not in ids_s4:
                        ids_s4.append(x[0])
        ids_s4.sort()
        #print(len(ids_s4))

        ########### CHECK ID_S4 HAS WL ############
        wl = []
        for i in ids_s4:
            cursor.execute(f"SELECT `id` FROM `lbdbs4`.`vrp_users` WHERE `id`='{i}' AND `whitelisted`='1' AND `banned`='0';")
            for x in cursor:
                wl.append(x[0])
        print(wl)

        ############ GET IDENTIFIER FROM WHO HAS WL ############
        idd_s4 = []
        for i in wl:
            cursor.execute(f"SELECT `identifier` FROM `lbdbs4`.`vrp_user_ids` WHERE `user_id`='{i}';")
            idd_s4.append(cursor.fetchall())

        ############ GET ID_S3 WHO HAS WL ############
        ids_s3 = []
        for i in idd_s4:
            y = len(i)
            for j in range(y):
                cursor.execute(f"SELECT `user_id` FROM `lbdb`.`vrp_user_ids` WHERE `identifier`='{i[j][0]}';")
                for x in cursor:
                    if x[0] not in ids_s3:
                        ids_s3.append(x[0])
        print(ids_s3)

        ################## GET NAME AND BAN REASON ############
        ban_reason = []
        for i in ids_s3:
            cursor.execute(f"SELECT `id`, `ban_reason` FROM `lbdb`.`vrp_users` WHERE `id`='{i}';")
            ban_reason.append(cursor.fetchall())
        print(ban_reason)
                # ban = cursor.fetchone()
                # if len(ban) == 0:
                #     pass
                # else:
                #     if ban[0][1] == ban[0][1]:
                #         if ban[0][1] not in ids_s4:
                #             ids_s4.append(ban[0][1])
                #             test += f'\n{ban[0][1]} {ban[0][0]} '
                #         else:
                #             test += f'{ban[0][0]} '
        #
        # if test == '':
        #     pass
        # else:
        #     strip = test.rstrip().lstrip().split('\n')
        #     for lines in strip:
        #         strip2 = lines.rstrip().lstrip().split(' ')
        #         cursor.execute(f"SELECT `user_id` FROM `lbdb`.`vrp_user_ids` WHERE `identifier`='{strip2[1]}';")
        #         id_s3 = cursor.fetchone()
        #         print(f'S3: {id_s3[0]} S4: {strip2[0]}')
        cursor.close()
        con.close()

def check_match(identifier):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT `user_id` FROM `lbdbs4`.`vrp_user_ids` WHERE `identifier`='{identifier}';")
        player = cursor.fetchall()
        cursor.close()
        con.close()
        if len(player) == 0:
            return None
        else:
            return player

def rename_db(id, age, name, firstname):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"UPDATE `lbdbs4`.`vrp_user_identities` SET `name`='{name}',`firstname`='{firstname}',`age`={int(age)} WHERE  `user_id`={int(id)};")
        con.commit()
        cursor.close()
        con.close()

def check_num(phone):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM `lbdbs4`.`vrp_user_identities` WHERE `phone` = '{phone}';")
        result = cursor.fetchone()
        cursor.close()
        con.close()
        if result is None:
            return 0
        elif result is not None:
            return 1

def check_rg(rg):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM `lbdbs4`.`vrp_user_identities` WHERE `registration` = '{rg}';")
        result = cursor.fetchone()
        cursor.close()
        con.close()
        if result is None:
            return 0
        elif result is not None:
            return 1

def check_vehs(id, vehs):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM `lbdbs4`.`vrp_user_vehicles` WHERE `user_id` = '{id}' AND `vehicle` = '{vehs}';")
        result = cursor.fetchone()
        cursor.close()
        con.close()
        if result is None:
            return 0
        elif result is not None:
            return 1

def get_name(id):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT `name`, `firstname` FROM `lbdbs4`.`vrp_user_identities` WHERE `user_id` = '{id}';")
        result = cursor.fetchall()
        cursor.close()
        con.close()
        name = ''
        for i in result:
            name = f'{i[0]} {i[1]} | {id}'
        return name

def get_steam(id):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM `lbdbs4`.`vrp_user_ids` WHERE `user_id` = '{id}';")
        result = cursor.fetchall()
        cursor.close()
        con.close()
        steam = ''
        for i in result:
            if str(i[0]).startswith('steam'):
                steam = i[0][6:]
        return steam

# POLICIA
def new_pol_officer(badge, hour, msg_id):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO `lbdbs4`.`policia` (`badge`, `status`, `hour`, `msg_id`) VALUES ('{badge}', '1', '{hour}', '{msg_id}');")
        con.commit()
        cursor.close()
        con.close()

def pol_updt(badge, status, hour, msg_id):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"UPDATE `lbdbs4`.`policia` SET `status`='{status}', `hour`='{hour}', `msg_id`='{msg_id}' WHERE `badge`={badge};")
        con.commit()
        cursor.close()
        con.close()

def get_pol_badge(badge):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM `lbdbs4`.`policia` WHERE `badge` = '{badge}';")
        result = cursor.fetchone()
        cursor.close()
        con.close()
        if result is None:
            return None
        else:
            return result

def get_pol_status(badge):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT `status` FROM `lbdbs4`.`policia` WHERE `badge` = '{badge}';")
        result = cursor.fetchone()
        cursor.close()
        con.close()
        for i in result:
            return i

def get_pol_hour(badge):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT `hour` FROM `lbdbs4`.`policia` WHERE `badge` = '{badge}';")
        result = cursor.fetchone()
        cursor.close()
        con.close()
        for i in result:
            return i

def get_pol_msg(badge):
    con.connect()
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute(f"SELECT `msg_id` FROM `lbdbs4`.`policia` WHERE `badge` = '{badge}';")
        result = cursor.fetchone()
        cursor.close()
        con.close()
        for i in result:
            return i
