def solve(n):
    col = set()
    pos_diagonal = set()
    neg_diagonal = set()
    
    solution = []
    
    def backtrack(r):
        if r == n:
            print(solution)
            return
        else:
            for c in range(n):
                # Checking if the column is invalid
                if c in col or (r + c) in pos_diagonal or (r - c) in neg_diagonal:
                    continue
                
                # Column is valid
                # So we add position of queen to our solution list
                solution.append([r, c])
                # We also add col, pos_diagonal and neg_diagonal values to their respective sets
                col.add(c)
                pos_diagonal.add(r + c)
                neg_diagonal.add(r - c)
                
                # Then we try next row
                backtrack(r + 1)
                
                # This code will run after all rows have been tried
                # This clean up code to prepare for the next solution
                del solution[-1]
                pos_diagonal.remove(r + c)
                neg_diagonal.remove(r - c)
    
    backtrack(0)

solve(4)
                
            
