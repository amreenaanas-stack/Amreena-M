import random



print("================================")
print(" LEGENDS OF THE FORGOTTEN REALM")
print("================================")


name = input("Enter your name: ")


print("\nChoose your class")
print("1. Warrior")
print("2. Mage")
print("3. Archer")
print("4. Assassin")

choice = input("Enter choice: ")

if choice == "1":
    player_class = "Warrior"
    hp = 150
    attack = 30
    defense = 20

elif choice == "2":
    player_class = "Mage"
    hp = 100
    attack = 40
    defense = 10

elif choice == "3":
    player_class = "Archer"
    hp = 120
    attack = 35
    defense = 15

else:
    player_class = "Assassin"
    hp = 90
    attack = 45
    defense = 8


max_hp = hp
level = 1
gold = 100
potions = 3
enemies_defeated = 0


print("\nWelcome", name)
print("Class:", player_class)
print("Level:", level)

while hp > 0 and level <= 10:

    enemies = ["Goblin", "Wolf", "Zombie", "Skeleton"]
    enemy = random.choice(enemies)
    enemy_hp = random.randint(40, 70)
    enemy_attack = random.randint(10, 20)

    print("\n==============================")
    print("Enemy:", enemy)
    print("Enemy HP:", enemy_hp)
    print("==============================")


    while enemy_hp > 0 and hp > 0:

        print("\nYour HP:", hp)
        print("Enemy HP:", enemy_hp)

        print("\n1. Attack")
        print("2. Heal")
        print("3. Defend")
        print("4. Run")

        action = input("Choose: ")

        if action == "1":
            damage = random.randint(
                attack - 5,
                attack + 5
            )

            if random.randint(1, 10) == 1:
                damage = damage * 2
                print("CRITICAL HIT!")
            enemy_hp = enemy_hp - damage
            print("You dealt", damage, "damage.")


        
        elif action == "2":

            if potions > 0:

                hp = hp + 30

                if hp > max_hp:
                    hp = max_hp

                potions = potions - 1

                print("You used a potion.")
                print("HP:", hp)

            else:

                print("No potions left!")


        
        elif action == "3":

            damage = enemy_attack // 2

            hp = hp - damage

            print("You defended!")
            print("Enemy dealt", damage, "damage.")


        
        elif action == "4":

            print("You ran away!")
            break


        
        else:

            print("Invalid choice!")
            continue


        
        if enemy_hp > 0:

            hp = hp - enemy_attack

            print(
                enemy,
                "attacked you for",
                enemy_attack,
                "damage."
            )

    if hp <= 0:

        print("\n================")
        print("GAME OVER")
        print("================")

        break


    
    if enemy_hp <= 0:

        print("\nYou defeated", enemy)

        enemies_defeated = enemies_defeated + 1

        gold = gold + 50

        print("You got 50 gold.")

        
        level = level + 1

        print("LEVEL UP!")
        print("Your level is:", level)

        hp = max_hp

        attack = attack + 5
        defense = defense + 2

        print("Attack increased!")
        print("Defense increased!")




if level > 10:

    print("\n================================")
    print("           VICTORY!")
    print("================================")

    print("Congratulations", name)
    print("You completed the game!")

else:

    print("\nGame Finished.")


print("\n========== FINAL STATS ==========")
print("Name:", name)
print("Class:", player_class)
print("Level:", level)
print("Gold:", gold)
print("Enemies defeated:", enemies_defeated)
print("Potions left:", potions)
print("================================")