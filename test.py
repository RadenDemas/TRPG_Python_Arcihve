from system import user as file

user = file.read_user_attr()
user_data_string = f"{user['name']}, {user['lv']}, {user['hp']}, {user['att']}, {user['armor']}, {user['exp']}"    
with open ("user_data.txt","w",encoding="utf+8") as mana:
    mana.write(user_data_string)