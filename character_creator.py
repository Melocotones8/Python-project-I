from character import Warrior, Mage, Rogue
from menus_input import user_input

def character_creator():

    print("Enter your character's name:")
    name = user_input()
    print("Enter your gender:")
    gender = user_input()
    hero = None
    
    while hero == None:
        character_class = input("You are Warrior, Mage(recomended) or Rogue?: ").capitalize()
        if character_class == "Warrior":
            hero = Warrior(name, gender)
        elif character_class == "Mage":
            hero = Mage(name, gender)
        elif character_class == "Rogue":
            hero = Rogue(name, gender)
        else:
            print("There is no such a class")

    hero.getInfo()
    hero.message()
    
    return hero

def loaded_character(save):
    
    try:
        name = save[0]
        gender = save[1]
        hero_class = save[2]
        hp = save[3]
        attack = save[4]
        defense = save[5]
        level = save[6]
        ability = save[7]

        if hero_class == 'Warrior':
            loaded_hero = Warrior(name, gender, hp, attack, defense, ability, level)
        elif hero_class == 'Mage':
            loaded_hero = Mage(name, gender, hp, attack, defense, ability, level)
        elif hero_class == 'Rogue':
            loaded_hero = Rogue(name, gender, hp, attack, defense, level)
        
        print("-" * 30)
        print("Game succesfully loaded")
        print("-" * 30)
        loaded_hero.getInfo()

        return loaded_hero 
    
    except:
        return 'error'
