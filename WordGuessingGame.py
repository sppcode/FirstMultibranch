import random

list = ['dog', 'cat', 'bird']
n = random.randint(0,2)

while 1:
  print("I\'m thinking of an animal... what could it be?")
  guess = input("It's a... ")

  if guess == list[n]:
    print("Holy shit, you got it! nice.")
    break
  else:
    print("Damn, you an idiot")
    print("debug notice: result was: " + list[n])
    break
  
