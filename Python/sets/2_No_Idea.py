from array import array


n,m = tuple(map(int, input().split()))
array = list(map(int, input().split()))
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
happiness=0
for i in array:
    if i in A:
        happiness+=1
    if i in B:
        happiness-=1
print(happiness)

