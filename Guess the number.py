from random import *
random_number = randint(0,10)
print ("Guess what number between 0 and 10 I am thinking of in under 7 guesses")
guessed_number = input()
guesses_made = 1
while int(guessed_number) != random_number and guesses_made < 7:
    if int(guessed_number) < random_number:
        print ("The number you guessed is too low")
    if int(guessed_number) > random_number:
        print("The number you guessed is too high")
    guessed_number = input()
    guesses_made = guesses_made + 1
if guesses_made < 7:
   print ("You win! You have correctly guessed it in " + str(guesses_made) + " tries")
else:
    print("You lose! You have exceeded the number of trials")
    
 