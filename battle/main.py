from classes.game import Person, BColors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 60, 34, magic)

running = True
i = 0

print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACKS" + BColors.ENDC)

while running:
    print("=============================================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()
        if cost > current_mp:
            print(BColors.FAIL + "\nNot enough MP\n" + BColors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(BColors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + BColors.ENDC)

    enemy_choices = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("----------------------------------------------")
    print("Enemy HP:", BColors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + BColors.ENDC)
    print("Your HP:", BColors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + BColors.ENDC)
    print("Your MP:", BColors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + BColors.ENDC)

    if enemy.get_hp() == 0:
        print(BColors.OKGREEN + "You win!" + BColors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(BColors.FAIL + "Your enemy has defeated you!" + BColors.ENDC)
