# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# this code is written by me
def print_formatted(number):
    # your code goes here
    for i in range(n+1):
        o=oct(i)
        h=hex(i).upper()
        b=bin(i)
        print(f"{i} {o[2:]} {h[2:]} {b[2:]}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
