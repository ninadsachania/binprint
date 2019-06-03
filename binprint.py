#! /usr/bin/python3
#
# Aim: Take a decimal number and convert it to binary
# Author: Ninad Sachania

import sys

if len(sys.argv) <= 1:
    print('Usage:\n \
           binprint <number>...')
    sys.exit(-1)

# Get all the numbers to be converted to binary
NUMBERS = [int(arg) for arg in sys.argv[1:]]


def dec_to_bin(number: int) -> str:
    number = int(number)

    # List where individual binary digits will be stored
    digits = []

    while number > 0:
        # The quotient
        quotient = number // 2
        remainder = number % 2
        digits.append(remainder)
        number = quotient

    digits.reverse()

    # Return the binary number as a string
    return '0b' + ''.join(str(x) for x in digits)


for number in NUMBERS:
    print(dec_to_bin(number))
