# User function Template for python3

class Solution:
    def rearrange(self, arr, n):
        # code here
        negatives = [None] * n
        positives = [None] * n
        positive_index = 0
        negative_index = 0
        for index in range(0, n):
            if arr[index] < 0:
                negatives[negative_index] = arr[index]
                negative_index += 1
            else:
                positives[positive_index] = arr[index]
                positive_index += 1
        positive_index = 0
        negative_index = 0
        index = 0
        while(index < n):
            positive_value = positives[positive_index]
            negative_value = negatives[negative_index]
            if positive_value is not None and negative_value is not None:
                if index % 2 == 0:
                    arr[index] = positive_value
                    positive_index += 1
                else:
                    arr[index] = negative_value
                    negative_index += 1
            elif positive_value is not None and negative_value is None:
                arr[index] = positive_value
                positive_index += 1
            elif positive_value is None and negative_value is not None:
                arr[index] = negative_value
                negative_index += 1
            index += 1
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    n = 10
    arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    ob = Solution()
    ob.rearrange(arr, n)
    print(arr)

# } Driver Code Ends
