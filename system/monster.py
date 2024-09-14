from user import read_user_attr
import random
def create_monster () -> dict:
    #Creating Monster
    with open("library_monster.txt","r") as monster:
        monster = monster.readlines()
        choice_monster = monster[random.randrange(0,3)].strip()
        choice_monster = choice_monster.split(",")
        monster_name = choice_monster[0]
        list_attr = []
        for i in range(1,7):
            list_attr.append(int(choice_monster[i]))
        monster_attr = list_attr
        monster_hp = random.randrange(monster_attr[0],monster_attr[1])
        monster_att = random.randrange(monster_attr[2],monster_attr[3])
        monster_armor = random.randrange(monster_attr[4],monster_attr[5])
        
        #Lv_Adjusment
        user = read_user_attr()
        lv_adjusment = int(user["lv"])
        monster_hp += 3 * (lv_adjusment)
        monster_att += 1 * (lv_adjusment)
        monster_armor += 1 * (lv_adjusment)
        
        monster_data = {
            'name' : monster_name,
            'hp' : monster_hp,
            'att' : monster_att,
            'armor' : monster_armor
        }
        monster_data_string = f'{monster_data["name"]}, {monster_data["hp"]}, {monster_data["att"]}, {monster_data["armor"]}'
        with open("monster.txt","w",encoding='utf+8') as data:
            data.write(monster_data_string)
            
def create_boss(path):
    pass
            
def read_monster_attr():
    with open('monster.txt', "r") as monster:
        load_monster = monster.read()
        load_monster = load_monster.split(',')
        monster_name,monster_hp,monster_att,monster_armor = load_monster
        monster_data = {
            'name' : monster_name,
            'hp' : monster_hp,
            'att' : monster_att,
            'armor' : monster_armor
        }
        return monster_data
    
def monster_data_info():
    with open('monster.txt',"r") as monster:
        load_monster = monster.read()
        load_monster = load_monster.split(',')
        monster_name,monster_hp,monster_att,monster_armor = load_monster
        monster_data = f"""
        Name \t: {monster_name}
        hp \t: {monster_hp}
        att \t: {monster_att}
        armor \t: {monster_armor}"""
        return monster_data

if __name__ == "__main__":
    create_monster()
    pass 