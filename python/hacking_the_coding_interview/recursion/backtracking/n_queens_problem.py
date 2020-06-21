
def is_valid_move(proposed_row, proposed_col, solution):
  # we need to check with all queens
  # in current solution
  for i in range(0, proposed_row):
    old_row = i
    old_col = solution[i]

    diagonal_offset = proposed_row - old_row
    if (old_col == proposed_col or 
         old_col == proposed_col - diagonal_offset or 
         old_col == proposed_col + diagonal_offset):
      return False

  return True

def solve_n_queens_rec(n, solution, row, results):
  if row == n:
    results.append(copy.deepcopy(solution))
    return

  for i in range(0, n):    
    if is_valid_move(row, i, solution):
      solution[row] = i
      solve_n_queens_rec(n, solution, row + 1, results)

def solve_n_queens(n, results):
  solution = [-1] * n
  solve_n_queens_rec(n, solution, 0, results)
  return len(results)

results = []  
n = 4
res = solve_n_queens(n, results)
print("Total solutions count for " + str(n) + " queens: " + str(res));