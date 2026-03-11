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
    elif choice == "2":
        print(f"\nYou return to the village and rest safely for the night.\n")
        decisions.append("Returned to the village")
    else:
        print("\nInvalid choice, defaulting to turning back.\n")
        decisions.append("Invalid choice - returned to village")

def main():
    display_title()
    player_name = get_player_name()
    decisions = []

    forest_path(player_name, decisions)
    print(f"Decisions so far: {decisions}")

main()