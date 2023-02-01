#Pizza order: Based on a user's order, work out their final bill.
print("Welcome to python pizza deliveries!")
size = input("What size of pizza do you want ? S, M, or L : ")
pepperoni = input("Do you want pepperoni ? Y or N : ")
cheese = input("Do you want extra cheese? Y or N : ")
S = 15
M = 20
L = 25
PS = 2
PML = 3
EC = 1
bill = 0

if size == "S":
    bill += S
elif size == "M":
    bill += M
else:
    bill += L

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}$ ")
