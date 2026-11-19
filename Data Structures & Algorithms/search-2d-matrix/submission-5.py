class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = (len(matrix) * len(matrix[0])) -1


        legnth1 = len(matrix) -1
        length2 = len(matrix[0])-1
        
        row = 0
        l = 0
        r = 0
        

        while row < len(matrix):
            if matrix[row][0] <= target <= matrix[row][length2]:
                break
            row += 1

        if row ==len(matrix):
            return False


        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2 

            if target == matrix[row][mid]:
                return True

            elif target < matrix[row][mid]:
                right = mid -1
            
            else:
                left = mid +1
            
            
        
        return False

    