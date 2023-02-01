ib = int(input("What is the Bill Amount? "))
p = int(input("Number of People? "))
t = int(input("Tip amount? "))

tip = ib*(t/100)
pay = round((ib+tip)/p, 2)

print(f"{pay}")