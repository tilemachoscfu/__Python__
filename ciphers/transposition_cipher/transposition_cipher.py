# Transposition cipher implemented in Python

import math

def main():
    message = input('Enter message: ')
    key = int(input('Enter key [2-%s]: ' % (len(message) - 1)))
    mode = input('Encryption/Decryption [e/d]: ')

    if mode.lower().startswith('e'):
        text = encryptMessage(key, message)
    elif mode.lower().startswith('d'):
        text = decryptMessage(key, message)

    print('Output: ', text )

def encryptMessage(key, message):
    cipherText = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)

def decryptMessage(key, message):
    numCols = math.ceil(len(message) / key) # math.ceil(x) >> return the ceiling of x as a float,
    numRows = key                               #  the smallest int value greater or equal to x.
    numShadedBoxes = (numCols * numRows) - len(message)
    plainText = [""] * numCols
    col = 0; row = 0;

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if (col == numCols) or (col == numCols - 1) and (row >= numRows - numShadedBoxes):
            col = 0
            row += 1

    return "".join(plainText)

if __name__ == '__main__':
    import doctest # the doctest module searches for pieces of text that look like interactive python
    doctest.testmod()   # and then executes those sessions to verify that they work exactly as shown.
main()