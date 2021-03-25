# User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here
        new_arr = ""
        index = N - 1
        carry = 0
        while(index > -1):
            num = arr[index]
            if index == N - 1 and num + 1 > 9:
                new_arr = "0"
                carry = 1
            elif num + carry > 9:
                new_arr = "0" + new_arr
                carry = 1
            else:
                carry = 0
                new_arr = str(arr[index] + carry + 1) + new_arr
                f = ""
                for digit in range(0, index):
                    f += str(arr[digit])
                new_arr = f + new_arr
                break
            index -= 1
        if carry > 0:
            new_arr = str(carry) + new_arr
        return new_arr


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    arr = [0, 0, 9, 9, 9]
    N = 3
    ob = Solution()
    ptr = ob.increment(arr, len(arr))
    print(ptr)
# } Driver Code Ends
