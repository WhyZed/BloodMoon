
#___________________________________________________________________________IDEAS__________________________________________________________________________________

## --A new quest (go to scrivener):introducing players to magic step by step_For those who can't, it's 5 more points of sanity, as magic is insane ;)
## --Riders have different attacks - There are three possibilities attacks by riders- Utimate(20%)- Rare(30%) - Common(50%)             `
## --Make multiple fights possible
## --Make weapons and energy usable. For a fight you need to use stamina and if using firearms less stamina but need ammos
## --For mages, if he wants to specialize in firearms, then he becomse a warlock
## --Make hidden class (by either comleting hidden quests)
## --We can work on the actual graphics of the game
## --The absortion rate of everyone (armour)


#____________________________________________________________________MIIGHT NOT WORK BUT STIL...___________________________________________________________________

## --When we get to the point of fighting multiple enemies at once global "on" variable might be causing an error( e.g killing one player.could instantly kill the other)

#_________________________________________________________________________CHANGE LOG_______________________________________________________________________________
##1.13.5:
##    -Setup the attacks (not in-game) powers and name
##    -Wrote a bit more of the stroyline in Scrivener
##    -Coded of the past storyline
##    -Fixed bugs when killing a zombie, you needed to kill it it multiple times
##1.14.5:
##    -Separate zombies program and riders program on different file but still not delete them
##    -Might want a custom player.that want to flip a coin and if you answer in less than 1.5 sec:
##    -Convert riders list to a dictionary keys = type of riders and values as list = attacks for riders  {rider1: [super_attack,small attack]} ^^^ line above as well

#__________________________________________________________________________________________________________________________________________________________________

from timeit import default_timer as time

import time

import random

import sys

import GUI
import enemyclass
import player
#____________________________________________________________________________ZOMBIE_______________________________________________________________________________





zombies = ['weak zombie' , 'normal zombie' , 'enhenced zombie']
















def stats_sheet():



    print('''



                                        ________________________________________________
                                       |                                                |
                                       |             You are fighting a {ze}            |
                                       |                                                |
                                       |  His health: {zh}                              |
                                       |  His cloth: {zc}                               |
                                       |  His max damage (potential) : {zd}             |
                                       |________________________________________________|
                                       |                                                |
                                       |                 Your stats:                    |
                                       |                                                |
                                       |  {l}                                           |
                                       |  {pp}/{p}                                      |
                                       |                                                |
                                       |  Health: {h}                                   |
                                       |  Your damages (without the weapons): {m}       |
                                       |  How many clothes you have: {c}                |
                                       |  Range Cooldown: {r}                           |
                                       |________________________________________________|



           '''.format(zh = zhealth , zc = zcloth , zd = zmelee_damage , ze = enemiez  , h = health , m = Melee_Damage , c = cloth , r = attack_total , l = display_lvl , p = expOld , pp = exp))



#_____________________________________________________________________________RIDER________________________________________________________________________________

def riderspick(pick):
    if pick >= 0 and pick <= 25:
        riders_stats(riders[0])
        return riders[0]


    if pick >= 26 and pick <= 35:
        riders_stats(riders[3])
        return riders[3]


    if pick >= 36 and pick <= 60:
        riders_stats(riders[1])
        return riders[1]


    if pick >= 61 and pick <= 75:
        riders_stats(riders[4])
        return riders[4]


    if pick >= 76 and pick <= 100:
        riders_stats(riders[2])
        return riders[2]




#__________________________________________________________________________________________________________________________________________________________________





#def game():



##def delay_print(s):
##    for c in s:
##        sys.stdout.write(c)
##        sys.stdout.flush()
##        time.sleep(0.001)
##
##delay_print('''
##
##     ...     ..            ..                            ..              ...     ..      ..
##  .=*8888x <"?88h.   x .d88"                           dF              x*8888x.:*8888: -"888:
## X>  '8888H> '8888    5888R          u.          u.   '88bu.          X   48888X `8888H  8888          u.          u.      u.    u.
##'88h. `8888   8888    '888R    ...ue888b   ...ue888b  '*88888bu      X8x.  8888X  8888X  !888>   ...ue888b   ...ue888b   x@88k u@88c.
##'8888 '8888    "88>    888R    888R Y888r  888R Y888r   ^"*8888N     X8888 X8888  88888   "*8%-  888R Y888r  888R Y888r ^"8888""8888"
## `888 '8888.xH888x.    888R    888R I888>  888R I888>  beWE "888L    '*888!X8888> X8888  xH8>    888R I888>  888R I888>   8888  888R
##   X" :88*~  `*8888>   888R    888R I888>  888R I888>  888E  888E      `?8 `8888  X888X X888>    888R I888>  888R I888>   8888  888R
## ~"   !"`      "888>   888R    888R I888>  888R I888>  888E  888E      -^  '888"  X888  8888>    888R I888>  888R I888>   8888  888R
##  .H8888h.      ?88    888R   u8888cJ888  u8888cJ888   888E  888F       dx '88~x. !88~  8888>   u8888cJ888  u8888cJ888    8888  888R
## :"^"88888h.    '!    .888B .  "*888*P"    "*888*P"   .888N..888      .8888Xf.888x:!    X888X.:  "*888*P"    "*888*P"    "*88*" 8888"
## ^    "88888hx.+"     ^*888%     'Y"         'Y"       `"888*""      :""888":~"888"     `888*"     'Y"         'Y"         ""   'Y"
##        ^"**""          "%                                ""             "~'    "~        ""
##''')
##
##time.sleep(2)

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")


print('''Before getting started, I need to tell you some things about this game:
         1. This is a choice based game. Your choices matter and will affect the story;
         2. This game is still under devellopement and isn't finished (20% only of the story);
         3. Try to relax...;
         4. There are zombies in this game. You will need to outsmart them;
         5. Based on the choice you made, it will affect your sanity. If you are very sane, it will make assistant's trust you more;
         6. Insanity will result in no trust, BUT will affect your stats in a positive way;
         7. Sanity will also result in change of items: if you really are insane, then your items will be "Dark";
         8. If you are sane, your items will be "Light";
         9. Wackycks are the currency of the game, 1 WK = 1,000 $
         10.If you want to throw, there is a cooldown of 4 turns


                                           !NOW ENJOY!

      ''')

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")


time.sleep(0)
# Settings

username =  input("What shall be your name?")

while True:
    gender = input("What gender do you want your character to be? (remenber that you can only chose boy or girl...)")
    if gender == "boy" or gender == "Boy" or gender =="BOY" or gender == "girl" or gender == "Girl" or gender == "GIRL":
        print("\n")
        break
    elif gender == "e":
        player.inventory(gender)
        continue
    elif gender == "Hey god give me some of your powers!":
        player.health = 99999999999
        player.Melee_Damage = 99999999999
        player.stamina = 99999999999
        player.health = 99999999999
        player.cloth = 99999999999
        player.evasion = 99999999999
        player.mana = 99999999999
        player.race = "human"
        print("\n")
        print ("!!!______!!!Congrats on becoming a god!!!______!!!")
        print("\n")
        print(mana , stamina , Melee_Damage , cloth , evasion , health)
        continue
    else:
        print("Didn't I already say that you can only chose: Boy,BOY,boy or Girl,BOY,girl.")
        print("\n")
        continue

#  Monday 1 june 20XX----------Chapter 1


print("\n")

print('''Narrater: You are actually working at Appdey. You hate your job, but are unable to change because

      you are afraid of not getting enough money... The next bloodmooon will be this Tuesday 2 june 20XX.

      We are currently the Monday 1 june 20XX.''')

print("\n")

# Tuesday 2 june 20XX-----------Chapter 1
time.sleep(0)
print('''Conscience: I wake up in the middle of the night. I remember that i felt sleepy and fell on the ground

      asleep. I think it was something like 11 pm... I don't think I feel so great...I go to the bathroom to take

      medication...I open the door...''')

print ("\n")

time.sleep(0)

player.race()
race = player.race




print ("Then {n}, it shall be the {r}...".format(r = race , n = username))

while True:
    choice_1 = input("Would you like to see your stats?")
    if choice_1 == "Yes" or choice_1 == "yes" or choice_1 == "YES":
        print ("\n")
        print ('''Your health is {h}, your stamina is at {s}, your magic stamina is at {m}, your melee damage is currently at {d},

you have {c} of clothes and you are at {e} of evasion. Your sanity is {s} and you only have {w} wackycks...'''
               .format (h = player.health , st = player.stamina , m = player.mana , d = player.Melee_Damage , c = player.cloth , w = player.Wackycks , s = player.sanity , e = player.evasion))
        break

    elif choice_1 == "No" or choice_1 == "no" or choice_1 == "NO":
        print ("\n")
        print ("If you say so...")
        break


    else:
        print ("\n")
        print ('''Seriously ?!  Just chose between yes or no...''')
        print("\n")
        continue

time.sleep(0)

print(race)

if race == "Vampire" or race == 'Werewolf' or race == 'Mage' or race == 'Elf' or race == 'dev':

    print("\n")

    print('''Narrater: When you open the door ,you really don't feel great. Once you are in front of the pharmacie, you loose conscience.

          You transformed into a {r}. '''.format(r =race))

time.sleep(0)

if race == "Vampire" or race == 'Werewolf' or race == 'Mage' or race == 'Elf' or race == 'dev':

    print('''
          Conscience: (*wakes up*)...So that was that... why I didn't feel great was because I turned into a {r}. I will never be able

          to go out ever again.

          Narrater: After two more days in your home it is currently the 4 june 20XX. This is when you decide to go out... '''.format(r = race))

    print("\n")

time.sleep(0)
if race == "human":

    print("\n")

    print('''Narrater: When you open the door ,you really don't feel great. Once you are in front of the pharmacie, you loose conscience.

          You didn't felt great because you lost one of your eyes...''')
    print("\n")

if race == "human":

    time.sleep(0)

    print('''Conscience: So that was why... Why I didn't felt great. I lost an eye...Anyway.It's strange, i don't feel any pain...It's like I am in a video game...

    Narrater: After getting drunk for two days it is currently the 4 june 20XX. You got hungry and there is nothing in your fridge so you decide to go out...''')


print("\n")

#Thursday 4 June 20XX-----------Chapter 2
print('\n')
print("CHAPTER 2")
print('\n')
print('\n')
print('\n')

print("When you go out, you see a horde of zombies, what will you do?")


while True:

    choice_2 = input('''



                        (1)You decide to face them (-10 of sanity)
                        (2)You chose to come back to your house to pick weapons (+10 of sanity)
                        _______________

              ''')

    if choice_2 == "1":
        player.sanity-= 10


        print("\n")
        print("Oh. Wait. There is a window that popped-up on your left side... ")
        print("It might be a good idea to see what it is.")
        print("\n")
        print("You might want to take a weapon...")
        player.shop(player.Wackycks)
        player.zombie_fight()

        print("Let's go to the nearest deli. After all you didn't came out of your house for nothing...")
        break

#_______________________________________________________________________IF NOT FIGHTING AGAIsNT ZOMBIES_________________________________________________________________

    elif choice_2 == '2':

        player.sanity += 10

        print("\n")
        print("\n")
        print("\n")
        print("When you come back at your house to take a weapon, you encounter a tarantula!")
        print("\n")
        print("\n")
        choice3_A = input('''

                 (1)You stomp on it and kill it (+2 of sanity ----- +10 wackycks)
                 (2)You decide to raise it like you would do it if it were your son (-15 of sanity)
                 _______________


              ''')

        if choice3_A == "1":

            player.sanity += 2
            player.Wackycks += 10
            print("\n")
            print("\n")
            print("You get in your house...")
            print("\n")
            print("\n")
            print("You have remorse about that tarantula you killed ....... -12 of sanity")
            player.sanity -= 12

        elif choice3_A == "2":
            player.sanity -= 15
            print("\n")
            print("\n")
            print("You decided to raise a tarantula as your son. You now have a companion!!!")
            time.sleep(2)
            print("\n")
            print("")
            print("\n")
            print("Because you have someone to speak to that won't judge you, you feel happy ....... +10 of sanity")
            player.sanity += 10


        else:
            print("Please just say 1 or 2, thank you for your understanding!")
            continue

        print("You open the door of your house. After 2 hours, you gather everything you think is a weapon,")
        print("and 5 wackycks.")
        player.Wackycks += 5
        print("\n")
        print("\n")
        time.sleep(2)
        print("Wait! The items you have gathered went into, huhh... Nothing?")
        print("Hey look! a window seem to have opened!")
        print("Conscience: Hmmm. Seems like that of a computer...")
        time.sleep(3)
        print("Narrator: Because this is your first time opening 'Da Shop', it's free")
        print("oh yeah. And because I am kind, I'll give 10 wackycks")
        time.sleep(2)
        player.Wackycks += 10
        player.shop(player.Wackycks)
        print("\n")
        print("Alright! Now let's go to the nearest deli! After all you really need to eat...")
        break

#___________________________________________________AFTER GOING THROUGH THE ZOMBIES OR SEARCHING YOUR HOUSE - CHAPTER 3________________________________________________


print('\n')
print("CHAPTER 3")
print('\n')
print('\n')
print('\n')

print("Hi!Think fast!")
time.sleep(1)
start = timer()
int(input("1 or 2"))
end = timer()
print(end - start)

if end - start < 1.5:
	print("You won 10 wackycks!")
	player.Wackycks += 10
else:
	print("You lost 10 of your wackycks...")
	player.Wackycks -= 10

print("Seems we arrived to destination.")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
delay_print("Entering...")
time.sleep(2)

print("\nWhen you enter the deli you hear a groan coming from the second floor.")
print("\n")
deli_1 = input('''

                 (1)Do you go to see if it really was a zombie that caused it? (+10 sanity)
                 (2)Or do you want to just explore the first floor? (-15 of sanity)
                 _______________

              ''')