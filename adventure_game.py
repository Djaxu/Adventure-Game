import time
import random


def print_pause(mesagge_to_print):
    print(mesagge_to_print)
    time.sleep(1)


def intro(enemy):
    print_pause("You find yourself standing in an open field, filled with\n"
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,")
    print_pause("and has been terrifying the nearby village.")


def house(enemy, items):
    print_pause("You knock on the door of the house")
    print_pause(f"an enraged {enemy} is in front of you")
    if "Sword of Dawn" in items:
        print_pause("I feel good about this fight with my new shiny sword")
        fight(enemy, items)
    else:
        print_pause("I got a bad feeling about this")
        run_away = input("What do you do \n"
                         "run\n"
                         "fight\n")
        if "run" in run_away:
            print_pause("you run as fast as you can")
            choose_action(enemy, items)
        elif "fight" in run_away:
            print_pause("ok then it's your funeral")
            fight(enemy, items)
        else:
            print_pause("oh come on it was simple choice\n"
                        "too little too late now your dead")
            play_again()


def cave(enemy, items):
    print_pause("You peek in to the cave")
    if "Sword of Dawn" in items:
        print_pause("You looted the place already\n"
                    "go on adventure or something")
        choose_action(enemy, items)
    else:
        print_pause("After spending some time in cave you\n"
                    "found a curious looking stone")
        cave_loot(enemy, items)


def cave_loot(enemy, items):
    cave_choice = input("Do you want to look closer\n"
                        "yes or no  ")
    if "yes" in cave_choice:
        print_pause("what appeared to be a stone is in fact small parchment")
        print_pause("after few moments letters on the parchment\n"
                    "starts glowing")
        print_pause("tell me little mortal what letter am I? ")
        cave_riddle(enemy, items)
    elif "no" in cave_choice:
        print_pause("you turn back and exit the cave")
        choose_action(enemy, items)
    else:
        print_pause("its not hard ")
        cave_loot(enemy, items)


def cave_riddle(enemy, items):
    answer = input("I am the beginning of everything the end of everywhere.\n"
                   "I’m the beginning of eternity the end of time and space.\n"
                   "What am I?\n").lower()
    if answer == "e":
        items.append("Sword of Dawn")
        print_pause("magnificent light appears from nowhere")
        print_pause("when your sight is back\n"
                    "you can see shining sword in front of you")
        print_pause("You grab the Sword of Dawn and exit cave")
        choose_action(enemy, items)
    elif "quit" in answer:
        print_pause("you exit the cave ")
        choose_action(enemy, items)
    else:
        print_pause("how disappointing")
        print_pause("remember mortal you can always just 'quit'")
        print_pause("but don't lose hope yet\n"
                    "answer is in the beginning and the end")
        cave_riddle(enemy, items)


def fight(enemy, items):
    print_pause(f"You FIGHT {enemy}")
    if "Sword of Dawn" in items:
        print_pause("Slashing with your blade like crazy u managed to\n"
                    "not only "
                    f"not hert yourself but also kill {enemy}\n")
        print_pause("Good job I didnt expect this oh well ;]")
        play_again()
    else:
        print_pause("let me guess you thought you could win ha \n"
                    "guess again ")
        play_again()


def choose_action(enemy, items):
    choice = input("In front of you is a house. \n"
                   "To your right is a dark but smmall cave\n"
                   "1. House\n"
                   "2. Cave\n")
    if choice == "1":
        house(enemy, items)
    elif choice == "2":
        cave(enemy, items)
    else:
        print("Please enter 1 or 2, or else...")
        choose_action(enemy, items)


def play_again():
    print_pause("GAME OVER")
    choice = input("Do you want to play again yes or no   ")
    if "yes" in choice:
        main()
    elif "no" in choice:
        print_pause("See yaa")
    else:
        print_pause("still dont get how simple yes or no works \n"
                    "!COME ON!")
        play_again()


def main():
    enemy = random.choice(["wicked fairie", "troll",
                           "vampire", "fire elemental"])
    items = []
    intro(enemy)
    choose_action(enemy, items)


main()
