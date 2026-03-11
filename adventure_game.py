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

def main():
    display_title()
    player_name = get_player_name()

main()