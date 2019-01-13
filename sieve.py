import sys
# --------------------------------
# Sieve of Eratosthenes
# Ported from csharphelper.com:  http://csharphelper.com/blog/2014/08/use-the-sieve-of-eratosthenes-to-find-prime-numbers-in-c/
# --------------------------------

def MakeSieve(max):
    # Make an array indicating whether numbers are prime.
    print("In MakeSieve with max = {}".format(max))
    is_prime = [True] * max 

    # Cross out multiples
    for i in range(2, max):
        # See if i is prime.
        if is_prime[i] == True:
            # Knock out multiples of i.
            for j in range(i*2, max, i):
                is_prime[j] = False
    return is_prime


def main():
    max = 50
    if len(sys.argv) > 1:
        max = int(sys.argv[1])
    print("list length = {}".format(max))
    arrPrimes = MakeSieve(max)
    for i in range(2, max):
        if arrPrimes[i] == True:
            print(i)


if __name__ == '__main__':
    main()





