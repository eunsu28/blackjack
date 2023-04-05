import random
import os

clear = lambda : os.system('clear')
clear()

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11]
#diller = random.choice(card)
mine = random.sample(card, 2)
print(mine)

mine_result = sum(mine)
print(mine_result)