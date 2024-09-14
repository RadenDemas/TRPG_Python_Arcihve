import os
import user

""" monster_spawn = monster_info(hp1 = 5, hp2= 10, att1= 2, att2= 5, armor1= 1, armor2=3)
while True:
    print(monster_spawn['hp'])
    monster_spawn['hp'] -= 1
    if monster_spawn['hp'] == 0:
        print("Monster Telah Mati")
        break """
print(user.load_game())

os.remove('monster.txt')