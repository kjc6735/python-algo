N,K = map(int, input().split())

result = []

for k in range(1,N+1):
    if N % k == 0:
        result.append(k)
        
        
if len(result) < K:
    print(0)
else:
    print(result[K-1])