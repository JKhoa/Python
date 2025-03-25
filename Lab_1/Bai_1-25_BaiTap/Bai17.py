# Define a function named "near_thousand" that takes an integer parameter "n"
def near_thousand(n):

    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

# Call the "near_thousand" function with the argument 1000 and print the result
print(near_thousand(1000))

# Call the "near_thousand" function with the argument 900 and print the result
print(near_thousand(900))

# Call the "near_thousand" function with the argument 800 and print the result
print(near_thousand(800))

# Call the "near_thousand" function with the argument 2200 and print the result
print(near_thousand(2200))
