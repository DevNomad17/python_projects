from common import art_blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards(num_of_cards, hand):
    for _ in range(num_of_cards):
        hand.append(cards[random.randint(0, 12)])
    convert_aces(hand)


def is_bust(hand):
    if sum(hand) > 21:
        return True
    else:
        return False


def convert_aces(hand):
    if sum(hand) > 21:
        if hand.count(11) > 0:
            hand[hand.index(11)] = 1


def is_natural(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return True
    else:
        return False


def handle_naturals(player, computer):
    if is_natural(player_hand) and is_natural(dealer_hand):
        print("Everybody has a Blackjack")
        print_draw()
    elif is_natural(player_hand) and not is_natural(dealer_hand):
        print("Congratulations, you have a Blackjack")
        print_win()
    else:
        print("Dealer has a Blackjack")
        print_lose()


def dealer_play(player, dealer):
    while sum(dealer) < 17:
        deal_cards(1, dealer)
    print_final_hand(player, dealer)
    if is_bust(dealer):
        print("Dealer is bust, You win    (ʘ‿ʘ)╯")
    elif sum(player) > sum(dealer):
        print_win()
    elif sum(player) < sum(dealer):
        print_lose()
    else:
        print_draw()


def print_current_hand(player, dealer):
    print(f"    Your cards: {player}, current score: {sum(player)}")
    print(f"    Computer's first card: {dealer[0]}")


def print_final_hand(player, dealer):
    print(f"    Your final hand: {player}, final score: {sum(player)}")
    print(f"    Computer's final hand: {dealer}, final score: {sum(dealer)}")


def print_draw():
    print("It's a draw    (ಠ_ಠ)")


def print_win():
    print("You win    (ʘ‿ʘ)╯")


def print_lose():
    print("You lose    ༼ つ ◕_◕ ༽つ")


while True:
    play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'n':
        break
    print("\n\n\n\n\n\n\n")
    print(art_blackjack)
    player_hand = []
    deal_cards(2, player_hand)
    dealer_hand = []
    deal_cards(2, dealer_hand)
    deal = 'init'
    while True:
        if is_natural(player_hand) or is_natural(dealer_hand):
            print_final_hand(player_hand, dealer_hand)
            handle_naturals(player_hand, dealer_hand)
            break

        if deal == 'init':
            print_current_hand(player_hand, dealer_hand)
        deal = input("Type 'h' to hit, type 's' to stand: ")
        if deal == 's':
            break
        deal_cards(1, player_hand)
        print_current_hand(player_hand, dealer_hand)
        if is_bust(player_hand):
            print_final_hand(player_hand, dealer_hand)
            print("You are bust. You lose    ༼ つ ◕_◕ ༽つ")
            break
    if deal == 's':
        dealer_play(player_hand, dealer_hand)

print("\n\nBye Bye")
