class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencycount(self, A, N):
        # code here
        count = {}
        for integer in A:
            if integer not in count:
                count[integer] = 0
            count[integer] += 1
        for index in range(N):
            if index + 1 in count:
                A[index] = count[index + 1]
            else:
                A[index] = 0


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    N = 5
    A = [8, 8, 8, 8, 8]
    ob = Solution()
    ob.frequencycount(A, N)
    print(A)

# } Driver Code Ends
