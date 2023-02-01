#Number Guessing Game:

logo ="""___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/     |__|        \/          \/             \/     \/      """

import random
print(logo)
print("Welcome to the Number Guessing Game!")
number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
print(number)

def game(a):
  done = False
  count = a
  
  for i in range(a):
    print(f"You have {count} attempts remaining to guess the number.")
    player = int(input("Make a guess: "))
    count -= 1
    if number == player:
      print(f"You got it! the answer is {number}")
      done == True
      break
    elif number < player:
      print("Too High")
    elif number > player:
      print("Too Low")
    else:
      print("dfrtuilkjhg")
  if count == 0:
    print("You've run out of guesses, you lose.")
    

def easy():
  game(10)

def hard():
  game(5)

level=input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
  easy()
elif level == "hard":
  hard()
else:
  print("You haven't choose anything.")
