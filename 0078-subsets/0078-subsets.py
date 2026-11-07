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


"""
why no nonlocal:
List: you’re only changing what’s inside it (append, pop). The variable subset still points to the same list, so no nonlocal.
count += 1: you’re making the variable point to a new number, since ints can’t be changed in place. That’s reassigning the name, so you need nonlocal.

Short version: changing the contents = no nonlocal, reassigning the variable = nonlocal
"""
