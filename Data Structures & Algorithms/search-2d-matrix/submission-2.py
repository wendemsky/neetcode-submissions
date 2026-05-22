class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search on first index of every row
        i, j = 0, len(matrix)-1
        row = 0
        while i <= j:
            mid = (i + j) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                j = mid - 1
            else:
                i = mid + 1
            
        print(row)
        i, j = 0, len(matrix[0])-1
        while i <= j:
            mid = (i + j) // 2
            if matrix[row][mid] == target:
                return True 
            elif matrix[row][mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return False 

        