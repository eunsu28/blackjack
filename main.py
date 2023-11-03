import random
import os
from time import sleep as s

on_game = True

while on_game:
    clear = lambda : os.system('clear')
    clear()

    card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11]

    diller = sum(random.sample(card, 2))
    mine = random.sample(card, 2)

    second_card = random.choice(card)
    mine_result = sum(mine)
    final_result = mine_result + second_card


    print("your cards: ", mine)
    print("your sub-card: ", second_card)

    choice = input("add or not: ")

    if choice == "add":
        print(final_result)
        mine_result = final_result
        s(1)
    elif choice == "off":
        on_game = False
    else:
        print(mine_result)

    if mine_result > 21:
        print("you failed")
        s(1)
        if diller == 21:
            print("blackjack")
            print("diller's number was: ", diller)
        else:
            print("diller's number was: ", diller)
    else:
        print("diller's number: ", diller)

    if mine_result > diller:
        print("you win")
    elif mine_result == diller:
        print("tie")
    else:
        print("you lose")

    s(3)