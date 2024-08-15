import sys
sys.stdin = open("input.txt","r" )

arr = []
for _ in range(9):
    arr.append(int(input()))

arr = sorted(arr)

result = []

for a in range(3):
    for b in range(a+1, 4):
        for c in range(b+1, 5):
            for d in range(c+1, 6):
                for e in range(d+1,7):
                    for f in range(e+1 ,8):
                        for g in range(f+1, 9):
                            if(arr[a]+arr[b]+arr[c]+arr[d]+arr[e]+arr[f]+arr[g] == 100):
                                print(arr[a])
                                print(arr[b])
                                print(arr[c])
                                print(arr[d])
                                print(arr[e])
                                print(arr[f])
                                print(arr[g])
                                exit()
