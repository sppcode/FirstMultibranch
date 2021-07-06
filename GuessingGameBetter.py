import random

n = random.randint(1,99)

while 1:
  guess = int(input("Enter an integer from 1 to 99: "))
  if guess == "guess":
    break
  if guess < n:
    print("guess is low")
  elif guess > n:
    print("guess is high")
  else:
    print("you guessed it!")
    break

