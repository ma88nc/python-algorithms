# Quicksort

import util

def Partition(lst, start, end):
    pivot = lst[end]

    # Elements less than pivot will be pushed to the left of pIndex.
    # Elements greater than pivot will be pushed to the right of pIndex.
    # Equal elements can go either way.
    pIndex = start

    # Each time we find an element less than or equal to pivot, pIndex
    # is incremented and that element would be placed before the pivot.
    for i in range(start, end):
        if lst[i] <= pivot:
            # temp = lst[i]
            # lst[i] = lst[pIndex]
            # lst[pIndex] = temp
            lst[i], lst[pIndex] = util.swap(lst[i], lst[pIndex])
            pIndex += 1

    # Swap pIndex with Pivot        
    # temp = lst[end]
    # lst[end] = lst[pIndex]
    # lst[pIndex] = temp
    lst[end], lst[pIndex] = util.swap(lst[end], lst[pIndex])

    # Return pIndex (index of pivot element)
    return pIndex

def Quicksort(lst, start, end):
    # Base condition
    if start >= end:
        return

    # Rearrange the elemnets across pivot
    pivot = Partition(lst, start, end)
    print("new pivot index {} and value are {}".format(pivot, lst[pivot]))
    print(lst)

    # Recurse on sub-array containing elements that are less than pivot.
    Quicksort(lst, start, pivot-1)

    # Recurse on sub-array containing elements that are greater than pivot.
    Quicksort(lst, pivot+1, end)

def main():
    #temp - test list randomizing function.
    lst = [10,9,8,7,32,26,31,24,21,6,5,4,3,2,1,20,44,3,2,7,88,30]
    newlst = util.randomizeList(lst)
    print(newlst)

    n = len(newlst)
    Quicksort(newlst, 0, n-1)
    print(newlst)

if __name__ == '__main__':
    main()