#to access all the code
import random

#they are two list in this part, []list, A value that is random
#coin = random.choice(["Heads", "tails"])
#print(coin)





#m = random.randint(1, 10)

#print(m)

cards = ["Jack", "queen", "King"]
random.shuffle(cards)
#print one at the time
for _ in cards:
    print(_)