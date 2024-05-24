arr = [1, 4, 5, 7, 9]

# Problem calculate sum of first n numbers

# brute force sum  O(n*m)
# we are calculating sum for each number separately
sum = 0
for i in range(0,3):
    sum += arr[i]

print(sum)


# prefix sum
len_arr = len(arr)
prefix_sum_arr = [0] * (len_arr + 1)

for i in range(1, len_arr + 1 ):
    prefix_sum_arr[i] = prefix_sum_arr[i-1] + arr[i-1]


for i, val in enumerate(prefix_sum_arr):
    print(i, val)