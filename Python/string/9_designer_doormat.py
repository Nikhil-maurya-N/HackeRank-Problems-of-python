# Designer Door Mat in Python - HackerRank Solution START
# this code is not written by me this is copied and pasted from web 
# i just understanded the working of that
N, M = map(int, input().split())
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))
# Designer Door Mat in Python - HackerRank Solution END
