import sys

sys.stdin = open("input.txt", "r")


def check(num: int) -> True:
    arr = str(num)
    gap = int(arr[0]) - int(arr[1])
    for i in range(len(arr)-1):
        if (int(arr[i]) - int(arr[i+1])) != gap:
            return False
    return True

cnt = 0
N = int(input())
for i in range(1,N+1):
    if(i <= 99):
        cnt+=1
    else:
        if check(i):
            cnt+=1
            
print(cnt)