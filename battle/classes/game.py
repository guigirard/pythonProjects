import random


<<<<<<< HEAD
class BColors:
=======
class bcolors:
>>>>>>> origin/master
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
<<<<<<< HEAD
    def __init__(self, hp, mp, atk, df, magic):
=======
    def __init__(self, name, hp, mp, atk, df, magic, items):
>>>>>>> origin/master
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
<<<<<<< HEAD
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

=======
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Items"]
        self.name = name

    def get_generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

>>>>>>> origin/master
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

<<<<<<< HEAD
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
=======
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
>>>>>>> origin/master
        return self.maxhp

    def get_mp(self):
        return self.mp

<<<<<<< HEAD
    def get_max_mp(self):
=======
    def get_maxmp(self):
>>>>>>> origin/master
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

<<<<<<< HEAD
    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(BColors.OKBLUE + BColors.BOLD + "Actions" + BColors.ENDC)
        for item in self.actions:
            print(str(i) + ":", item)
=======
    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    " + "ACTIONS:" + bcolors.ENDC)
        for item in self.action:
            print("        " + str(i) + ".", item)
>>>>>>> origin/master
            i += 1

    def choose_magic(self):
        i = 1
<<<<<<< HEAD
        print(BColors.OKBLUE + BColors.BOLD + "Magic" + BColors.ENDC)
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1
=======
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    " + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    " + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name + ":", item["item"].description,
                  "(x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    " + "TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target: ")) -1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += '\u2588'
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        # Producing the dynamic rendering of HP for enemy
        enemy_hp_string = str(self.hp) + "/" + str(self.maxhp)
        enemy_current_hp = ""

        if len(enemy_hp_string) < len(str(self.maxhp) + str(self.maxhp) + "/"):
            decreased = len(str(self.maxhp) + str(self.maxhp) + "/") - len(enemy_hp_string)

            while decreased > 0:
                enemy_current_hp += " "
                decreased -= 1

            enemy_current_hp += enemy_hp_string
        else:
            enemy_current_hp = enemy_hp_string

        print("                         _________________________________________________________________________"
              "_____")
        print(bcolors.BOLD + self.name + "    " + "HP: " +
              enemy_current_hp + "|" + bcolors.FAIL + hp_bar + bcolors.ENDC)

    # Defining points bars starting points
    def get_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self.hp / self.maxhp) * 100 / 4
        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10

        # Making bars dynamic to reflect progress in HP and MP
        while hp_bar_ticks > 0:
            hp_bar += '\u2588'
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += '\u2588'
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        # Producing the dynamic rendering of HP
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < len(str(self.maxhp) + str(self.maxhp) + "/"):
            decreased = len(str(self.maxhp) + str(self.maxhp) + "/") - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        # Producing the dynamic rendering of MP
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < len(str(self.maxmp) + str(self.maxmp) + "/"):
            decreased_mp = len(str(self.maxmp) + str(self.maxmp) + "/") - len(mp_string)

            while decreased_mp > 0:
                current_mp += " "
                decreased_mp -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

            # Printing the results of combats on HP and MP
        print("                        _______________________________________")
        print(bcolors.BOLD + self.name + "    " + "HP: " +
              current_hp + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC +
              "\n                        " + "________________" + "\n" + "          " + "MP:   " +
              current_mp + "|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC)

    def choose_enemy_spell(self):
        if self.hp / self.maxhp * 100 > 50:
            magic_choice = random.randrange(0, (len(self.magic) - 1))
            spell = self.magic[magic_choice]
            magic_dmg = spell.generate_damage()
        else:
            magic_choice = random.randrange(0, len(self.magic))
            spell = self.magic[magic_choice]
            magic_dmg = spell.generate_damage()

        if self.mp < spell.cost:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
>>>>>>> origin/master
