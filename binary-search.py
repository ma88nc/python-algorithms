# binary search

import sys

def binarySearch(a, x):
    alen = len(a)
    low = 0
    high = alen-1
    iter=0
    print("low={}, high={}, x={}".format(low, high,x))
    while low < high: 
        # if a[low] == x:
        #     return low
        mid = int((high-low)/2) + low
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            high = mid #- 1
        else:
            low = mid + 1
        print("low={}, high={}, mid={}".format(low, high, mid))  
        if a[low] == x:
            return low
        iter += 1
        if iter > 8:
            return -2       
    return -1

def main():
    if len(sys.argv) > 1:
        x=int(sys.argv[1])
    else:
        print("Please enter value to search for")   
        return 
    lst = [1,5,6,7,9,10,12,14,15,16,18,20,21,23,25]

    print("Binarius searchus!")
    ret = binarySearch(lst, x)
    print("Result is {}".format(ret))

if __name__ == '__main__':
    main()         

''' pass in x=7
low=1, high=4, mid=0
low=3, high=4, mid=2
low=1, high=4, mid=0
low=3, high=4, mid=2
low=1, high=4, mid=0
low=3, high=4, mid=2 

pass in x=20 or x=19
low=5, high=15, mid=4
low=6, high=15, mid=5
low=5, high=15, mid=4
low=6, high=15, mid=5
low=5, high=15, mid=4


'''
