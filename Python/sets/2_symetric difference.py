# Enter your code here. Read input from STDIN. Print output to STDOUT
# m=int(input())
a = set(input().split())
# n=int(input())
b = set(input().split())

diff = a.difference(b)

diff1 = b.difference(a)

un = diff.union(diff1)
ls = list(un)
ls.sort()
for i in ls:
    print(i)
# 2 4 5 9
# 2 4 11 12