class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == '.': 
                    continue
                
                box = (row // 3, col // 3)
                row_mark = (item, 'row', row)
                col_mark = (item, 'col', col)
                box_mark = (item, 'box', box)

                if row_mark in seen or col_mark in seen or box_mark in seen:
                    return False

                seen[row_mark] = True
                seen[col_mark] = True
                seen[box_mark] = True
        return True

                        #update seen - add item w row, col, box id
                        # row++, col++
                        # row/col/box id match in seen:
                        #   return False
                        #else: return True
