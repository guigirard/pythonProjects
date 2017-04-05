from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random



# Create black magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 45, 1400, "black")

# Create white magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")

# Create some item
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("Mega Elixir", "elixir", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 2},
                {"item": grenade, "quantity": 5}]

enemy_spells = [fire, thunder, meteor, curaga]

# Instantiate People
player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick :", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)
players = [player1, player2, player3]
defeated_players = 0
number_players = len(players)

enemy1 = Person("Imp    ", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Magus", 18200, 701, 525, 25, enemy_spells, [])
enemy3 = Person("Imp    ", 1250, 130, 560, 325, enemy_spells, [])
enemies = [enemy1, enemy2, enemy3]
defeated_enemies = 0
number_enemies = len(enemies)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "ENEMIES ARE ATTACKING!" + bcolors.ENDC)

# Starts the loop for combat actions
while running:
    # Prints the initial text for the battle
    print("========================================")

    print("\n\n")
    print("NAME")

    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    # Prompt the player to select an action for the battle for each character
    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        # If player selects to attack, this flow will apply to the combat
        if index == 0:
            dmg = player.get_generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(player.name + " attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died")
                defeated_enemies += 1
                del enemies[enemy]
        # If player selects to use magic, this flow will apply to the combat
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            # Allows the player to revert choice by typing 0
            if magic_choice == -1:
                continue

            # Starts the logic in case a player chooses to
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            # Checks if player has enough MP to cast the spell
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            # Introduces the difference between damage and healing
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                      "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died")
                defeated_enemies += 1
                del enemies[enemy]

        # If player selects an item, this flow will apply to the combat
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == - 1:
                continue

            item = player.items[item_choice]["item"]

            # Counts remaining items and return error if selected item is depleted
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            # Subtracts 1 to the quantity of items owned
            player.items[item_choice]["quantity"] -= 1

            # Manages healing points with potions
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            # Manages restoration with elixirs
            elif item.type == "elixir":
                if item.name == "Mega Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            # Manages damage inflicted with harmful items
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop),
                      "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died")
                    defeated_enemies += 1
                    del enemies[enemy]

    # Check if battle is over
    # Check if player won
    if defeated_enemies == number_enemies:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False

    print("\n")
    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Choose attack
            target = random.randrange(0, len(players))
            enemy_dmg = enemies[0].get_generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "")
                  + " for", enemy_dmg)

            if players[target].get_hp() == 0:
                print(players[target].name.replace(" ", "") + " has died")
                defeated_players += 1
                del players[target]

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + spell.name + " heals " + enemy.name + " for", str(magic_dmg),
                      "HP" + bcolors.ENDC)
            elif spell.type == "black":
                target = random.randrange(0, len(players))

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died")
                    defeated_players += 1
                    del players[target]

                players[target].take_damage(magic_dmg)
                print(bcolors.FAIL + spell.name + " deals", str(magic_dmg),
                      "points of damage to " + players[target].name.replace(" ", "") + bcolors.ENDC)

    # Check if enemies won
    if defeated_players == number_players:
        print(bcolors.FAIL + "Your enemies has defeated you!" + bcolors.ENDC)
        running = False
