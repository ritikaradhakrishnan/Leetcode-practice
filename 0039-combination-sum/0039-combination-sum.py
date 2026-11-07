class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        #very similar to previous question

        result = []
        subset = []
        def dfs(i, total):
            if total == target:
                result.append(subset.copy())
                return
            if i>=len(candidates) or total > target:
                return
            #choose to add the candidate
            #i and not i+1 because we are allowed to repeat, eg. [2,2,3]
            subset.append(candidates[i])
            dfs(i, total + candidates[i])

            #chose to not include and move on to next index
            subset.pop()
            dfs(i+1, total)

        dfs(0,0)
        return result