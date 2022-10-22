# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of
#  commands where each command will be of the  types listed above. Iterate through
#  each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    N = int(input())
    mainlist=[]
    commandlist=[]
    # clist=""
    for i in range(N):
        commandlist.append(str(input()))
    for command in  commandlist:
        clist=command.split()
        if clist[0]=="insert":
            mainlist.insert(int(clist[1]),int(clist[2]))
        elif clist[0]=="print":
            print(mainlist)
        elif clist[0]=="remove":
            mainlist.remove(int(clist[1]))
        elif clist[0]=="append":
            mainlist.append(int(clist[1]))
        elif clist[0]=="sort":
            mainlist.sort()
        elif clist[0]=="pop":
            mainlist.pop()
        elif clist[0]=="reverse":
            mainlist.reverse()
        else:
            print("invalid command")
        
        
        
