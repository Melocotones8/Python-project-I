from functools import wraps
from time import sleep

from menus_input import user_action, warrior_fight_menu, mage_fight_menu

def fight_stats(func):
    @wraps(func)
    def wrapper(hero, enemy):
        distance = 3
        heroStats = hero.stats_dic()
        heroHP = heroStats["HP"]
        maxHP = heroStats["HP"]
        heroAttack = heroStats["attack"]
        heroDefense = heroStats["defense"]
        heroSpecialAbility = heroStats["special"]

        enemyStats = enemy.stats_dic()
        enemyHP = enemyStats["HP"]
        enemyDefense = enemyStats["defense"]
        
        print('-' * 30)
        enemy.getinfo()

        result = func(distance, heroHP, maxHP, heroAttack, heroDefense, heroSpecialAbility, enemyStats, enemyHP, enemyDefense, hero, enemy)

        return result
        
    return wrapper
    
def game_over(hero, heroHP, enemyHP):

    sleep(0.5)
    if heroHP <= 0:
        print("It's over. Try again")
        sleep(0.5)
        print(".")
        sleep(0.5)
        print(".")
        sleep(0.5)
        print("You are recovered")
        result = 'lose'
    elif enemyHP <= 0:
        print("Excellent! You have killed an enemy.")
        sleep(0.5)
        hero.level_up()
        sleep(1)
        hero.show_stats()
        result = 'win'
    else:
        result = 'NULL'
    print('-' * 30)

    return result
    
def fight_distance(distance, h_hp, e_hp):

    if distance == 3:
        print("HP:{}      YOU----------||----------||----------ENEMY      HP:{}".format(h_hp, e_hp))
    elif distance == 2:
        print("HP:{}      YOU----------||----------ENEMY      HP:{}".format(h_hp, e_hp))
    elif distance == 1:
        print("HP:{}      YOU----------ENEMY      HP:{}".format(h_hp, e_hp))
    elif distance == 0:
        print("HP:{}      YOU-ENEMY      HP:{}".format(h_hp, e_hp))

@fight_stats
def warrior_fight(distance, heroHP, maxHP, heroAttack, heroDefense, heroSpecialAbility, enemyStats, enemyHP, enemyDefense, hero, enemy):

    while heroHP > 0 and enemyHP > 0:
        
        print("^" * 30)
        fight_distance(distance, heroHP, enemyHP)
        warrior_fight_menu()
        user_choice = user_action()
        print('-' * 30)
        
        if user_choice == 1:
            if distance == 0:
                hit = hero.hit() - enemyDefense
                if hit > 0: 
                    enemyHP -= hit
                    print("You takes {} demage".format(hit))
                else:
                    enemyDefense -= 1
                    print("Enemy's defense decrease by 1 point")
            elif distance > 0:
                print("You are too far")
        elif user_choice == 2:
            if distance > 0:
                distance -= 1
            else:
                print("You are too close")
        elif user_choice == 3:
            print("Bye")
            break
        else:
            print("I don't know what to do")

        if user_choice in range (1, 3) and enemyHP > 0:
            if distance > 0:
                distance -= 1
                print("Enemy is moving")
            else:
                hit = enemy.enemy_hit() - heroDefense
                if hit > 0: 
                    heroHP -= hit
                    print("Enemy takes {} demage".format(hit))
                else:
                    heroDefense -= 1
                    print("Your defence decrease by 1 point")
                counter = hero.counter(heroSpecialAbility, heroAttack, enemyDefense)
                if counter > 0: enemyHP -= counter 

    result = game_over(hero, heroHP, enemyHP) 

    return result 

@fight_stats
def mage_fight(distance, heroHP, maxHP, heroAttack, heroDefense, heroSpecialAbility, enemyStats, enemyHP, enemyDefense, hero, enemy):

    while heroHP > 0 and enemyHP > 0:
        
        print("^" * 30)
        fight_distance(distance, heroHP, enemyHP)
        user_choice = mage_fight_menu(heroSpecialAbility)
        print('-' * 30)

        if user_choice == 1:
            if distance == 0:
                hit = hero.hit() - enemyDefense
                if hit > 0: 
                    enemyHP -= hit
                    print("You takes {} demage".format(hit))
                else:
                    enemyDefense -= 1
                    print("Enemy's defense decrease by 1 point")
            elif distance > 0:
                print("You are too far")
        elif user_choice == 2:
            if distance > 0:
                distance -= 1
            else:
                print("You are too close")
        elif user_choice == 3:
            spell = hero.spell(heroSpecialAbility, heroHP, maxHP)
            if spell == 1:
                enemyHP -= 10
                heroSpecialAbility -= 30
            elif spell == 2:
                heroHP += 20
                if heroHP > maxHP: heroHP = maxHP
                heroSpecialAbility -= 40
            elif spell == 3:
                distance = 3
                heroSpecialAbility -= 30
            elif spell == 4:
                heroSpecialAbility += 15
            elif spell == 0:
                user_choice = 0
        elif user_choice == 4:
            print("Bye")
            break
        else:
            print("I don't know what to do")

        if user_choice in range (1, 4) and enemyHP > 0:
            if distance > 0:
                distance -= 1
                print("Enemy is moving")
            else:
                hit = enemy.enemy_hit() - heroDefense
                if hit > 0: 
                    heroHP -= hit
                    print("Enemy takes {} demage".format(hit))
                else:
                    heroDefense -= 1
                    print("Your defence decrease by 1 point")

    result = game_over(hero, heroHP, enemyHP) 

    return result

@fight_stats
def rogue_fight(distance, heroHP, maxHP, heroAttack, heroDefense, heroSpecialAbility, enemyStats, enemyHP, enemyDefense, hero, enemy):

    while heroHP > 0 and enemyHP > 0:
        
        print("^" * 30)
        fight_distance(distance, heroHP, enemyHP)
        warrior_fight_menu()
        user_choice = user_action()
        print('-' * 30)
        
        if user_choice == 1:
            if distance == 0:
                hit = hero.hit(distance) - enemyDefense
                if hit > 0: 
                    enemyHP -= hit
                    print("You takes {} demage".format(hit))
                else:
                    enemyDefense -= 1
                    print("Enemy's defense decrease by 1 point")
            elif distance > 0:
                hit = hero.hit(distance) - enemyDefense
                if hit > 0: enemyHP -= hit
                enemyDefense -= 1
                print("You took {} demage ".format(hit))
        elif user_choice == 2:
            if distance > 0:
                distance -= 1
            else:
                print("You are too close")
        elif user_choice == 3:
            print("Bye")
            break
        else:
            print("I don't know what to do")

        if user_choice in range (1, 3) and enemyHP > 0:
            if distance > 0:
                distance -= 1
                print("Enemy is moving")
            else:
                hit = enemy.enemy_hit() - heroDefense
                if hit > 0: 
                    heroHP -= hit
                    print("Enemy takes {} demage".format(hit))
                else:
                    heroDefense -= 1
                    print("Your defence decrease by 1 point")

    result = game_over(hero, heroHP, enemyHP) 

    return result 
