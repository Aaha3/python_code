from random import randint
import time

intro = input("v1.6")

def slow_dots():
    for i in range(3):
        time.sleep(1)
        print(i*'.', end="")
    print()

def reload():
    print("card game")
    bet = input("whats your bet number? ")
    print("bet = " +"$" + bet)
    print("press enter to start")

    # betNUM = int(bet) + 1000
    opponent_card = str(randint(1,10))
    player_card = str(randint(1,10))
    opponant_add_up = str(randint(1,10)) + str(randint(1,10))
    player_add_up = str(randint(1,10)) + str(randint(1,10))
    print("your card numbers are " + player_card + ", " + player_card)
    slow_dots()
    time.sleep(1)
    print("the flop cards are " + str(randint(1,10)) + ", " + str(randint(1,10)) + " and " + str(randint(1,10)))
    time.sleep(1)
    print("the turn card is " + str(randint(1,10)))
    time.sleep(1)
    print("the last card is " + str(randint(1,10)))
    time.sleep(1)
    print("your opponent's cards are " + opponent_card + ", " + opponent_card)
    time.sleep(1)
    if opponant_add_up <= player_add_up:
        print("the winner is the opponent! you lose!")
        print("you lost " + "$" + bet + "!")
    else:
        print ("you are the winner! you won!")
        print("you won " + "$" + bet + "!")
        print("adding money to account...")

if __name__ == "__main__":
    # Create a counter to check if user plays for the first time
    counter=0

    while(True): 
        if counter == 0:
            reload()
            # increase counter as user has already played once
            counter+=1
            reload_y_n = input("do you want to reload???")
        else:
            reload_y_n = input("do you want to reload???")

        if reload_y_n == "y":
            reload()
        else:
            break