# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters,
#  alphabetical characters, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    # print(s.isalnum())
    alnumcount=0
    alphacount=0
    numericcount=0
    lowercount=0
    uppercount=0
    for letter in s:
        if letter.isalnum():
            alnumcount+=1
        if letter.isalpha():
            alphacount+=1
        if letter.isnumeric():
            numericcount+=1
        if letter.islower():
            lowercount+=1
        if letter.isupper():
            uppercount+=1
    if alnumcount==0:
        print(False)
    else:
        print(True)
    if alphacount==0:
        print(False)
    else:
        print(True)
    if numericcount==0:
        print(False)
    else:
        print(True)
    if lowercount==0:
        print(False)
    else:
        print(True)
    if uppercount==0:
        print(False)
    else:
        print(True)
    