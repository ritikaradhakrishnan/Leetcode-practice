# in Python, q[0] and q[-1] are just standard Python indexing used to peek at the leftmost and rightmost positions of the deque without removing anything.
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()

        for r, num in enumerate(nums):
            # 1. Evict smaller or equal elements and only then append(right most need ot eb the greatest so far)
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(r)
            #we are storing index not the elem itself
             # 2. Evict front index if it fell outside the window [r - k + 1, r]
            if q[0] <= r-k:
                q.popleft()
             # 3. Record max once the first window of size k is formed
            if r+1>=k:
                output.append(nums[q[0]])
        return output


        