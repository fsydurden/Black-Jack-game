import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

strat_game = str(input("Do you want to play the black Jack game? Type y for yes and n for no."))
strat_game.lower()
if strat_game == "y":
    print(logo)
    user_cards = [random.choice(cards) , random.choice(cards)]
    computer_choice = [random.choice(cards), random.choice(cards)]
    print(f"Your cards :{user_cards}")
    print(f"Dealers cards: {computer_choice[0]}")
    user_total = user_cards[0] + user_cards[1]
    computer_total = computer_choice[0] + computer_choice[1]
    stage_two = str(input("Type y for yes if you want to take another card"))
    if stage_two == "y":
        user_cards += [random.choice(cards)]
        user_total += user_cards[2]
        print(f"Your cards : {user_cards} and your total score : {user_total}")
        if user_total > 21:
            print("You loose, your total is more than 21")
        else:
            stage_three = str(input("Type y for yes if you want to take another card"))
            if stage_three == "y":
                user_cards += [random.choice(cards)]
                user_total += user_cards[3]
                if user_total > 21:
                    print("You loose, your total is more than 21")
                else:
                    computer_choice += [random.choice(cards)]
                    computer_total += computer_choice[2]
                    if computer_total > 21:
                        print("User wins")
                    elif computer_total == user_total:
                        print("Its a draw!!")
                    else:
                        print("Computer wins")
    else:
        if user_total < computer_total:
            print("You wins")
        elif user_total > computer_total:
            print("Computer wins")
        elif user_total == computer_total:
            print("Its a draw!!!!!!1")
else:
    print("Game ended!")
