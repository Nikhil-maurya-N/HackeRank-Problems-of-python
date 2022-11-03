# You are given a string and your task is to swap cases.
#  In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    returnstring=""
    for letter in s:
        if letter.isupper():
            returnstring+=letter.lower()
        elif letter.islower():
            returnstring+=letter.upper()
        else:
            returnstring+=letter
    return returnstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)