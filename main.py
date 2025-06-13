import random
from art import logo
print(logo)

def deal_cards():
    """Function that picks cards at random"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for _ in range(2):
    """This loop assigns two random cards each to user and computer """
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

print(user_cards)
print(computer_cards)
def calculate_score(card_list):
    """Function that calculates scores in the list"""
    total = sum(card_list)
    if total == 21:
        return 0
    elif total > 21 and 11 in card_list:
            card_list.remove(11)
            card_list.append(1)
            total = sum(card_list)
            return total
    else:
        return total

display = ""

def check_winner(user_card_list, computer_card_list, display_text):
    user_total = calculate_score(user_card_list)
    computer_total = calculate_score(computer_card_list)
    if user_total == 0:
        display = "You won!! (Blackjack)"
        return False
    elif computer_total == 0:
        return "You lose, computer has Blackjack!!"
    elif user_total > 21:
        return "You lose!! Your score exceeds 21."
    elif computer_total > 21:
        return "You won!! Computer score exceeds 21."
    elif len(user_cards) == 3 and user_total <= 21 and user_total > computer_total :
        return "You won1"
    else:
        return True

winner = check_winner(user_cards,computer_cards,display)
print(winner)

while winner:
    choice = str(input("type 'y' if you want another card")).lower()
    if choice == "y":
        user_cards.append(deal_cards())
        print(user_cards )
        winner = check_winner(user_cards, computer_cards,display)

    else:
        winner = check_winner(user_cards,computer_cards,display)
