import sys
import util

def findMin(lst):
    minIndex = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[minIndex]:
            minIndex = i
    return lst[minIndex]


def findMax(lst):
    maxIndex = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[maxIndex]:
            maxIndex = i
    return lst[maxIndex]    


def main():
    size = 10  # set default
    if len(sys.argv) > 1:
        size = int(sys.argv[1])    

    # Create a random list
    lst = util.randomList(0, 99, size)
    print("length of list is {}".format(len(lst)))
    print(lst)

    print("Findus minimus: {}".format(findMin(lst)))
    print("Findus maximus: {}".format(findMax(lst)))

if __name__ == '__main__':
    main()