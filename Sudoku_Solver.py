# Sudoku Solver using Backtracking

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(row)

# Function to find an empty cell in the grid
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:  # 0 means empty
                return i, j
    return None

# Check if a number can be placed at grid[row][col]
def is_valid(grid, num, row, col):
    # Check row
    if num in grid[row]:
        return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3×3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

# Backtracking solver
def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True  # Puzzle solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, num, row, col):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0  # Undo (backtrack)

    return False


# Example Sudoku Puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Solving Sudoku...\n")

if solve_sudoku(sudoku_grid):
    print("Sudoku solved successfully!\n")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
