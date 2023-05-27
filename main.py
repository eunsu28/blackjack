import random
import os
from time import sleep as s

clear = lambda : os.system('clear')
clear()

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11]

diller = random.sample(card, 2)
mine = random.sample(card, 2)

second_card = random.choice(card)
mine_result = sum(mine)


print("your cards: ", mine)
print("your sub-card: ", second_card)

choice = input("add or not: ")

if choice == "add":
    final_result = mine_result + second_card
    print(final_result)
    s(1)
    if final_result > 21:
        print("you failed")
        clear()
else:
    print()