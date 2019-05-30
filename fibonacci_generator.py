def get_input():
    num = int(
        input("Enter how many values of the fibonacci sequence would you like: "))
    return num

# Start of Fibonacci sequence
list = [0, 1]

# Generate the fibonacci sequence to number of iterations required

def fibonacci(val):
    while val > 1:
        new = list[len(list)-1] + list[len(list)-2]
        list.append(new)
        val -= 1
    return list

# User input
fibonacci(get_input())

# Print result
print("The Fibonacci sequence to %s places is: " % (len(list)-1))
for i in list[1:]:
    print(i)
