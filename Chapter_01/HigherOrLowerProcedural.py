# %%
import random

# card constants (each defined as tuple which is immuntable)
suit_tuple = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
rank_tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

ncards = 8

def get_card(deck):
    '''
    input:  deck of cards
    output: top card from deck
    '''
    this_card = deck.pop()  # select 1st card of deck
    return this_card


# %%
def shuffle(deck_in):
    '''
    input:  deck of cards
    output: shuffled deck of cards
    '''
    deck_out = deck_in.copy()
    random.shuffle(deck_out)
    return deck_out

# %%
# create starting deck (defined as list which is mutable)
starting_deck_list = []
for suit in suit_tuple:
    for i, rank in enumerate(rank_tuple):
        card_dict = {'rank':rank, 'suit':suit, 'value':i+1}
        starting_deck_list.append(card_dict)

score = 50

# %%
while True:  # play multiple games
    print()
    print('###############################')
    print('Shuffling the deck')
    print()
    game_deck_list = shuffle(starting_deck_list)
    current_card_dict = get_card(game_deck_list)
    current_card_rank = current_card_dict['rank']
    current_card_value = current_card_dict['value']
    current_card_suit = current_card_dict['suit']
    print('Starting card is:', current_card_rank + ' of ' + current_card_suit)
    print()

    for card_number in range(0, ncards):  # play 1 game of this many cards
        print('Card ', card_number + 1, ' of ', ncards)
        answer = input('Will the next card be higher or lower than the ' +
                       current_card_rank + ' of ' + current_card_suit + 
                       '? (enter h or l): ')
        answer = answer.casefold()  # force lower case
        next_card_dict = get_card(game_deck_list)
        next_card_rank = next_card_dict['rank']
        next_card_suit = next_card_dict['suit']
        next_card_value = next_card_dict['value']
        print('Next card is:', next_card_rank + ' of ' + next_card_suit)

        if answer == 'h':
            if next_card_value > current_card_value:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15

        elif answer == 'l':
            if next_card_value < current_card_value:
                print('You got it right, it was lower')
                score = score + 20
            else:
                print('Sorry, it was not lower')
                score = score - 15

        print('Your score is: ', score)
        print()
        current_card_rank = next_card_rank
        current_card_value = next_card_value
        current_card_suit = next_card_suit

    go_again = input('To play again, press ENTER, or "q" to quit: ')
    if go_again == 'q':
        break

print('OK bye')
# %%