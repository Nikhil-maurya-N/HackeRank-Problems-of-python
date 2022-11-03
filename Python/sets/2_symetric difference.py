# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a=set(input(),split())
n=int(input())
b=set(input(),split())
un=a.union(b)
inty=a.intersection()
diff=un.difference(inty)
print(diff)
