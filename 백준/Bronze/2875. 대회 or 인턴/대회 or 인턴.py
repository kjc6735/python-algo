N,M,K = map(int, input().split())

maleCnt = 0
for i in range(1,M+1):
    if 2*i <= N:
        maleCnt = i

remain = K - (M-maleCnt) - (N - maleCnt*2)
for i in range(10000000):
    if remain - i*3 <= 0:
        maleCnt -= i
        break

print(maleCnt)
