for n in range(1,101):
    a = n%3
    b = n%5
    if a == 0 and b == 0:
        print("FizzBuzz")
    elif a == 0 and b != 0:
        print("buzz")
    elif a != 0 and b == 0:
        print("Fizz")
    else:
        print(n)