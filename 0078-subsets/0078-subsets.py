class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result, subset = [], []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            #decision to keep
            subset.append(nums[i])
            dfs(i+1)

            #decision to not add and move on to the next index
            subset.pop()
            dfs(i+1)

        dfs(0)
        return result
