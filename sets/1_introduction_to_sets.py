def average(array):
    # your code goes here
    num=set(arr)
    sum=0
    t_num=0
    for i in num:
        sum+=int(i)
        t_num+=1
    avg=sum/t_num
    return f"{avg :.3f}"
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)