from copy import deepcopy

# Check if a queen can be placed on board[row][col]
def is_safe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    return True

# Main recursive function to solve N-Queens
def solve_n_queens(board, col, n):
    # Base case: If all queens are placed
    if col >= n:
        return [deepcopy(board)]
    
    solutions = []
    
    # Try placing queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            # Find all solutions
            solutions += solve_n_queens(board, col + 1, n)
            board[i][col] = 0  # backtrack
    
    return solutions

# Function to print a single solution
def print_one_solution(solution):
    if solution:
        print("One solution:")
        for row in solution:
            print(" ".join(str(cell) for cell in row))
    else:
        print("No solution found for the given input.")

# Function to count and print all solutions
def print_all_solutions(solutions, n):
    print(f"Total solutions: {len(solutions)}")
    
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in solution:
            print(" ".join(str(cell) for cell in row))
        print()

# Driver code
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))  # Number of queens and size of board (n x n)
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    while True:
        print("\nMenu:")
        print("1. Find and print one solution")
        print("2. Find and print all solutions")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            one_solution = solve_n_queens(board, 0, n)
            print_one_solution(one_solution[0])  # Print the first solution
        
        elif choice == "2":
            all_solutions = solve_n_queens(board, 0, n)
            print_all_solutions(all_solutions, n)
        
        elif choice == "3":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Time complexity: O(N!): The first queen has N placements, the second queen must not be in the same column as the first as well as at an oblique angle, so the second queen has N-1 possibilities
# Spatial Complexity: O(N): Need to use arrays to save information.
