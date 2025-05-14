# Kyle Beck
# Adventure Game
# 12 MAY 2025
# This program is a basic adventure game called strike.

import random

# Initialize health for characters and creatures
characters = {}
creatures = {
    "Spider": 100,
    "Snake": 100,
    "Bear": 100,
    "Lion": 100
}

# Get 3 characters from the user
print("Enter names for 3 characters:")
for i in range(1, 4):
    name = input(f"Enter name for character #{i}: ")
    characters[name] = 100

def choose_alive(options):
    return [name for name, hp in options.items() if hp > 0]

# Game loop
while True:
    alive_characters = choose_alive(characters)
    alive_creatures = choose_alive(creatures)

    # Check win/lose condition
    if not alive_characters:
        print("\nAll your characters have been defeated. Game Over!")
        break
    if not alive_creatures:
        print("\nAll creatures have been slayed. You win!")
        break

    print("\n--- Current Status ---")
    print("Characters:")
    for name, hp in characters.items():
        print(f"{name}: {hp} HP")
    print("\nCreatures:")
    for name, hp in creatures.items():
        print(f"{name}: {hp} HP")

    # Player chooses character and creature
    attacker = input("\nChoose a character to attack with: ")
    while attacker not in alive_characters:
        attacker = input("Invalid or dead character. Choose again: ")

    target = input("Choose a creature to attack (Spider, Snake, Bear, Lion): ").capitalize()
    while target not in alive_creatures:
        target = input("Invalid or dead creature. Choose again: ").capitalize()

    # Random attack damage
    player_damage = random.randint(1, 80)
    creature_damage = random.randint(1, 70)

    print(f"\n{attacker} attacks {target} for {player_damage} damage!")
    creatures[target] -= player_damage

    if creatures[target] <= 0:
        print(f"{target} has been slayed!")
        creatures[target] = 0
    else:
        # Creature strikes back
        print(f"{target} strikes back at {attacker} for {creature_damage} damage!")
        characters[attacker] -= creature_damage
        if characters[attacker] <= 0:
            print(f"{attacker} has been defeated!")
            characters[attacker] = 0
