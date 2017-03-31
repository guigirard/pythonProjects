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

# Instantiate People
player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick :", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)
enemy = Person("Magus", 10000, 701, 525, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

# Starts the loop for combat actions
while running:
    # Prints the initial text for the battle
    print("========================================")

    print("\n\n")
    print("NAME")

    for player in players:
        player.get_stats()

    print("\n")

    enemy.get_enemy_stats()

    # Prompt the player to select an action for the battle for each character
    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        # If player selects to attack, this flow will apply to the combat
        if index == 0:
            dmg = player.get_generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.")
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
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        # If player selects an item, this flow will apply to the combat
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == - 1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "Mega Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = random.randrange(0, 2)
    enemy_dmg = enemy.get_generate_damage()
    players[enemy_choice].take_damage(enemy_dmg)
    print("Enemy attacks", players[enemy_choice].name, "for", enemy_dmg)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False
