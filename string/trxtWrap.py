# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .
import textwrap
def wrap(string, max_width):
    returnstring=""
    for index in range(0,len(string)//max_width):
        index=index*max_width
        returnstring+=string[index:index+max_width]+'\n'
    returnstring+=string[(len(string)-(len(string))%max_width):]
    return returnstring

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)