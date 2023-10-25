import random

mob_list = [("Skeleton", 70, 9, 2, 70), ("Golem", 150, 4, 6, 30), ("Thief", 120, 6, 4, 50)]


class Enemy():

    def __init__(self, name, hp, attack, defense, critical):
        
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.critical = critical

    def getinfo(self):
        print("It's a {}, his stats: hp = {}, attack = {}, defense = {} and critical hit chance = {}%".format(self.name, self.hp, self.attack, self.defense, self.critical))
        
    def enemy_hit(self):
        hit = self.attack
        chance = [1, 2]
        result = random.choices(chance, [self.critical, 100 - self.critical])[0]
        if result == 1:
            hit = self.attack * 1.5
        return hit
    
    def stats_dic(self):
        stats_dictionary = {"HP": self.hp, "attack": self.attack, "defense": self.defense, "critical": self.critical}
        return stats_dictionary


class Minotaur(Enemy):
    
    def __init__(self, name="Minotaur", hp=200, attack=10, defense=5, critical=70):
        super().__init__(name, hp, attack, defense, critical)

    def getinfo(self):
        return super().getinfo()

    
    def enemy_hit(self):
        hit = super().enemy_hit()
        if hit > self.attack:
            print("Minotaur gets angry. His attack is improving")
            self.attack += 1
        return hit
    
    def stats_dic(self):
        return super().stats_dic()


def mob_draw(mob_list):
    enemy = random.choice(mob_list)
    oponent = Enemy(enemy[0], enemy[1], enemy[2], enemy[3], enemy[4])
    return oponent
