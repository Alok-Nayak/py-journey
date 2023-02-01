import math
wh = int(input("wall height? "))
ww = int(input("wall width? "))
cpc = 5

x = (wh * ww) / cpc
num_of_can = math.ceil(x)

print(f"you'll need {num_of_can} cans of paint")
