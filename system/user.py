import random
def read_user_attr():
    with open("user_data.txt","r") as user:
        load_user = user.read()
        load_user = load_user.strip()
        load_user = load_user.split(',')
        user_name,user_lv,user_hp,user_att,user_armor,user_exp = load_user
        user_data = {
                'name' : user_name,
                'lv' : user_lv,
                'hp' : user_hp,
                'att' : user_att,
                'armor' : user_armor,
                'exp' : user_exp
            }
        return user_data
        
def load_game():
    try:
        with open("user_data.txt", mode="r", encoding="utf+8") as user:
            load_user = user.read()
            load_user = load_user.split()
            user_name,user_lv,user_hp,user_att,user_armor,user_exp = load_user
            user_data = {
                'name' : user_name,
                'lv' : user_lv,
                'hp' : user_hp,
                'att' : user_att,
                'armor' : user_armor,
                'exp' : user_exp
            }
            return user_data
    except FileNotFoundError:
        print("Data player tidak ditemukan\nmembuat data player baru...")
        with open("user_data.txt", mode="w", encoding="utf+8") as user:
            user_hp = random.randrange(10,20)
            user_att = random.randrange(3,5)
            user_armor = random.randrange(3,5)
            user_name = str(input("Berikan nama karakter anda: "))
            user_lv = 1
            user_exp = 0
            user_data = {
                'name' : user_name,
                'lv' : user_lv,
                'hp' : user_hp,
                'att' : user_att,
                'armor' : user_armor,
                'exp' : user_exp
            }
            user_data_string = f"{user_data['name']}, {user_data['lv']}, {user_data['hp']}, {user_data['att']}, {user_data['armor']}, {user_data['exp']}"
            user.write(user_data_string)
            
def user_lv_up():
    with open("user_data.txt", 'r') as user:
        read_user = user.read()
        read_user = read_user.split(",")
        user_name,user_lv,user_hp,user_att,user_armor,user_exp = read_user
        user_lv = int(user_lv)
        user_hp = int(user_hp)
        user_att = int(user_att)
        user_armor = int(user_armor)
        user_lv += 1
        user_hp += 5
        user_att += 2
        user_armor += 2
        user_data = {
                'name' : user_name,
                'lv' : user_lv,
                'hp' : user_hp,
                'att' : user_att,
                'armor' : user_armor,
                'exp' : user_exp
            }
        user_data_string = f"{user_data['name']}, {user_data['lv']}, {user_data['hp']}, {user_data['att']}, {user_data['armor']}, {user_data['exp']}"
        with open("user_data.txt", "w",encoding="utf+8") as file:
            file.write(user_data_string)
        #user.write(user_data_string)
        
def user_data_info():
    with open('user_data.txt', "r") as user:
        load_user = user.read()
        load_user = load_user.split(',')
        user_name,user_lv,user_hp,user_att,user_armor,user_exp = load_user
        user_data = f"""
        Name \t: {user_name}
        lv \t: {user_lv}
        hp \t: {user_hp}
        att \t: {user_att}
        armor \t: {user_armor}
        exp \t: {user_exp}"""
        return user_data
        
    
if __name__ == "__main__":
    #print(read_user_attr())
    user_lv_up()