import re
import json

def display_title():
    print("-" * 50)
    print("Welcome to the Python Adventure Game!")
    print("-" * 50)
    print("\nIn this game, you will make choices that shape your story.")
    print("Your decisions will be saved at the end.\n")

def get_player_name():
    while True:
        name = input("Enter your name. You can use lowercase letters, numbers, or underscores only: ")
        if re.match(r"^[a-z0-9_]+$", name):
            print(f"\nWelcome, {name}! Your adventure begins now.")
            print("-" * 50)
            return name
        else:
            print("Invalid name. Please use only lowercase letters, numbers, or underscores.\n")

def forest_path(player_name, decisions):
    print("You find yourself at the edge of a dark forest.")
    print("1. Enter the dark and scary forest")
    print("2. Turn back to the village")

    choice = input("\nWhat do you do? (1 or 2): ")

    if choice == "1":
        print("-" * 50)
        print(f"Brave choice, {player_name}! You enter the dark forest and discover hidden treasure!")
        decisions.append("Entered the dark forest")
        cave_scene(player_name, decisions)
    elif choice == "2":
        print("-" * 50)
        print(f"You return to the village and rest safely for the night.")
        decisions.append("Returned to the village")
        village_scene(player_name, decisions)
    else:
        print("-" * 50)
        print("Invalid choice, defaulting to turning back.")
        decisions.append("Invalid choice, you are returned to village.")
        village_scene(player_name, decisions)

def village_scene(player_name, decisions):
    print("-" * 50)
    print("You arrive in the village and hear a commotion near the market.")
    print("A merchant is arguing with a young boy accused of stealing bread.")
    print("1. Step in and defend the boy")
    print("2. Mind your own business and walk past")

    choice = input("\nWhat do you do? (1 or 2): ")

    if choice == "1":
        print("-" * 50)
        print(f"You defend the boy, {player_name}, but the merchant turns the crowd against you.")
        print("You're chased out of the village and lose half your supplies.\n")
        decisions.append("Defended the boy and chased out of village.")
    elif choice == "2":
        print("-" * 50)
        print(f"As you walk past, the merchant notices your confidence and mistakes you for a guard.")
        print("He tips you generously and offers you a free room for the night.\n")
        decisions.append("Ignored the dispute and got rewarded by a merchant.")
    else:
        print("-" * 50)
        print("Invalid choice, you wander the village aimlessly.")
        decisions.append("Wandered the village")

def cave_scene(player_name, decisions):
    print("-" * 50)
    print("Deep in the forest you find a cave. A faint glimmer comes from inside.")
    print("Scratched above the entrance are the words: 'LEAVE YOUR WEAPONS AT THE DOOR'")
    print("1. Respect the warning and leave your sword at the entrance")
    print("2. Keep your sword and enter cautiously")

    choice = input("\nWhat do you do? (1 or 2): ")

    if choice == "1":
        print("-" * 50)
        print(f"You leave your weapon and enter, {player_name}.")
        print("Inside, a dragon stirs from its sleep. Seeing you unarmed, it recognizes you as a peaceful visitor.")
        print("It gifts you rare armor as a token of respect.\n")
        decisions.append("Respected the cave warning and got rewarded by a dragon.")
    elif choice == "2":
        print("-" * 50)
        print(f"You grip your sword and step inside, {player_name}.")
        print("The metal clangs against the cave wall. A monster lurking in the shadows is startled awake.")
        print("You barely escape, but not before it tears through your supplies.\n")
        decisions.append("Ignored the warning and got attacked by a monster")
    else:
        print("-" * 50)
        print("Invalid choice, you linger at the entrance until nightfall and sleep in the cold.\n")
        decisions.append("Hesitated at cave entrance")

def get_outcome_summary(decisions):
    outcome_map = {
        "Entered the dark forest": "You braved the unknown and ventured into danger.",
        "Returned to the village": "You chose safety over adventure.",
        "Defended the boy and chased out of village.": "Your good intentions led to an unfortunate outcome.",
        "Ignored the dispute and got rewarded by a merchant.": "Your indifference paid off unexpectedly.",
        "Respected the cave warning and got rewarded by a dragon.": "Your respect earned you a rare and powerful gift.",
        "Ignored the warning and got attacked by a monster": "Your caution worked against you in the darkness.",
        "Wandered the village": "You gained nothing from your time in the village.",
        "Hesitated at cave entrance": "Fear left you cold and empty handed.",
        "Invalid choice, you are returned to village.": "Indecision cost you the chance to choose your own path."
    }

    print("\nDecision & Outcome Summary:")
    for decision in decisions:
        outcome = outcome_map.get(decision, "Unknown outcome.")
        print(f"  {decision} → {outcome}")

def save_game_data(player_name, decisions):
    game_data = {
        "player_name": player_name,
        "decisions": decisions,
        "outcome_count": len(decisions)
    }

    with open(f"{player_name}_game_data.json", "w") as f:
        json.dump(game_data, f, indent=4)

    print(f"\nYour game data has been saved to {player_name}_game_data.json\n")

def main():
    while True:
        display_title()
        player_name = get_player_name()
        decisions = []

        forest_path(player_name, decisions)

        print("=" * 40)
        print("Your adventure has ended!")
        print(f"Here are the decisions you made and their outcomes, {player_name}:")

        get_outcome_summary(decisions)
        print("=" * 40)

        save_game_data(player_name, decisions)

        replay = input("\nWould you like to play again? (yes/no): ").lower()
        if replay != "yes":
            print(f"\nThanks for playing, {player_name}! Goodbye.\n")
            print("-" * 50)
            break
main()