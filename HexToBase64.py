import sys
import re

# Base64 character lookup table
base64Table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64Conversion(hex):
    returnValue = ""
    for i in range(0, len(hex), 6):
        # Take 3 hex digits (6 characters) at a time.
        partHex = hex[i:i+6]
        #print(partHex)
        
        # bin() converts to binary but does not left fill with zeroes and also returns leading "0b".
        # Remove the "0b" and left fill with zeroes to get full 24/16/8 bits. 
        partBin = bin(int(partHex, 16))[2:].zfill(len(partHex)*4)
        #print("partial binary - {}".format(partBin))
        # Now take the binary string six bits at a time.
        for j in range(0, len(partBin), 6):
            # If less than six digits, pad to the right with zeroes.
            sixBit = partBin[j:j+6].ljust(6, '0')
            # Convert binary string to decimal.
            dec = int(sixBit, 2)
            #print("decimal for bin {} is {}".format(sixBit, dec))
            # Look up the decimal value in the base64 table.
            b64Char = base64Table[dec]
            returnValue += b64Char
        # If we don't have a complete 24 bit string, return "=" for each missing 8 bits. 
        extraBits = int((24-len(partBin))/8)
        returnValue += "="*extraBits    

    return returnValue                

def main():
    # Basic validations
    # If no input parameter, exit with command line spec.
    if len(sys.argv) < 2:
        print("Pass hexadecimal string as parameter")
        return

    hex = sys.argv[1].upper()

    # Ensure legal hex digits (0-9, A-F) are passed
    if re.search(r'[^0-9A-F]', hex) is not None:
        print("Invalid hexadecimal character was supplied")
        return 

    # Ensure that input length is multiple of 2 in order to be complete hex digit.
    if len(hex) % 2 != 0:
        print("Detected incomplete hexadecimal digit")
        return        

    print("Base sixty-fourus convertus")
    print (base64Conversion(hex))

if __name__ == '__main__':
    main()
