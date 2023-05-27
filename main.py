import random
import os

clear = lambda : os.system('clear')
clear()

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11]
#diller = random.sample(card, 2)
mine = random.sample(card, 2)
second_card = random.choice(card)

print(mine)

mine_result = sum(mine)
print(mine_result)

print(second_card)

choice = input("add or not:")

if choice == "add":
    final_result = mine_result + second_card
    print(final_result)