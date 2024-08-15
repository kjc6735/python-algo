N = int(input())

cnt = 0

for 남 in range(1,N+1):
    for 영 in range(1, N+1):
        for 택 in range (1, N+1):
            if 남 + 영 + 택 != N:
                continue
            if 영 + 2 > 남:
                continue
            if 택 % 2 == 1:
                continue
            cnt+=1
print(cnt)