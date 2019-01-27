import sys

# This is a version using dictionary, then sorting by key.
def bucketSortDict(strIn):
    bkt = {}
    strOut = ''
    for i in range(0, len(strIn)-1):
        bkt[strIn[i]] = bkt.get(strIn[i], 0) + 1
    #Retrieve the contents of the bucket
    for key in sorted(bkt.keys()): 
        #print(key, bkt[key])
        for i in range(0, bkt[key]):
            strOut += key
    return strOut

# This is a version sorting by list.
def bucketSort(strIn):
    bkt = [0] * 255
    strOut = ''    
    for i in range(0, len(strIn)-1):
        # First printable ASCII character is '' (32), so offset by 32 when saving.
        bkt[ord(strIn[i])-32] += 1
    for i in range(0, 255):
        for j in range(0, bkt[i]):
            strOut += chr(i+32)  
    return strOut

def main():
    strIn = ''
    sortMode = 'L'
    if len(sys.argv) > 1:
        strIn = sys.argv[1]
        if len(sys.argv) > 2:
            sortMode = sys.argv[2].upper()
        if sortMode not in ('D', 'L'):
            print ("Sort mode must be D [dictionary] or L [list]")
            return
        if sortMode == 'D':
            print("Stringus dictionarius sorto")
            strSorted = bucketSortDict(strIn)
        else:
            print("Stringus listus sorto")
            strSorted = bucketSort(strIn)  
        print ("Sorted string is {}".format(strSorted))
    else:
        print("Please supply string to sort")


if __name__ == '__main__':
    main()        
