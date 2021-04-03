# User function Template for python3
from collections import defaultdict
from itertools import permutations


class Solution:
    def LargestEven(self, s):
        # code here
        numbers = []
        number = ""
        for st in s:
            numbers.append(int(st))
        if any(list(map(lambda x: x % 2 == 0, numbers))):
            min_even = min(list(filter(lambda x: x % 2 == 0, numbers)))
            number += str(min_even)
            numbers.remove(min_even)
        numbers.sort()
        for i in numbers:
            number = str(i) + number
        return number


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    s = "1324".strip()
    ob = Solution()
    print(ob.LargestEven(s))
# } Driver Code Ends
