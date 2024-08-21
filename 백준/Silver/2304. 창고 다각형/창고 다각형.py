import sys

maxValue = 0
N = int(sys.stdin.readline())

arr = [0] * (1002)

for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    arr[L] = H
    if maxValue < H:
        maxValue = H

sIndex = 0
eIndex = len(arr)-1
sMax = arr[sIndex]
eMax = arr[eIndex]
sum = arr[sIndex] + arr[eIndex]

for index, value in enumerate(arr):
    if value == maxValue:
        sIndex = index
        break
    if sMax < value:
        sMax = value
    sum += sMax 


for index in range(len(arr) - 1, 0, -1):
    if arr[index] == maxValue:
        eIndex = index
        break
    if eMax < arr[index]:
        eMax = arr[index]
    sum += eMax

if sIndex != eIndex:
    sum += (eIndex - sIndex + 1)*maxValue 
else:
    sum += maxValue

print(sum)

    
    