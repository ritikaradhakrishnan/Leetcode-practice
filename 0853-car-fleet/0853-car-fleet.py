class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pairs = [[p,s] for p,s in zip(position, speed)]
        # pairs.sort()
        # stack = []
        # for p, s in pairs[::-1]:
        #     stack.append((target-p)/s)
        #     if len(stack)>=2 and stack[-1]<= stack[-2]:
        #         stack.pop()
        # return len(stack)

        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs.sort()
        stack = []
        for p, s in pairs[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
