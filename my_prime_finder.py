# Code has been refactored to make more efficient for larger numbers
# Even numbers > 2 now not calculated, numbers > number/2 not calculated

# Ask user for a number
number = (int(input("Enter your number: ")))
# Reduce workload by removing numbers greater than number/2
half = range(1, int(number/2))
# List of factors of number
result = []

# Generate list of factors of number and append number to end

def prime_factors():
    # Ignore even numbers
    if number == 2:
        print("Your number is a prime, factors are 1 and 2")
    elif number > 1 and number % 2 == 0:
        print("Your number is divisible by 1, 2, and itself so is NOT a prime")
    # Generate factors for odd numbers
    elif number % 2 != 0:
        for i in half:
            if number % i == 0:
                result.append(i)
        result.append(number)
        # Return result to user
        if len(result) == 2:
            print("Your number is prime, factors are 1 and %s" %
                  (str(result[1])))
        else:
            print("Your number is NOT a prime, factors are: ")
            for i in result:
                print(i,)

prime_factors()
