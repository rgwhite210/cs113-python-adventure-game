import re
import json

def display_title():
    print("=" * 40)
    print("Welcome to the Python Adventure Game!")
    print("=" * 40)
    print("\nIn this game, you will make choices that shape your story.")
    print("Your decisions will be saved at the end.\n")

def get_player_name():
    while True:
        name = input("Enter your name or code name (lowercase letters, numbers, underscores only): ")
        if re.match(r"^[a-z0-9_]+$", name):
            print(f"\nWelcome, {name}! Your adventure begins now.\n")
            return name
        else:
            print("Invalid name. Please use only lowercase letters, numbers, or underscores.\n")

def forest_path(player_name, decisions):
    print("You find yourself at the edge of a dark forest.")
    print("1. Enter the forest")
    print("2. Turn back to the village")

    choice = input("\nWhat do you do? (1 or 2): ")

    if choice == "1":
        print(f"\nBrave choice, {player_name}! You enter the forest and discover a hidden treasure!\n")
        decisions.append("Entered the forest")
        cave_scene(player_name, decisions)
    elif choice == "2":
        print(f"\nYou return to the village and rest safely for the night.\n")
        decisions.append("Returned to the village")
        village_scene(player_name, decisions)
    else:
        print("\nInvalid choice, defaulting to turning back.\n")
        decisions.append("Invalid choice - returned to village")
        village_scene(player_name, decisions)

def village_scene(player_name, decisions):
    print("You arrive in the village and hear a commotion near the market.")
    print("A merchant is arguing with a young boy accused of stealing bread.")
    print("\n1. Step in and defend the boy")
    print("2. Mind your own business and walk past")

    choice = input("\nWhat do you do? (1 or 2): ")

    if choice == "1":
        print(f"\nYou defend the boy, {player_name}, but the merchant turns the crowd against you.")
        print("You're chased out of the village and lose half your supplies.\n")
        decisions.append("Defended the boy - chased out of village")
    elif choice == "2":
        print(f"\nAs you walk past, the merchant notices your confidence and mistakes you for a guard.")
        print("He tips you generously and offers you a free room for the night.\n")
        decisions.append("Ignored the dispute - rewarded by merchant")
    else:
        print("\nInvalid choice, you wander the village aimlessly.\n")
        decisions.append("Wandered the village")

def cave_scene(player_name, decisions):
    print("Deep in the forest you find a cave. A faint glimmer comes from inside.")
    print("Scratched above the entrance are the words: 'LEAVE YOUR WEAPONS AT THE DOOR'")
    print("\n1. Respect the warning and leave your sword at the entrance")
    print("2. Keep your sword and enter cautiously")

    choice = input("\nWhat do you do? (1 or 2): ")

    if choice == "1":
        print(f"\nYou leave your weapon and enter, {player_name}.")
        print("Inside, a dragon stirs from its sleep. Seeing you unarmed, it recognizes you as a peaceful visitor.")
        print("It gifts you a scale of rare armor as a token of respect.\n")
        decisions.append("Respected the cave warning - rewarded by dragon")
    elif choice == "2":
        print(f"\nYou grip your sword and step inside, {player_name}.")
        print("The metal clangs against the cave wall. A monster lurking in the shadows is startled awake.")
        print("You barely escape, but not before it tears through your supplies.\n")
        decisions.append("Ignored the warning - attacked by monster")
    else:
        print("\nInvalid choice, you linger at the entrance until nightfall and sleep in the cold.\n")
        decisions.append("Hesitated at cave entrance")

def main():
    display_title()
    player_name = get_player_name()
    decisions = []

    forest_path(player_name, decisions)
    print(f"Decisions so far: {decisions}")

main()