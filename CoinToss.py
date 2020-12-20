# File		    : Coin-Toss.py
# Description	    : Coin toss (head or tails)
# Last Modified     : 19/02/2020
# Author	    : Engr. Dom

import random as rnd
question = "wtf!"
while question != "q":
    question = input("Call heads or tails.")
    answer = rnd.randint(1, 2)
    if question == "q":
        print("You're done!")
        break
    elif question != "heads" and question != "tails":
        print("WTF?")
    elif answer == 1:
        print("Heads, I win!")
    else:
        print("Tails, You lose!")
