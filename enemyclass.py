import random
import time


class Enemy():

    ehealth = 0
    emelee_damage = 0
    ecloth = 0
    emana = 0
    rider_attack = []





    #comabatant = zombie
    def __init__(self,combatant):
        self.combatant = combatant



    def Combatant_Settings(self):


        if self.combatant == "weak zombie":
            self.ehealth = 75
            self.emelee_damage = 25
            # have anotger method with colth picker
            self.ecloth = Enemy.ecloth_picker(1)


        if self.combatant == "normal zombie":

           self.ehealth = 100
           self.emelee_damage = 30
           self.ecloth = Enemy.ecloth_picker(2)

        if self.combatant == "enhenced zombie":
           self.ehealth = 150
           self.emelee_damage = 50
           self.ecloth = Enemy.ecloth_picker(3)


        if self.combatant == "riders scout":

               rhealth = 75
               rmelee_damage = 25
               rcloth = 10
               rider_attack = ["sniping" , "kicking" , "stabing in the back"]

        if self.combatant == "riders muscleman":

               rhealth = 100
               rmelee_damage = 30
               rcloth = 10
               rider_attack = ["thrusting his knife" , "high kicking" , "shooting his handgun"]

        if self.combatant == "riders biker":

               rhealth = 150
               rmelee_damage = 40
               rcloth = 30
               rider_attack = ["shooting his handgun" , "confusing" , "riding over you"],#need 50 of evasion to escape the "riding over you"

        if self.combatant == "riders right handman":

               rhealth = 200
               rmelee_damage = 60
               rcloth = 50
               rider_attack = ["shooting his rifle" , "throwing a grenade" , "calling for back-up"]


        if self.combatant == "riders lesser Mage":

               rhealth = 30
               rmelee_damage = 10
               rcloth = 5
               rmana = 30
               rider_attack = ["firing a little fire ball" , "throwing you away" , "firing a litle nuke"]



    def ecloth_picker(self,key):

        if key == 1:
            return random.randint(1,35)
        if key == 2:
            return random.randint(10,45)
        if key == 3 :
            return random.randint(30,90)


    def e_hit_percentage(self):
     return random.randint(0,100)


