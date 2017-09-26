# using PEP8 conventions
import random
currentFunds = 1000



def main():

    global currentFunds
    random_number = random.randrange(0, 36)

    while True:
        try:
            bet_amount = int(input("Your funds are £" + str(currentFunds) + " how much would you like to bet \n"))
        except:
            print("Invalid input")
        else:
            if bet_amount > currentFunds:
                print("You don't have enough funds")
            elif bet_amount <= 0:
                print("Your bet is too low")
            else:
                currentFunds = currentFunds - bet_amount
                print(str(bet_amount) + " has been deducted. Your remaining funds are now " + str(currentFunds))
                break

    while True:
        try:
            bet = int(input("Choose a number between 0 and 36\n"))
        except:
            print("Invalid input")
        else:
            if bet > 36 or bet < 0:
                print("A number between 0 and 36 was not input")
            else:
                print("A " + str(random_number) + " was rolled")
                break

    if random_number == bet:
        winnings = int(bet_amount * 35)
        currentFunds = currentFunds + winnings
        print("YOU WON £" + str(winnings))
    else:
        print("SORRY, bet lost")


while True:

    main()
    if currentFunds <= 0:
        print("You've run out of money, goodbye")
        break

