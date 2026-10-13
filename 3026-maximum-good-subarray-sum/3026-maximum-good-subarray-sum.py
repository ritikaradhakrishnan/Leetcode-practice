# When you see a subarray problem, try to represent the subarray as [l...r].

# Here, we need to find a subarray such that: |nums[r] - nums[l]| = k

# We can rewrite the absolute value condition as: nums[r] - nums[l] = k or nums[r] - nums[l] = -k

# Therefore: nums[l] = nums[r] - k or nums[l] = nums[r] + k

# So, for every index r, we need to find an earlier index l whose value is either:

# nums[r] - k
# nums[r] + k


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dict = {}
        bestSum = float('-inf')
        running_sum = 0
        for n in nums:
            # 1. Total sum including the current element x
            current_total = running_sum + n
            # 2. Check if this chunk can start with (n - k)
            if (n - k) in dict:
                bestSum = max(bestSum, current_total - dict[n - k])
            # 2. Check if this chunk can start with (n + k)
            if (n + k) in dict:
                bestSum = max(bestSum, current_total - dict[n + k])
            # 4. Save the running sum before n (keep the minimum)
            if n not in dict or running_sum < dict[n]:
                dict[n] = running_sum
            running_sum += n
        return bestSum if bestSum!=float('-inf') else 0
        

        


        

        