arr = [10]
res = arr[0]
for i in range(1,len(arr)):
    if arr[i] > res:
        res = arr[i]

print(res)
