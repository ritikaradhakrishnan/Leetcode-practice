class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS-1
        while top<=bottom:
            mid = (top + ((bottom-top)//2))
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        l, r = 0, len(matrix[mid])-1
        while l<=r:
            midnew = (l + ((r-l)//2))
            if target > matrix[mid][midnew]:
                l = midnew + 1
            elif target < matrix[mid][midnew]:
                r = midnew-1
            else:
                return True
        return False

        