import random
from collections import Counter

#amount of score needed as the number of rounds increase
needed_score = [30,150,250,340,400,500,600]

def convert_pls(l_check_this):
    r_numbers = []
    forms = []
    templist = []
    tempcount = len(l_check_this)

    for i in range(tempcount):
        templist.append(l_check_this[i].split())

    l_check_this = templist

    for i in l_check_this:
        r_numbers.append(i[0])
        forms.append(i[1])

    number_to_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                     'K': 13, 'A': 14}

    converted_numbers = []
    for i in range(len(r_numbers)):
        converted_numbers.append(number_to_value[r_numbers[i]])
    r_numbers = converted_numbers

def round_end_cleanup_pls():
    print("\nCongratulations! You Win This Round!")
    print("\nPress Enter to proceed to the next round!\n")
    input()
    for i in range(4):
        print()

def choose_deck_pls(l_ranks: list,l_suits: list,l_deck: list):
    """
    :param l_ranks: list
    :param l_suits: list
    :param l_deck: list
    """
    l_ranks = []
    l_suits = []
    print("Wellcome to Balazstro!")
    print("It is a simplifed, text based Balatro (a poker game).")
    print()
    print("You can choose between decks, to just play the game or to test some kind of functionality:")
    print("Type the number of the deck you want!\n")
    print("Default Deck:                     All the suits ♥ ♦ ♣ ♠      -  All the ranks          number to type: 1")
    print("Pairs/X of a kind Tester Deck:    All the suits ♥ ♦ ♣ ♠      -  A,K                    number to type: 2")
    print("A-Straight Tester Deck:           Red suits     ♥ ♦          -  A,2,3,4,5,6            number to type: 3")
    print("Royale/Straight Tester Deck:      Red suits     ♥ ♦          -  K,J,Q,10,9,A           number to type: 4")

    for i in range(8):
        print()
    chosen_deck = int(input())
    print()

#setting ranks
    if(chosen_deck == 1):
        l_ranks = [" 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", "10 ", " J ", " Q ", " K "," A "]
    if (chosen_deck == 2):
        l_ranks = [" A "," K "]
    if (chosen_deck == 3):
        l_ranks = [" A "," 2 ", " 3 ", " 4 ", " 5 ", " 6 "]
    if (chosen_deck == 4):
        l_ranks = [" 9 ", "10 ", " J ", " Q ", " K "," A "]

# setting suits
    if(chosen_deck == 1 or chosen_deck == 2):
        l_suits = ["♥", "♦", "♣", "♠"]
    else:
        l_suits = ["♥", "♦"]

    for suit in l_suits:
        for rank in l_ranks:
            temp = rank + suit
            l_deck.append(temp)

    print("This is your deck: ")

#typeing enter after each suit
    for i in range(len(l_deck)):
        if ((i) % (len(l_deck)/len(l_suits)) == 0):
            print("")
        print(l_deck[i],",", end="")
    print()

def draw_pls(i_draw_this_many: int,l_numbers: list,d_deck: dict,loop: int,l_hand):
    """
    :param i_draw_this_much: int
    :param l_numbers: list
    :param d_deck: dict
    :param loop: int
    :return:
    """

    r_numbers = l_numbers.copy()
    random.shuffle(r_numbers)


#formatting
    print("\nRound:",loop+1,"! You need to Score",needed_score[loop],"points to get to the next round!")
    print("\nType the number of the cards you want to play (up to 5)! ")

    for i in range(i_draw_this_many):
        l_hand[i] = d_deck[r_numbers[i]]
        if (l_hand[i]["Score"] == 0):
            print(l_hand[i]["Deck"],"      number to type:",i+1)
        else:
            print(l_hand[i]["Deck"], "+", l_hand[i]["Score"]," number to type:",i+1)

def recognize_pls(l_check_this):
    print("Your Selected Cards Are: ",l_check_this)

    r_numbers = []
    forms = []
    templist = []
    tempcount = len(l_check_this)

    for i in range(tempcount):
        templist.append(l_check_this[i].split())

    check_this = templist

    for i in check_this:
        r_numbers.append(i[0])
        forms.append(i[1])

    number_to_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                     'K': 13, 'A': 14}

    # print(r_numbers)
    tempo = len(r_numbers)
    converted_numbers = []
    for i in range(tempo):
        converted_numbers.append(number_to_value[r_numbers[i]])
    r_numbers = converted_numbers

# Ordering cards:

    for i, nums in enumerate(converted_numbers):
        for i, numb in enumerate(converted_numbers[:-1], start=1):
            if (converted_numbers[i - 1] > converted_numbers[i]):
                converted_numbers[i - 1], converted_numbers[i] = converted_numbers[i], converted_numbers[i - 1]

    flush_check = False
    straight_check = False
    royal_flush_check = False
    four_of_a_kind_check = False
    full_house_check = False
    two_pair_check = False
    three_of_a_kind_check = False
    a_pair_check = False


    if(converted_numbers == [2, 3, 4, 5, 14]):
        straight_check = True

    if (len(converted_numbers) == 5):
        is_bigger = 0
        for i in range(1, 5):
            if (converted_numbers[i - 1] + 1 == converted_numbers[i]):
                is_bigger += 1
            else:
                i += 999
        if (is_bigger == 4):
            straight_check = True


# Counting how many of each number we have
    pair_counter = Counter(converted_numbers)
    pair_counter_values = list(pair_counter.values())

# 4 Of A Kind
    try:
        if(pair_counter_values[0] == 4 or pair_counter_values[1] == 4):
            four_of_a_kind_check = True
    except: pass

# Full House
    try:
        if(pair_counter_values[0] == 2 and pair_counter_values[1] == 3 or pair_counter_values[1] == 2 and pair_counter_values[0] == 3):
            full_house_check = True
    except: pass

# 2 Pair
    try:
        if (pair_counter_values[0] == 2 and pair_counter_values[1] == 2 or pair_counter_values[0] == 2 and pair_counter_values[2] == 2 or pair_counter_values[1] == 2 and pair_counter_values[2] == 2):
            two_pair_check = True
    except:
        pass

# 3 Of A Kind
    try:
        if(pair_counter_values[0] == 3 or pair_counter_values[1] == 3 or pair_counter_values[2] == 3):
            three_of_a_kind_check = True
    except: pass

# Pair
    try:
        if(pair_counter_values[0] == 2 or pair_counter_values[1] == 2 or pair_counter_values[2] == 2 or pair_counter_values[3] == 2):
            a_pair_check = True
    except: pass

# not printing hand types twice - negating checks
    if (full_house_check == True):
        three_of_a_kind_check = False
        a_pair_check = False
        two_pair_check = False

    if (four_of_a_kind_check == True):
        three_of_a_kind_check = False
        a_pair_check = False

    if (two_pair_check == True):
        a_pair_check= False

    if (three_of_a_kind_check == True):
        a_pair_check = False

    hand_type_score = 0

# printing hand type
    if(four_of_a_kind_check == True):
        hand_type_score = 170
        print("You Got A : 4 Of A Kind:",hand_type_score,"!")

    if(full_house_check == True):
        hand_type_score = 160
        print("You Got A : Full House:",hand_type_score,"!")


    if(two_pair_check == True):
        hand_type_score = 40
        print("You Got A : 2 Pair:",hand_type_score,"!")

    if (three_of_a_kind_check == True):
        hand_type_score = 90
        print("You Got A : 3 Of A Kind:",hand_type_score,"!")

    if(a_pair_check == True):
        hand_type_score = 20
        print("You Got A : Pair:",hand_type_score,"!")

    if(straight_check == True and flush_check == False):
        hand_type_score = 120
        print("You Got A : Straight:",hand_type_score,"!")

    elif(straight_check == False and flush_check == True):
        hand_type_score = 140
        print("You Got A : Flush:",hand_type_score,"!")

    elif (straight_check == True and flush_check == True and royal_flush_check == False):
        hand_type_score = 200
        print("You Got A : Straight Flush: ",hand_type_score,"!")

    elif (royal_flush_check == True):
        hand_type_score = 250
        print("You Got A : Royale Flush:",hand_type_score,"!")

    elif not any([four_of_a_kind_check,full_house_check,two_pair_check,three_of_a_kind_check,a_pair_check]):
        hand_type_score = 5
        print("You Got A : High Card:",hand_type_score,"!")

def discard_pls():
    print("This could discard your selected hand in the future")

def select_pls(l_check_this):
    temp_list = []

    print("\nType the numbers you want to Select and Press Enter!")
    p_input = input()
    p_input = [str(int(x) -1) for x in p_input]


    d_selected_number = [int(char) for char in p_input]
    for i in d_selected_number:
        temp_list.append(l_check_this[i-1])
    l_check_this = temp_list
    return l_check_this

def showdeck_pls(show: int, d_deck: dict):
    """
    :param show: int
    :param d_deck: dict
    """
    print("\nThis is your Deck:\n")
    for i in d_deck:
        if (show[i]["Score"] == 0):
            print(show[i]["Deck"])
        else:
            print(show[i]["Deck"],"+",show[i]["Score"])

def add_score_pls(d_deck: dict):
    """
    :param d_deck: dict
    """
    print("\nTo keep the gambling going You got a 50% chance to get + 10 Score to each of your cards!")

    for i in d_deck:
        x = random.randint(0, 1)
        if(x == 0):
            d_deck[i]["Score"] += 10
    # showdeck_pls(8,d_deck)
