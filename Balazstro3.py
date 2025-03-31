import random
from ctypes import c_char

from Balazstro_Functions import draw_pls
from Balazstro_Functions import select_pls
from Balazstro_Functions import recognize_pls
from Balazstro_Functions import choose_deck_pls
from Balazstro_Functions import round_end_cleanup_pls
from Balazstro_Functions import needed_score
from Balazstro_Functions import convert_pls
from Balazstro_Functions import add_score_pls
from Balazstro_Functions import discard_pls


global d_selected_number
global hand

# player setting up terminal
print("                                                                                     ↑")
for i in range(20):
    print("                                                                                     |")
print("Please increase the size of your terminal to fit the entire arrow, then press enter: ↓")
input()

deck = []
ranks = []
suits = []
win = True
#formatting
for i in range(4):
    print()

choose_deck_pls(ranks,suits,deck)

for i in range(0,len(deck)):
    ranks.append(i)
score = []
for i in range(0,len(deck)):
    score.append(0)

dicto = {d_ranks: {"Deck": d_deck,"Score": d_score}
    for d_ranks,d_deck,d_score in zip(ranks,deck,score)}

#main game loop
for loop in range(len(needed_score)):
    hand = [1, 2, 3, 4, 5, 6, 7, 8]
    draw_pls(8,ranks,dicto,loop,hand)
    check_this = []

    for i in range(len(needed_score)):
        check_this.append(hand[i]["Deck"])
    convert_pls(check_this)
    check_this = select_pls(check_this)
    recognize_pls(check_this)
    # score_earned =
    if needed_score[loop] > 999:
        print("You Lose!")
        win = False
        i += 999
    round_end_cleanup_pls()
    add_score_pls(dicto)

    if(win == True):
        print("Congratulations You Won!")



# discard = {}
# discard_pls ------- nemjo

#def add_score_to_hand_pls()

'''

- No duplicate cards -
- Played Hand priority - 
- Buffed cards -
- Show deck -
- Score
- Discard pile
- Number based ordering -

♥   ♦   ♣   ♠
J = 11
Q = 12
K = 13
A = 1 és 14

High Card      5 
Pair           20
Two Pair       40
3 Of A Kind    90
Straight       120
Flush          140
Full House     160
4 Of A Kind    170
Straight Flush 200
Royal Flush    250

'''