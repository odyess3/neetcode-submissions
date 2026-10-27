from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    hge = []
    big = 0
    
    for i in range(len(nested_arr)):
    
        for j in range(len(nested_arr[i])):

            if big < nested_arr[i][j]:
                big = max(big,nested_arr[i][j])

        
        hge.append(big)    
        
    
    return hge



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
