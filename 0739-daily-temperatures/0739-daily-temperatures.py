class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = [0]*len(temperatures)
        # stack = []
        # for i in range(len(temperatures)):
        #     while stack and temperatures[i] > stack[-1][0]:
        #         stackTemp, stackIndex = stack.pop()
        #         result[stackIndex] = (i - stackIndex)
        #     stack.append([temperatures[i], i])
        # return result

        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([temperatures[i], i])
        return result

        