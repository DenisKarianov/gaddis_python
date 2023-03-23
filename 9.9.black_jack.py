# simplified black jack between two virtual players by using dictionary

import random


def main():
    # loop's end flag
    loop_flag = 'y'
    while loop_flag.lower() == 'y':
        # Create a deck of cards.
        deck = create_deck()
        first_pl_hand = {}  # make empty hand for 1st player
        second_pl_hand = {}  # make empty hand for 2nd player
        first_head_cards = "1st pl. cards"
        first_head_value = "1st pl. value"
        sec_head_cards = "2nd pl. cards"
        sec_head_value = "2nd pl. value"
        print(f"{first_head_cards:^17}\t{first_head_value:^13}\t{sec_head_cards:^17}\t{sec_head_value:^13}")
        pl1_fl = True  # flag loop for 1st player
        pl2_fl = True  # flag loop fore 2nd player
        print_list = []  # list for print dealt cards for both players on every iteration
        while pl1_fl or pl2_fl:
            if len(deck) >= 2:
                if pl1_fl:  # card for 1st player
                    # deal card
                    deck, first_pl_hand, card = deal_1card(deck, first_pl_hand)
                    # add card and value to print list
                    print_list.append(card)
                    print_list.append(first_pl_hand[card])
                    # check for 21
                    hand_value = count_hand(first_pl_hand)
                    if hand_value == 21:
                        pl1_fl = False
                    elif hand_value > 21:
                        ace_found, ace_list = check_ace(first_pl_hand)
                        if ace_found:
                            if len(ace_list) == 1:
                                first_pl_hand[ace_list[0]] = 1  # change value of ace from 11 to 1
                                if count_hand(first_pl_hand) >= 21:  # end loop
                                    pl1_fl = False
                            else:  # if there's more than one ace in hand
                                for i in range(len(ace_list)):
                                    if count_hand(first_pl_hand) > 21 and ace_found:
                                        first_pl_hand[ace_list[i]] = 1
                                        ace_found, ace_list_none = check_ace(first_pl_hand)
                                if count_hand(first_pl_hand) >= 21:  # end loop
                                    pl1_fl = False
                        else:
                            pl1_fl = False
                else:
                    # add empty value to print list because card is not dealt to the player
                    print_list.append("---")
                    print_list.append("---")

                if pl2_fl:  # card for 2nd player
                    # deal card
                    deck, second_pl_hand, card = deal_1card(deck, second_pl_hand)
                    # add card and value to print list
                    print_list.append(card)
                    print_list.append(second_pl_hand[card])
                    # check for 21
                    hand_value = count_hand(second_pl_hand)
                    if hand_value == 21:
                        pl2_fl = False
                    elif hand_value > 21:
                        ace_found, ace_list = check_ace(second_pl_hand)
                        if ace_found:
                            if len(ace_list) == 1:
                                second_pl_hand[ace_list[0]] = 1  # change value of ace from 11 to 1
                                if count_hand(second_pl_hand) >= 21:  # end loop
                                    pl2_fl = False
                            else:  # if there's more than one ace in hand
                                for i in range(len(ace_list)):
                                    if count_hand(second_pl_hand) > 21 and ace_found:
                                        second_pl_hand[ace_list[i]] = 1
                                        ace_found, ace_list_none = check_ace(second_pl_hand)
                                if count_hand(second_pl_hand) >= 21:  # end loop
                                    pl2_fl = False
                        else:
                            pl2_fl = False
                else:
                    # add empty value to print list because card is not dealt to the player
                    print_list.append("---")
                    print_list.append("---")
            else:
                pl1_fl = False
                pl2_fl = False
                # print card and its value for both players
            # print(print_list)
            print(f"{print_list[0]:^17}\t{print_list[1]:^13}\t{print_list[2]:^17}\t{print_list[3]:^13}")
            print_list = []  # erase for next iteration

        # check winner
        first_pl_result = count_hand(first_pl_hand)
        sec_pl_result = count_hand(second_pl_hand)
        if first_pl_result == sec_pl_result:
            if first_pl_result == 21:
                print(f"Draw! Both players has {first_pl_result} scores and win.")
            else:
                print(f"Draw! No one wins, both players has {first_pl_result} scores.")
        else:  # if values differ
            if first_pl_result <= 21 < sec_pl_result:
                print(f"First player wins with {first_pl_result} scores! Second player has {sec_pl_result} scores.")
            elif sec_pl_result <= 21 < first_pl_result:
                print(f"Second player wins with {sec_pl_result} scores! First player has {first_pl_result} scores.")
            elif first_pl_result <= 21 and sec_pl_result <= 21:
                if first_pl_result > sec_pl_result:
                    print(f"First player wins with {first_pl_result} scores! Second player has {sec_pl_result} scores.")
                else:
                    print(
                        f"Second player wins with {sec_pl_result} scores! First player has {first_pl_result}  scores.")
            else:
                print(f"Both players loose! First player has {first_pl_result} scores, second player has"
                      f" {sec_pl_result} scores.")

        loop_flag = input("Play again (y/n)? ")


# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value stored as key-value pairs.
    deck = {'Ace of Spades': 11, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 11, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 11, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 11, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10}

    # Return the deck.
    return deck


# The deal_1card function deals one card from deck and remove dealt card from deck
# from the deck.
def deal_1card(deck, hand):
    card = random.choice(list(deck))  # get random card from deck
    # save card and its value to hand dictionary
    hand[card] = deck[card]
    # delete dealt cards
    del deck[card]
    return deck, hand, card


def count_hand(hand):
    # count value of cards in hand
    total = 0  # var for total value of cards in hand
    for card in hand:
        total += hand[card]
    return total


def check_ace(hand):
    ace_found = False  # variable if ace found
    ace_list = []  # list for ace names
    for card in hand:
        if card == 'Ace of Spades' or card == 'Ace of Hearts' or card == 'Ace of Clubs' or card == 'Ace of Diamonds':
            if hand[card] == 11:  # check if value for the ace wasn't change to 1
                ace_found = True
                ace_list.append(card)
    return ace_found, ace_list


# Call the main function.
if __name__ == '__main__':
    main()
