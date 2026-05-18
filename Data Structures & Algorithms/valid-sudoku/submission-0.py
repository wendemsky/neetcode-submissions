class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_dict = {}
        
        box_hashset = [0] * 9
        
        
        for i in range(len(board)):
            # print("row: ", i, end="\n")
            rows_hashset = [0] * 9
            cols_hashset = [0] * 9
            for j in range(len(board)):
                # check the rows
                if board[i][j] != '.':
                    if rows_hashset[int(board[i][j])-1] == 1:
                        return False
                    else:
                        rows_hashset[int(board[i][j])-1] = 1
    
                # check the cols
                if board[j][i] != '.':
                    if cols_hashset[int(board[j][i])-1] == 1:
                        return False
                    else:
                        cols_hashset[int(board[j][i])-1] = 1
            
                # print(rows_hashset)
                # print(cols_hashset)

                # check the 3*3 boxes, key is int(index/3) value is a hashset
                if board[i][j] != '.':
                    key = (int(i/3), int(j/3))
                    if key not in box_dict:
                        box_dict[key] = [0] * 9
                        box_dict[key][int(board[i][j])-1] = 1
                    else:
                        if box_dict[key][int(board[i][j])-1] == 1:
                            return False
                        else:
                            box_dict[key][int(board[i][j])-1] = 1
        return True            

                
                
                
        
        