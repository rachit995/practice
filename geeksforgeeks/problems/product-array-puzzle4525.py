# User function Template for python3

def productExceptSelf(arr, n):
    # code here
    product = 1
    for integer in arr:
        product *= integer
    new_arr = [None] * n
    for index in range(n):
        if arr[index] == 0:
            val = 1
            for j in range(n):
                if index != j:
                    val *= arr[j]
        else:
            val = product / arr[index]
        new_arr[index] = int(val)
    return new_arr

    # {
    #  Driver Code Starts
    # Initial Template for Python 3


if __name__ == '__main__':
    n = 5
    arr = [10, 0, 5, 6, 2]
    ans = productExceptSelf(arr, n)
    print(ans)
# } Driver Code Ends
