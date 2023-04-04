import random
import os

clear = lambda : os.system('clear')
clear()

card = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k"]
#diller = random.choice(card)
mine = random.choices(card, k = 2)
print(mine)