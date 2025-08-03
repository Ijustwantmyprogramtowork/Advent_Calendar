import numpy as np


def count_MAS_in_X(grid):
    """
    Count the number of times 'MAS' (or 'SAM') appears in an 'X' pattern in the grid.

    An 'X' pattern is defined as both diagonals crossing through the center cell 
    forming valid 'MAS' or 'SAM' sequences.

    Parameters
    ----------
    grid : np.array
        The character matrix (grid of letters)

    Returns
    -------
    int
        Number of 'MAS' patterns forming an 'X'
    """
    # Diagonals (crossing at A) form:
    # Top-left to bottom-right:     x . .
    #                               . A .
    #                               . . x
    #
    # Bottom-left to top-right:     . . x
    #                               . A .
    #                               x . .
    
    count = 0
    valid_diags = {'MAS', 'SAM'}

    for i in range(grid.shape[1]):
        for j in range(grid.shape[0]):
            if grid[j][i] == 'A':
                if j >= 1 and j <= grid.shape[0] - 2 and i >= 1 and i <= grid.shape[1] - 2:
                    diag1 = grid[j-1][i-1] + grid[j][i] + grid[j+1][i+1]
                    diag2 = grid[j+1][i-1] + grid[j][i] + grid[j-1][i+1]
                    if diag1 in valid_diags and diag2 in valid_diags:
                        count += 1

    return count




def count_XMAS(grid):
    """
    Count the number of times 'XMAS' appears in the grid in any direction:
    vertical, horizontal, or diagonal (in all 8 directions).

    Parameters
    ----------
    grid : np.array
        The character matrix (grid of letters)

    Returns
    -------
    int
        Number of 'XMAS' occurrences in all directions
    """

    count = 0

    for i in range(grid.shape[1]):
        for j in range(grid.shape[0]):
            # Optimization: only continue if the current letter is 'X'
            if grid[j][i] == 'X':
                # Check in each of the 8 directions from current (j, i)
                
                # Vertical Up
                if j >= 3 and grid[j][i] + grid[j-1][i] + grid[j-2][i] + grid[j-3][i] == 'XMAS':
                    count += 1
                # Horizontal Left
                if i >= 3 and grid[j][i] + grid[j][i-1] + grid[j][i-2] + grid[j][i-3] == 'XMAS':
                    count += 1
                # Vertical Down
                if j <= grid.shape[0] - 4 and grid[j][i] + grid[j+1][i] + grid[j+2][i] + grid[j+3][i] == 'XMAS':
                    count += 1
                # Horizontal Right
                if i <= grid.shape[1] - 4 and grid[j][i] + grid[j][i+1] + grid[j][i+2] + grid[j][i+3] == 'XMAS':
                    count += 1
                # Diagonal Top-Left
                if j >= 3 and i >= 3 and grid[j][i] + grid[j-1][i-1] + grid[j-2][i-2] + grid[j-3][i-3] == 'XMAS':
                    count += 1
                # Diagonal Bottom-Right
                if j <= grid.shape[0] - 4 and i <= grid.shape[1] - 4 and grid[j][i] + grid[j+1][i+1] + grid[j+2][i+2] + grid[j+3][i+3] == 'XMAS':
                    count += 1
                # Diagonal Top-Right
                if j >= 3 and i <= grid.shape[1] - 4 and grid[j][i] + grid[j-1][i+1] + grid[j-2][i+2] + grid[j-3][i+3] == 'XMAS':
                    count += 1
                # Diagonal Bottom-Left
                if i >= 3 and j <= grid.shape[0] - 4 and grid[j][i] + grid[j+1][i-1] + grid[j+2][i-2] + grid[j+3][i-3] == 'XMAS':
                    count += 1

    return count


def main():
    """
    Main function that reads the input grid from a file, processes it,
    and prints the number of times 'XMAS' appears in all directions,
    as well as the number of 'MAS' patterns forming an X shape.
    """
    with open('input_day_4.txt', 'r') as file:
        data=file.read()
    #We need to create a matrice of the words for the grid search
    grid= np.array([list(line) for line in data.split('\n')])
    count_xmas=count_XMAS(grid)
    count_mas_in_x=count_MAS_in_X(grid)
    print(f"""
          __________________________________________________
          THERE IS {count_xmas} XMAS IN THE GRID 
          ___________________________________________
          THERE IS {count_mas_in_x} MAS IN X IN THE GRID """)
    
if __name__=="__main__":
    main()


