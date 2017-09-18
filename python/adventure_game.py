import random


class Creature:
    def __init__(self, hp, name):
        self.hp = hp
        self.maxhp = hp
        self.dead = False
        self.name = name
        self.weapon = None

    def __str__(self):
        return "{}".format(self.name)


class Weapon:
    def __init__(self, name, ap):
        self.name = name
        self.ap = int(ap)

class Game:
    def __init__(self):
        print("")
        self.hero_name = input("What's our Hero's name?: ")
        print("")

        difficulty = str(input("Press 1 for a heroic challenge, 2 for a stringent one, and 3 for an easy-peasy game."))
        diff_dict = {"1": 50, "2": 70, "3": 100}
        self.hero = Creature(diff_dict[difficulty], self.hero_name)
        weapon_choice = str(input("What weapon do you want for your hero?: "))
        self.hero.weapon = Weapon(weapon_choice, random.randrange(20,30))

        enemy_list = ["Troll", "Tax Man", "Merman", "Alien"]
        self.enemy = Creature(random.randrange(40, 80, 5), random.choice(enemy_list))
        self.enemy.weapon = Weapon("wooden sword", 20)

    def battle(self):
        print("")
        print("You've engaged the enemy!!! ")
        attack_var = int(random.randrange(1, 10))
        # print("attack var is {}".format(attack_var))
        if attack_var <= 9:
            self.hero.hp -= self.enemy.weapon.ap
            self.dead_check()
            print("{} was attacked for {} HP.".format(self.hero.name, self.enemy.weapon.ap))
        if attack_var >= 1:
            self.enemy.hp -= self.hero.weapon.ap
            self.dead_check()
            print("{} was attacked for {} HP.".format(self.enemy.name, self.hero.weapon.ap))
        else:
            print("Double miss!")

    def dead_check(self):
        if self.hero.hp <= 0:
            self.hero.dead = True
        elif self.enemy.hp <= 0:
            self.enemy.dead = True

    def heal(self):
        potion_val = random.randrange(10, 30, 5)
        self.hero.hp += potion_val
        print("You've used a potion for {} HP!  {}'s HP is now {}. ".format(potion_val, self.hero.name, self.hero.hp))

    def sneak_attack(self):
        sneak_var = int(random.randrange(1,100))
        print("sneak attack {}".format(sneak_var))
        if sneak_var < 8:
            self.hero.hp -= (self.enemy.weapon.ap - 5)
            print("A sneak attack!!! {} was attacked for {} HP.".format(self.hero.name, self.enemy.weapon.ap))

    def game_menu(self):
        while self.hero.dead == False and self.enemy.dead == False:
            print("")
            print("{}'s HP is {}.".format(self.hero.name, self.hero.hp))
            print("{}'s HP is {}.".format(self.enemy.name, self.enemy.hp))
            choice = str(input("Press 1 to attack with your {}, 2 to heal.".format(self.hero.weapon.name)))
            self.sneak_attack()
            if choice == '1':
                self.battle()
            if choice == '2':
                self.heal()
        if self.hero.dead == True:
            print("")
            print("The evil {} killed our hero {}!!! ".format(self.enemy.name, self.hero.name))
        else:
            print("")
            print("Our hero {} destroyed the enemy!!! ".format(self.hero.name))




main = Game()
main.game_menu()



