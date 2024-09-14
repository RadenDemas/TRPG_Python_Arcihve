from user import read_user_attr, user_data_info
from monster import read_monster_attr, monster_data_info
import os
import random

def user_defending() -> float:
    user = read_user_attr()
    user_armor = int(user['armor']) * 1.5
    return user_armor

def monster_defending() -> float:
    monster = read_monster_attr()
    monster_armor = int(monster['armor']) * 1.5
    return monster_armor

def user_attacking(defend):
    #Informatian user & monster data
    user = read_user_attr()
    monster = read_monster_attr()
    user_lv = user['lv']
    user_exp = user['exp']
    user_hp = int(user['hp'])
    user_att = int(user['att'])
    user_armor = int(user['armor'])
    monster_hp = float(monster['hp'])
    monster_att = int(monster['att'])
    monster_armor = int(monster['armor'])
    
    #attacking system
    if defend == True:
        monster_hp -= user_att-(monster_defending() * 0.5)
    elif defend != True:
        monster_hp -= user_att-(monster_armor*0.5)
        
    #discarding monster data
    if monster_hp <= 0 :
        os.remove('monster.txt')
        print(f"{monster['name']} telah dikalahkan")
    #returning user&monster data
    else:
        user_data_string = f" {user['name']},{user_lv}, {user_hp}, {user_att}, {user_armor},{user_exp}"
        with open("user_data.txt","w",encoding='utf+8') as user_file:
            user_file.write(user_data_string)
        monster_data_string = f'{monster["name"]},{monster_hp},{monster_att},{monster_armor}'
        with open("monster.txt","w",encoding='utf+8') as data:
            data.write(monster_data_string)
    
def monster_attack(defend,path):
    #informatian user & monster data
    user = read_monster_attr()
    monster = read_monster_attr()
    user_hp = int(user['hp'])
    user_att = int(user['att'])
    user_armor = int(user['armor'])
    monster_hp = float(monster['hp'])
    monster_att = int(monster['att'])
    monster_armor = int(monster['armor'])
    
    #attacking system
    if defend == True:
        user_hp -= monster_att-(user_defending()*0.5)
    elif defend != True:
        user_hp -= monster_att-(user_armor*0.5)
        
    #discarding user data
    if user_hp <= 0:
        os.remove('user_data.txt')
        print(f"{user['name']} telah dikalahkan oleh {monster['name']}")
        print(f'Selama ini kamu telah menyelesaikan sampai stage {path}')
        print('Silahkan untuk coba kembali, dan berjuang untuk menyelesaikan permainan')
        
    else: 
        user_data_string = f" {user['name']},{user['lv']}, {user_hp}, {user_att}, {user_armor},{user['exp']}"
        with open("user_data.txt","w",encoding='utf+8') as user_file:
            user_file.write(user_data_string)
        monster_data_string = f'{monster["name"]},{monster_hp},{monster_att},{monster_armor}'
        with open("monster.txt","w",encoding='utf+8') as data:
            data.write(monster_data_string)
            
def escape():
    escape_value = 5
    escape_persentage = random.randrange(0,10)
    if escape_persentage == escape_value:
        print("Kamu berhasil melarikan diri")
        os.remove('monster.txt')
    else:
        print("Kamu gagal melarikan diri")
        
        
def rest(chance):
    user = read_user_attr()
    user_hp = int(user['hp'])
    heal = user_hp *0.5
    if chance == 0:
        print("Kamu tidak bisa lagi beristirahat")
    elif chance != 0:
        print("Kamu sedang beristirahat")
        user_hp += user_hp * 0.5
        print(f"mengembalikan darah sebanyak {heal}")
        user_data_string = f" {user['name']},{user['lv']}, {user_hp}, {user['att']}, {user['armor']},{user['exp']}"
        with open ('user_data.txt',"w",encoding="utf+8") as data:
            data.write(user_data_string)    
    
def you_win():
    print("Selamat kamu telah mencapai puncak tertinggi dari tower ini")
    print('Kamu telah menaklukan tower ini, dan sekarang dunia telah aman')
    print("Terimakasih telah memainkan game ini")

if __name__ == "__main__":
    #escape()
    user_attacking(False)