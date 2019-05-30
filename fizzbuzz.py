user = int(input("Enter top of range: "))
list = range(1, user+1)

def game(list):
    for i in list:
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

game(list)
