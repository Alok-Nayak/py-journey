print("Welcome to love calculator!")
a = input("Enter your name: ")
b = input("Enter your partners name: ")
name1 = a.lower()
name2 = b.lower()

name = name1 + name2

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')

true = t+r+u+e

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')

love = l+o+v+e

score = int(f"{true}{love}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.");
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")



