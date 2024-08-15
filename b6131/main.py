
N = int(input())
cnt = 0
for B in range(1,501):
    for A in range(B,501):
        AA = A*A
        BB = B*B
        if AA - BB == N : 
            cnt+=1
print(cnt)