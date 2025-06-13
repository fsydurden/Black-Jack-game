import random
from art import logo
print(logo)

def deal_cards():
    """Pick one card at random from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(card_list):
    """Calculate the score of a hand. Return 0 for Blackjack."""
    total = sum(card_list)
    if total == 21 and len(card_list) == 2:
        return 0
    if total > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def check_winner(user_card_list, computer_card_list):
    """Determine the game result."""
    user_total = calculate_score(user_card_list)
    computer_total = calculate_score(computer_card_list)

    print(f"\nYour final hand: {user_card_list}, score: {user_total}")
    print(f"Computer's final hand: {computer_card_list}, score: {computer_total}")

    if user_total == 0:
        return "You win with a Blackjack!"
    elif computer_total == 0:
        return "Computer wins with a Blackjack. You lose!"
    elif user_total == 21:
        return "You won , you have 21 as your score"
    elif user_total > 21:
        return "You went over. You lose!"
    elif computer_total > 21:
        return "Computer went over. You win!"
    elif user_total > computer_total:
        return "You win!"
    elif user_total < computer_total:
        return "You lose!"
    else:
        return "It's a draw!"

# Start Game
user_cards = [deal_cards(), deal_cards()]
computer_cards = [deal_cards(), deal_cards()]

game_over = False

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nYour cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        another = input("Type 'y' to get another card, 'n' to pass: ").lower()
        if another == 'y':
            user_cards.append(deal_cards())
        else:
            game_over = True

# Computer plays after user stops
while calculate_score(computer_cards) < 21:
    computer_cards.append(deal_cards())

# Final result
print(check_winner(user_cards, computer_cards))
