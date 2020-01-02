


import random

import sys

import time


import enemyclass


#__________________________________________________________________________________________________________________________________________________________________

Wackycks = 100

sanity = 0

ammo = 0

mana = 10

evasion = 20

cloth = 50

health = 100

stamina = 100

Melee_Damage = 10

current_weapon = ""

attack_total = 0

race = "human"

dev_footprint = ""

jabitem = 0

swipeitem = 0

throwitem = 0

cool_Down = 1

exp = 0

level = "Level"

total_level = 0

on = True







#____________________________________________________________________________________________________________________________________________________________________






def dice_100():
    return random.randint(0,100)

def combatant_picker():

     if dice_100() >= 0 and dice_100() <= 45:
        return zombies [0]

     elif dice_100() >= 46 and dice_100() <= 85:
        return zombies [1]
     elif dice_100() >= 86 and dice_100() <= 100:
        return zombies [2]



zombies = ['weak zombie' , 'normal zombie' , 'enhenced zombie']




def combatant_AI(number , player_attack_choice , z ):


    global attack_total
    global on
    global exp


    while True:


        if player_attack_choice == "jab":
            z.ehealth -= Melee_Damage + 15
            if attack_total > 0 :
                attack_total -= 1

        elif player_attack_choice == "swipe":
            z.ehealth -= Melee_Damage + 12.5
            if attack_total > 0 :
                attack_total -= 1

        elif player_attack_choice == "throw" and attack_total == 0 :
            z.ehealth -= Melee_Damage + 1
            attack_total = 4

        elif player_attack_choice == "throw" and attack_total > 0 and attack_total < 5:
            print("Cooling down your comput-oops. We are trying to grab the remains of that thing you threw at this monster. So you need ta wait a bit boi.")
            break

        elif player_attack_choice == "instant":
            z.ehealth -= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999




        if z.ehealth == 0 or z.ehealth < 0:

            exp += 50
            print("You killed a zombie. You are good. You gained 50 bulvels of exp.")
            exp_levelling(exp)
            on = False
            return 0


        if number >= 0 and number <= 4:
            return -1*(z.emelee_damage + 40)

        elif number >= 5 and number <= 14:
            return -1*(z.emelee_damage + 30)

        elif number >= 15 and number <= 45:
            return -1*(z.emelee_damage + 20)

        elif number >=45 and number <= 99:
            return -1*(z.emelee_damage + 15)

        elif number == 100:
            return 0
            print("You dodge the attack!")




def zombie_fight():


    #create an object , connect the object to zombie ai , within zombie ai throw object

    zombie = dice_100()
    global on
    on = True
    global enemiez
    enemiez = enemyclass.Enemy(combatant_picker())

    while on:

        #stats_sheet()

        while on:

            for item in backpack:

                if item == GameWeapons1["Lv1"+race][0]:
                    throwitem = item
                    jabitem = "fists"
                    swipeitem = "fists"
                elif item == GameWeapons1["Lv1"+race][1]:
                    jabitem = item
                    throwitem = "pencil"
                    swipeitem = "fists"
                elif item == GameWeapons1["Lv1"+race][2]:
                    swipeitem = item
                    throwitem = "pencil"
                    jabitem = "fists"
                else:
                    throwitem = "pencil"
                    jabitem = "fists"
                    swipeitem = "fists"




            global attack
            global dev_footprint




            if dev_footprint == "" :
                attack = input('''

                                        (1) You throw your {throw} |....Cooldown of 4 turns....|
                                        (2) You throw a jab with {jab}
                                        (3) You swipe with your {swipe}



                                  '''.format(throw = throwitem  , jab =  jabitem , swipe = swipeitem ))

                returned_damage = combatant_AI(enemiez.e_hit_percentage(),player_attack(attack) , enemiez)
                player_health(returned_damage)

            elif dev_footprint == "dev":

                attack = input('''

                                    (1) You throw your {throw} |....Cooldown of 4 turns....|
                                    (2) You throw a jab with {jab}
                                    (3) You swipe with your {swipe}
                                    (4) The mighty legendary attack : the 'instant'!!!



                              '''.format(throw = throwitem  , jab =  jabitem , swipe = swipeitem ))

                returned_damage = combatant_AI(enemiez.e_hit_percentage(),player_attack(attack) , enemiez)
                player_health(returned_damage)

            break






#______________________________________________________________________________________________________________________________________________________________________




def riders_AI(number , player_attack_choice):

    global attack_total
    global rhealth
    global on
    global exp

    while True:


        if player_attack_choice == "jab":
            rhealth -= Melee_Damage + 15
            if attack_total > 0 :
                attack_total -= 1

        elif player_attack_choice == "swipe":
            rhealth -= Melee_Damage + 12.5
            if attack_total > 0 :
                attack_total -= 1

        elif player_attack_choice == "throw" and attack_total == 0 :
            rhealth -= Melee_Damage + 1
            attack_total = 4

        elif player_attack_choice == "throw" and attack_total > 0 and attack_total < 5:
            print("Cooling down your comput-oops. We are trying to grab the remains of that thing you threw at this rider. So you need ta wait a bit boi.")
            break

        elif player_attack_choice == "instant":
            rhealth -= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999




        if rhealth == 0 or rhealth < 0:

            exp += 100
            print("You killed a rider that killed a lot of people. You are good. You gained 100 bulvels of exp.")
            exp_levelling(exp)
            on = False
            return 0


        if number >= 0 and number <= 4:
            return -1*(rmelee_damage + 40)

        elif number >= 5 and number <= 14:
            return -1*(rmelee_damage + 30)

        elif number >= 15 and number <= 45:
            return -1*(rmelee_damage + 20)

        elif number >=45 and number <= 99:
            return -1*(rmelee_damage + 15)

        elif number == 100:
            return 0
            print("You dodge the attack!")




def riders_fight():


    global rider
    rider = dice_100()
    global on
    on = True
    global riders_gang
    riders_gang = riderspick(rider)

    while on:

        stats_sheet()

        while on:

            for item in backpack:

                if item == GameWeapons1["Lv1"+race][0]:
                    throwitem = item
                    jabitem = "fists"
                    swipeitem = "fists"
                elif item == GameWeapons1["Lv1"+race][1]:
                    jabitem = item
                    throwitem = "pencil"
                    swipeitem = "fists"
                elif item == GameWeapons1["Lv1"+race][2]:
                    swipeitem = item
                    throwitem = "pencil"
                    jabitem = "fists"
                else:
                    throwitem = "pencil"
                    jabitem = "fists"
                    swipeitem = "fists"




            global attack
            global dev_footprint




            if dev_footprint == "" :
                attack = input('''

                                        (1) You throw your {throw} |....Cooldown of 4 turns....|
                                        (2) You throw a jab with {jab}
                                        (3) You swipe with your {swipe}



                                  '''.format(throw = throwitem  , jab =  jabitem , swipe = swipeitem ))

                returned_damage = riders_AI(riders_hit_percentage(),player_attack(attack))
                player_health(returned_damage)

            elif dev_footprint == "dev":

                attack = input('''

                                    (1) You throw your {throw} |....Cooldown of 4 turns....|
                                    (2) You throw a jab with {jab}
                                    (3) You swipe with your {swipe}
                                    (4) The mighty legendary attack : the 'instant'!!!



                              '''.format(throw = throwitem  , jab =  jabitem , swipe = swipeitem ))

                returned_damage = riders_AI(riders_hit_percentage(),player_attack(attack))
                player_health(returned_damage)

            break








#______________________________________________________________________________________________________________________________________________________________________









def weapon_cache(character_type):

    if character_type == "1":
        print(Lv1Human)
        weapon_human_choice_start = input('''

                     What weapon do you want?

                     Please type 1 - 2 - 3

                     _______________


                  ''')


        return human_cache[weapon_human_choice_start]

    elif character_type == "2":
        print(Lv1Werewolf)
        weapon_werewolf_choice_start = input('''

                     What weapon do you want?

                     Please type 1 - 2 - 3

                     _______________


                  ''')


        return human_cache[weapon_werewolf_choice_start]



def race():


    global race
    global health
    global sanity
    global Melee_Damage
    global cloth
    global mana
    global evasion
    global stamina
    while True:



        race = input('''Narrater: This is the part where you chose your race:

                 (1) Human |HP: 100 |Stamina: 100 Evasion: 20 |Melee Damage: 10 | Mana : 10 |
                 (2) Werewolf |HP: 300 |Stamina: 200 |Evasion: 0 |Melee Damage: 75 | /!\ CANNOT USE MAGIC /!\\
                 (3) Elf |HP: 50 |Stamina: 100 |Evasion: 50 | Melee Damage: 5 | Mana: 20 |
                 (4) Mage |HP: 50 |Stamina: 10 |Evasion: 25 |Mana: 100| Melee Damage: 10 | /!\ CANNOT USE FIREARMS /!\\
                 (5) Vampire |HP: 100 | Stamina: 100 |Evasion: 40 | Melee Damage: 20 |Mana: 50|

                 _______________


                 ''')

        if race == "1":
            print ("\n")
            race = "Human"
            break
        elif race == "2":
            Melee_Damage += 65
            stamina += 100
            health += 200
            cloth += 100
            evasion -= 20
            race = "Werewolf"
            print ("\n")
            break
        elif race == "3":
            health -= 50
            Melee_Damage -= 5
            cloth -= 50
            evasion += 30
            mana += 10
            race = "Elf"
        elif race == "4":
            health -= 50
            stamina -= 90
            mana += 100
            cloth -= 25
            evasion += 5
            race = "Mage"
            print ("\n")
            break
        elif race == "5":
            Melee_Damage +=20
            mana += 50
            cloth -=40
            evasion += 20
            race = "Vampire"
            print ("\n")
            break
        elif race == "DEV":
            Melee_Damage = 1
            health += 9999999999999999999
            mana += 50
            cloth -=40
            evasion += 20
            race = "dev"
            print("\n")
            break
        else:
            print ("\n")
            print ("Please chose ONE number between 1-5")
            continue




def finder(ID):

    global race
    global dev_footprint

    if ID == "Human":
        return GameWeapons1["Lv1Human"]

    elif ID == "Werewolf":
        return GameWeapons1["Lv1Werewolf"]

    elif ID == "Elf":
        return GameWeapons1["Lv1Elf"]

    elif ID == "Mage":
        return GameWeapons1["Lv1Mage"]

    elif ID == "Vampire":
        return GameWeapons1["Lv1Vampire"]
    elif ID == "dev":

        while True:
            dev_class = input('''Choose a class you want to work on...

                   1 "Lv1Human" : [knife , golf club , baseball bat
                   2 "Lv1Werewolf" :[axe , super duper heavy moon pan , sledge hammer
                   3 "Lv1Elf" : throwable knives , sharp stick , scissors
                   4 "Lv1Mage" : homemade flame thrower , poisonous stick , long stick
                   5 "Lv1Vampire" : wooden spear , butcher knife , enhenced bare teeth

                   _______________________________________________________________



                                                            ''')
            if dev_class == "1":
                dev_footprint = "dev"
                race = "Human"
                return GameWeapons1["Lv1Human"]

            elif dev_class == "2":
                dev_footprint = "dev"
                race = "Werewolf"
                return GameWeapons1["Lv1Werewolf"]

            elif dev_class == "3":
                dev_footprint = "dev"
                race = "Elf"
                return GameWeapons1["Lv1Elf"]

            elif dev_class == "4":
                dev_footprint = "dev"
                race = "Mage"
                return GameWeapons1["Lv1Mage"]

            elif dev_class == "5":
                dev_footprint = "dev"
                race = "Vampire"
                return GameWeapons1["Lv1Vampire"]
            else:
                print("invalid")
                continue



    else:
        print ("iFnvalid")




backpack = []

def inventory(item):
    if item == "e":
        print(backpack)
    else:
        backpack.append(item)



def player_health(inputed_damage):

    global health
    global on

    health += inputed_damage

    if health <= 0:
        print('''


                                        ________________________________________________
                                       |                                                |
                                       |                                                |
                                       |                                                |
                                       |                                                |
                                       |          :::::::game over:::::::               |
                                       |                                                |
                                       |                                                |
                                       |                                                |
                                       |                                                |
                                       |________________________________________________|



                    ''')
        time.sleep(5)
        on = False
        quit()







def shop(money):
    print("Welcome to Da Shop!")
    print("\n")
    print("\n")
    print("You have " , money , " wackycks")
    time.sleep(4)
    print("\n")
    ShopItemIdCard = finder(race)
    print('''

                                        ________________________________________________
                                       |                                                |
                                       |                ..Da shop..                     |
                                       |        {SIIC}                        |
                                       |                                                |
                                       |                                                |
                                       |                                                |
                                       |                                                |
                                       |                                                |
                                       |                                                |
                                       |________________________________________________|



          '''.format(SIIC = ShopItemIdCard))

    while True:

        shop_choice =  int(input("Please chose an item. In order to do so type 1 ; 2 ; 3. "))


        shop_choice -= 1

        if shop_choice == 0:
          inventory(ShopItemIdCard[shop_choice])
          break

        elif shop_choice == 1:
          inventory(ShopItemIdCard[shop_choice])
          break

        elif shop_choice == 2:
          inventory(ShopItemIdCard[shop_choice])
          break

        else:
          print("Did you read that sign over here?1 It says that you can only type a number between 1 and 3 to choose ")
          continue

GameWeapons1 = {"Lv1Human" : ['knife' , 'golf club' , 'baseball bat'],
                "Lv1Werewolf" :['axe' , 'super duper heavy moon pan' , 'sledge hammer'],
                "Lv1Elf" : ['throwable knives' , 'sharp stick' , 'scissors'],
                "Lv1Mage" : ['homemade flame thrower' , 'poisonous stick' , 'long stick'],
                "Lv1Vampire" : ['wooden spear' , 'butcher knife' , 'enhenced bare teeth']}




def player_attack(attack_choice):


    if dev_footprint == "":

        if attack_choice == "2":
            return "jab"

        elif attack_choice == "3":
            return "swipe"

        elif attack_choice == "1":
            return "throw"


    elif dev_footprint == "dev":
        if attack_choice == "2":
            return "jab"

        elif attack_choice == "3":
            return "swipe"

        elif attack_choice == "1":
            return "throw"
        elif attack_choice == "4":
            return "instant"



level = "LeveL "
total_level = 1
expOld = 80
display_lvl = "LeveL 1"

def exp_levelling(experience):
    global level
    global total_level
    global expOld
    global exp
    global display_lvl

    if experience >= expOld:

        total_level += 1
        expOld = round((expOld * 0.3) + expOld)
        level = level + str(total_level)
        display_lvl = level
        level = " LeveL "
        exp = 0


        print("You are now {l} !".format(l = level))
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")






enemy = enemyclass.Enemy(combatant_picker())
enemy.Combatant_Settings


