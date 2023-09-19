ip = list(map(int, input().split()))

# Solution 1
i = 0
j = len(ip) - 1

# partition of array around 0
while i < j:
    if ip[i] < 0:
        i += 1
    elif ip[j] > 0:
        j -= 1
    else:
        ip[i], ip[j] = ip[j], ip[i]
        i += 1
        j -= 1

# remove negative numbers and 0
ip = ip[i:]

# if all numbers are negative or 0
if len(ip) == 0:
    print(1)
    exit()

# find the largest positive number
max_ele = 0
for i in ip:
    if i > max_ele:
        max_ele = i

# make an array of that size and fill with zeros
arr = [0 for _ in range(max_ele)]

# mark the numbers present in the array
for i in ip:
    arr[i-1] = 1

# find the first missing positive number
for i in range(len(arr)):
    if arr[i] == 0:
        print(i+1)
        break





