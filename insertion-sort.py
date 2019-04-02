# Insertion sort
# C# Sharp Searching and Sorting Algorithm Exercises: Insertion sort
#   https://www.w3resource.com/csharp-exercises/searching-and-sorting-algorithm/searching-and-sorting-algorithm-exercise-6.php

import util

def insertionSort(lst):
    for i in range(0, len(lst)-1):
        for j in range(i+1, 0, -1):
            #print("i = {}, j = {}".format(i, j))
            if lst[j-1] > lst[j]:
                #swap j and j-1
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

def main():
    #temp - test list randomizing function.
    lst = [10,9,8,7,32,26,31,24,21,6,5,4,3,2,1,20,44,3,2,7,88,30]
    newlst = util.randomizeList(lst)
    print(newlst)

    #n = len(newlst)
    # Quicksort(newlst, 0, n-1)
    newlst = insertionSort(newlst)
    print(newlst)

if __name__ == '__main__':
    main()