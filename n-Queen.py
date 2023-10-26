def solve_n_queens_one_solution(n):
    board = [[0] * n for _ in range(n)]

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False

            for j in range(n):
                if board[i][j] == 1 and (abs(row - i) == abs(col - j)):
                    return False

        return True

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                if solve(row + 1):
                    return True
                board[row][col] = 0

        return False

    if solve(0 ):
        return [" ".join("Q" if cell == 1 else "." for cell in row) for row in board]
    else:
        return []

if _name_ == "_main_":
    n = int(input("Enter the number of solve_n_queens_one_solution: ")) # Change this to the desired board size
    solution = solve_n_queens_one_solution(n)
    if solution:
        print(f"Found a solution for {n}-queens:")
        for row in solution:
            print(row)
    else:
        print(f"No solution found for {n}-queens.")
