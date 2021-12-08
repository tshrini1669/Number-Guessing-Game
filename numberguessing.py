import random
number = random.randint(1,9)
print("Guess A number between 1 to 9")
chances = 0
while chances < 5:
    guess = int(input("Guess a number-"))
    if(guess == number):
        print("CONGRATS!YOU WON THE GAME!!!!!!")
        break
    elif(guess < number):
        print("Guess a number higher than" + str(guess))
    else:
        print("Guess a number lower than" + str(guess)) 
    chances = chances+1 
if(chances == 5):
    print("You have lost the game. The correct number was" + str(number))       