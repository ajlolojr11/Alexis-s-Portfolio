'''#Generate Program Ver 1.0 - choice(seq)
from random import choice

coin = choice(["heads", "tails"])
print(coin)'''

'''#Generate Program Ver 2.0 - randint(a, b)
import random

number = random.randint(1, 10)
print(number)'''

#Generate Program Ver 3.0 - shuffle(x)
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for c in cards:
    print (c)

