
N,M = map(int, input().split())
arr = list(map(int, input().split()))
s = 0
e = 0
cnt = 0
sum = arr[s]
while(e < N):
    if sum == M :
        cnt +=1
        sum -= arr[s]
        s+=1
    elif sum < M:
        e+=1
        if e >= N : break
        sum += arr[e]
    else:
        sum -= arr[s]
        s+=1

print(cnt)