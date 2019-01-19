from random import randint

# Create a list of random numbers ranging from minValue to maxValue
def randomList(minValue, maxValue, size):
    lst = []  # init list
    for i in range(0, size):
        lst.append(randint(minValue, maxValue))

    return lst


    
