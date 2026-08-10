#snake and ladder game using random module ?
import random
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}

position = 0

print("Welcome to Snake and Ladder!")
print("Reach 100 to win.\n")

while position < 100:
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("You rolled:", dice)

    if position + dice <= 100:
        position += dice
        print("You moved to:", position)
    else:
        print("You need an exact roll to reach 100.")

    # Check for ladder
    if position in ladders:
        print("Ladder! Climb up.")
        position = ladders[position]
        print("New position:", position)

    # Check for snake
    elif position in snakes:
        print("Snake! Slide down.")
        position = snakes[position]
        print("New position:", position)

    print()

if position == 100:
    print("Congratulations! You won the game!")