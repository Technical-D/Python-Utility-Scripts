def miniMaxSum(arr):
    # Write your code here
    a  = 0
    b = 0
    if len(set(arr)) == 1:
        a+= arr[1] * 4
        b+= arr[1] * 4

    for i in arr:
        if i != max(arr):
            a += i
    
    for i in arr:
        if i != min(arr):
            b+=i
    
    print(a, b)

miniMaxSum([5, 5, 5, 5, 5])