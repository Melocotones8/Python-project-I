from time import sleep

def user_action():
    user_choice = None
    while user_choice == None:
        try:
            user_choice = int(input("What would you like to do? "))   
        except ValueError:
            print("You have to choose a number")
    return user_choice

def user_input():
    user_choice = None
    while user_choice == None or len(user_choice) > 20 or len(user_choice) == 0:
        user_choice = input("")
        if len(user_choice) <= 20 and len(user_choice) > 0:
            return user_choice
        elif len(user_choice) == 0:
            print("This field cannot be left empty.")
        else:
            print("The name can't be longer than 20 characters")
    return user_choice

def main_menu():
    print('*' * 40)
    print("Welcome in the world of 'Swords and Boots'")
    print('-' * 40)
    sleep(0.5)
    print("""
1. Create new game
2. Load game
3. Show Author
4. Exit game""")

def game_menu():

    print("""
1. Fight vs BOSS
2. Training vs mobs
3. Show your stats
4. Save game
5. Quit to main menu
""")

def warrior_fight_menu():
    print("1.Attack  2.Move forward  3.Quit")

def mage_fight_menu(mana):
    print("1.Attack  2.Move forward  3.Spells (left mana: {})  4.Quit".format(mana))
    user_choice = user_action()
    if user_choice == 3:
        print("""
1. Fireball      --    take 10 demage   --  cost 30 points of mana
2. Cure          --     heal 20 HP      --  cost 40 points of mana
3. Wind push     --  set distance at 3  --  cost 30 points of mana
4. Regeneration  --  get 15 points of extra mana (without limit)""")
    
    return user_choice

def end_game():

    print('*' * 30)
    print("""   !!!MINOTAUR IS GONE!!!
          
The society is very grateful for the help. You have became honorary citizen of this area.
You can come back here whenever you want.
.
.
.
Than you for spending time with demo of my game. It's a first version, which i have created to show my programming skills. See you later.""")
    sleep(5)
    