# Find all permutations using backtracking.
# Ported from C# 
import sys

# Swap characters at position
# a:    string value
# i:    position 1
# j:    position 2
# return swapped string
def swap(a, i, j):   
    b = list(a)
    b[i] = a[j]
    b[j] = a[i]
    return ''.join(b)

# Permutation function
# str:  string to calculate permutation for
# l:    starting index
# r:    end index
def permute(str, l, r):
    # print("in permute: string {} for indexes {} and {}".format(str, l, r))
    if l == r:
        print(str)
    else:
        for i in range(l, r+1):
            # print("calling first swap of string {} for indexes {} and {}".format(str, l, i))
            str = swap(str, l, i)
            # print("out of first swap:" + str)
            permute(str, l+1, r)
            # print("calling second swap of string {} for indexes {} and {}".format(str, l, i))
            str = swap(str, l, i)    
            # print("out of second swap:" + str)


def main():
    if len(sys.argv) < 2:
        print("Please invoke with a string. This program will output all permutations of it.")
        return
    n = len(sys.argv[1])
    str = sys.argv[1]
    print("Permutationus determinus")
    permute(str, 0, n-1)    


if __name__ == '__main__':
    main()