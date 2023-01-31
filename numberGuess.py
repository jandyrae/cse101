import random
number = random.randint(1,75)
total_guesses = 0
#Save a random number from 1 to 75 in a variable
for i in range(76):
  
#Prompt the user for a guess
  guess = int(input("Take a guess, enter a number between 1 and 75. "))
#If they guess too high, tell them to guess lower
  total_guesses = total_guesses + 1
  #print number

  if guess > number:
      print ("You guessed too high")
#If they guess too low, tell them to guess higher
  elif guess < number:
    print ("You guessed too low")
#If the guess right, tell them how many guesses it took
  elif guess == number:
    print ("You got it, it only took you " + str(total_guesses) + " guesses!")