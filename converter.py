# converter.py
# Convert between decimal, binary, octal and hexadecimal
# using first principles
# not built in bin, oct, hex functions

import math

def dec_to_bin(dec_num):
    """ decimal to binary using repeated integer division by 2 """
    bin_num = ""
    while dec_num != 0:
        remainder = dec_num % 2
        bin_num = str(remainder) + bin_num
        dec_num = dec_num // 2
    return bin_num

def dec_to_oct(dec_num):
    """ decimal to octal using repeated integer division by 8 """
    oct_num = ""
    while dec_num != 0:
        remainder = dec_num % 8
        oct_num = str(remainder) + oct_num
        dec_num = dec_num // 8
    return oct_num

def dec_to_hex(dec_num):
    """ decimal to hexadecimal using repeated integer division by 16 """
    # initialize decimal to hexadecimal dictionary
    dec_hex_map = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6',
                   7:'7',8:'8', 9:'9', 10:'A', 11:'B', 12:'C',
                   13:'D', 14:'E', 15:'F'}
    # initialize result
    hex_num = ""
    # repeat while non-zero quotient
    while dec_num != 0:
        # get remainder when divided by base 16
        remainder = dec_num % 16
        # get remainder in hexadecimal character
        remainder = dec_hex_map[remainder]
        # concatenate result
        hex_num = remainder + hex_num
        # reduce quotient
        dec_num = dec_num // 16
    return hex_num

def bin_to_oct(bin_num):
    pass

def bin_to_dec(bin_num):
    """ binary to decimal using positional values """
    length = len(bin_num)
    dec_num = 0
    for i in range(length):
        dec_num += (int(bin_num[i]) * int(math.pow(2, length-i-1)))
    return dec_num

def bin_to_hex(bin_num):
    pass

def oct_to_bin(oct_num):
    pass

def oct_to_dec(oct_num):
    """ octal to decimal using positional values """
    length = len(oct_num)
    dec_num = 0
    for i in range(length):
        dec_num += (int(oct_num[i]) * int(math.pow(8, length-i-1)))
    return dec_num

def oct_to_hex(oct_num):
    pass

def hex_to_bin(hex_num):
    pass

def hex_to_oct(hex_num):
    pass

def hex_to_dec(hex_num):
    pass

# main
print(dec_to_bin(6))
print(dec_to_oct(13))
print(dec_to_hex(28))
# since machine display numbers in decimal by default,
# we will represent numbers in other bases using string
print(bin_to_dec("11010"))
print(oct_to_dec("32"))
# better still, do unit testing
