import random
number=random.randint(1,9)
trial=5
while(trial>0):
    trial=trial-1
    guess=int (input("Guess a number between 1-9 "))
    if(guess == number ):
        print("Congratulations!You won the game")
        break
    elif(guess<number):
        print("The number is low. Guess a higher number")
    elif(guess>number):
        print("The number is higher. Guess a lower number")
if(not trial>0):
    print("You lost the game. The number is",number)
