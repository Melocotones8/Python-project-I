from menus_input import game_menu, user_action, end_game, main_menu
from character_creator import character_creator, loaded_character
from enemies import mob_draw, mob_list, Minotaur
from fight import warrior_fight, mage_fight, rogue_fight
from saving import save_game, saves, load_game

def main_descopt(user_choice):
    while user_choice != 4:

        if user_choice == 1:
            hero = character_creator()
            print('-' * 30)
            game_descopt(hero) 
            main_menu()
            user_choice = user_action()
        elif user_choice == 2:
            print('-' * 30)
            positions = saves()
            if positions == 0:
                print("There is no saves")
            else:
                save = load_game()
                hero = loaded_character(save)
                if hero == 'error':
                    print("Wrong save name")
                    print('-' * 30)
                else:
                    game_descopt(hero)
            main_menu()
            user_choice = user_action()
        elif user_choice == 3:
            print('-' * 30)
            print("The author of this game is Bartosz Krupa, a future Python developer.")
            print('-' * 30)
            main_menu()
            user_choice = user_action()
        else:
            print("Unknown action")
            user_choice = user_action()

def game_descopt(hero):

    game_menu()
    user_choice = user_action()

    while user_choice != 5:
            
        if user_choice == 1:
            if hero.hero_class == "Warrior":
                result = warrior_fight(hero, Minotaur())
                if result == 'win':
                    end_game()
                    break
                else:
                    game_menu()
                    user_choice = user_action()
            elif hero.hero_class == "Mage":
                result = mage_fight(hero, Minotaur())
                if result == 'win':
                    end_game()
                    break
                else:
                    game_menu()
                    user_choice = user_action()
            elif hero.hero_class == "Rogue":
                result = rogue_fight(hero, Minotaur())
                if result == 'win':
                    end_game()
                    break
                else:
                    game_menu()
                    user_choice = user_action()
        elif user_choice == 2:
            if hero.hero_class == "Warrior":
                warrior_fight(hero, mob_draw(mob_list))
            elif hero.hero_class == "Mage":
                mage_fight(hero, mob_draw(mob_list))
            elif hero.hero_class == "Rogue":
                rogue_fight(hero, mob_draw(mob_list))
            game_menu()
            user_choice = user_action()
        elif user_choice == 3:
            hero.show_stats()
            game_menu()
            user_choice = user_action()
        elif user_choice == 4:
            saves()
            save_game(hero.name, hero.gender, hero.level, hero.hero_class, hero.hp, hero.attack, hero.defense, hero.ability)
            game_menu()
            user_choice = user_action()
        else:
            print("Unknown action")
            user_choice = user_action()
