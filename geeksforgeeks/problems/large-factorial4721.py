# User function Template for python3
class Solution:

    def factorial(self, a, n):
        # code here
        def fact(a):
            if a == 0 or a == 1:
                return 1
            prod = 1
            while(a > 1):
                prod *= a
                a -= 1
            return prod
        new_arr = [None] * n
        for index in range(n):
            new_arr[index] = fact(a[index])
        return new_arr

# {
#  Driver Code Starts
# Initial Template for Python 3


# Driver code
if __name__ == "__main__":
    n = 5
    a = [0, 1, 2, 3, 4]
    ob = Solution()
    res = ob.factorial(a, n)
    print(res)
# } Driver Code Ends
