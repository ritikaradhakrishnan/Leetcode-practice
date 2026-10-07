class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        #2 x slow = fast
        #2(p+C-X) = p + C-X + C
        #0 -> 1->2->3->4->5->1
        # p^     C-x^      x^

        #Each time, the current value becomes the next index, that's how we find the loop.
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


        
        