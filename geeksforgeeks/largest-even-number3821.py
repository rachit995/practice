# User function Template for python3
from collections import defaultdict
from itertools import permutations


class Solution:
    def LargestEven(self, s):
        # code here
        numbers = []
        for st in s:
            numbers.append(int(st))
        combos = list(permutations(numbers, len(numbers)))
        if any(list(map(lambda x: x % 2 == 0, numbers))):
            max_number = None
            index = len(combos) - 1
            while max_number is None:
                d_number = combos[index][len(combos[index]) - 1]
                if d_number % 2 == 0:
                    max_number = "".join(list(map(str, combos[index])))
                index -= 1
            return max_number
        else:
            return "".join(list(map(str, combos[len(combos) - 1])))


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    s = "1324".strip()
    ob = Solution()
    print(ob.LargestEven(s))
# } Driver Code Ends
