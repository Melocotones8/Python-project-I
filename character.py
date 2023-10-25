import random

from menus_input import user_action

class Character:

    def __init__(self, name, gender, hp=0, attack=0, defense=0, level=1, hero_class=None):
        self.name = name
        self.gender = gender
        self.hero_class = hero_class
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.level = level

    def getInfo(self):
        print("My name is {} and my gender is {}.".format(self.name, self.gender))
        print("My stats:") 
        print("HP = {}, attack = {}, defense = {}.".format(self.hp, self.attack, self.defense))

    def message(self):
        
        print("""Welcome in the Monstrom world. 
This is a beautiful and peaceful area where most people work in agriculture and tourism. 
This tranquility has been disrupted by the appearance of the Minotaur which regularly attacks farms and devours livestock. 
The tracking teams have already identified his hideout, but someone is needed to defeat him.
You have been chosen for this task. Good luck.""")

    def level_up(self):
        if self.level >= 10:
            print("You have maximum level of 10")
            pass
        else:
            self.level += 1
            print("LEVEL UP")

    def show_stats(self):
        stats = "HP = {}, attack = {}, defense = {}, level = {}".format(self.hp, self.attack, self.defense, self.level)
        return stats
    
    def stats_dic(self):
        stats_dictionary = {"Class": self.hero_class, "HP": self.hp, "attack": self.attack, "defense": self.defense}
        return stats_dictionary
    
    def hero_save(self):
        saving_stats = [self.name, self.gender, self.level, self.hero_class, self.hp, self.attack, self.defense]
        return(saving_stats)
    

class Warrior(Character):

    def __init__(self, name, gender, hp=120, attack=6, defense=6, counter=50, level=1, hero_class="Warrior"):
        super().__init__(name, gender, hp, attack, defense, level, hero_class)
        self.ability = counter
    
    def getInfo(self):
        super().getInfo() 
        print("I'm a {} and my special ability is counterattack at {}% level".format(self.hero_class, self.ability))
    
    def message(self):
         super().message()

    def level_up(self):
        if self.level < 10:
            self.hp += 10
            self.attack += 2
            self.defense += 2
            self.ability += 5
        super().level_up()
    
    def show_stats(self):
        heroe_stats = ", counterattack = {}%".format(self.ability)
        print(super().show_stats() + heroe_stats)

    def stats_dic(self):
        warrior_stats = super().stats_dic()
        warrior_stats.update({"special": self.ability})
        return warrior_stats
    
    def hit(self):
        return self.attack
    
    @staticmethod
    def counter(chance, hAttack, eDefense):
        counter = random.choices(range(1,3), [chance, 100 - chance])[0]
        if counter == 1:
            counterAttack = hAttack - eDefense 
            if counterAttack <= 0: counterAttack = 1
            print("Counterattack! You takes {} demage".format(counterAttack))
        else:
            counterAttack = 0
            
        return counterAttack
    
    def hero_save(self):
        return super().hero_save().append(self.ability)
        

class Mage(Character):

    def __init__(self, name, gender, hp=80, attack=8, defense=4, mana=100, level=1, hero_class="Mage"):
            super().__init__(name, gender, hp, attack, defense, level, hero_class)
            self.ability = mana
    
    def getInfo(self):
        super().getInfo() 
        print("I'm a {} and my special ability is magic. I have {} points of mana".format(self.hero_class, self.ability))

    def message(self):
        super().message()

    def level_up(self):
        if self.level < 10:
            self.hp += 10
            self.attack += 2
            self.defense += 1
            self.ability += 20
        super().level_up()

    def show_stats(self):
        heroe_stats = ", mana = {}".format(self.ability)
        print(super().show_stats() + heroe_stats)

    def stats_dic(self):
        mage_stats = super().stats_dic()
        mage_stats.update({"special": self.ability})
        return mage_stats
    
    def hit(self):
        return self.attack
    
    @staticmethod
    def spell(mana, heroHP, maxHP):
        spell_choice = user_action()
        print('-' * 30)
        if spell_choice == 1:
            if mana >= 30:
                print("You takes 10 demage")
            else:
                print("You don't have enough mana")
                spell_choice = 0
        elif spell_choice == 2:
            if mana >= 40:
                if heroHP < maxHP:
                    if maxHP - heroHP >=20:
                        print("You cures 20 HP")
                    else:
                        print("You cures {} HP".format((maxHP - heroHP)))
                else:
                    print("You already have full HP")
                    spell_choice = 0
            else:
                print("You don't have enough mana")
                spell_choice = 0
        elif spell_choice == 3:
            if mana >= 10:
                print("You pushes enemy at distance of 3")
            else:
                print("You don't have enough mana")
                spell_choice = 0
        elif spell_choice == 4:
            print("You gains 20 points of mana")
        else:
            print("I don't know this spell")
            spell_choice = 0

        return spell_choice
    
    def hero_save(self):
        return super().hero_save().append(self.ability)


class Rogue(Character):

    def __init__(self, name, gender, hp=80, attack=8, defense=5, level=1, hero_class="Rogue"):
            super().__init__(name, gender, hp, attack, defense, level, hero_class)
            self.ability = 'NULL'
    
    def getInfo(self):
        super().getInfo() 
        print("I'm a {} and i can use distance weapons which decrease enemy defense".format(self.hero_class))
    
    def message(self):
         super().message()
    
    def level_up(self):
        if self.level < 10:
            self.hp += 15
            self.attack += 2
            self.defense += 1
        super().level_up()

    def show_stats(self):
        print(super().show_stats())

    def stats_dic(self):
        rogue_stats = super().stats_dic()
        rogue_stats.update({"special": self.ability})
        return rogue_stats
    
    def hit(self, distance):
        if distance == 0:
            return self.attack
        else:
            print("Distance shot which damaged the opponent's defense by 1")
            return self.attack
        
    def hero_save(self):
        return super().hero_save().append('NULL')
