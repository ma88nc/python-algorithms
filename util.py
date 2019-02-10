from random import randint

# Create a list of random numbers ranging from minValue to maxValue
def randomList(minValue, maxValue, size):
    lst = []  # init list
    for i in range(0, size):
        lst.append(randint(minValue, maxValue))

    return lst

# Randomize list using the Fisher-Yates shuffle algorithm.
def randomizeList(lst):
    # Read array from highest index to lowest
    sz = len(lst)
    for i in range(sz-1, 0, -1):
        # Generate a random number j such that 0 <= j <= i
        j = randint(0, i)

        # Swap current element with random generated index
        temp = lst[j]
        lst[j] = lst[i]
        lst[i] = temp

    return lst

# Swap two variables
def swap(x, y):
    return y, x    
    
