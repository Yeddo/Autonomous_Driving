import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    
    new_beliefs = [] # Initialize list
    
    #
    # TODO - implement this in part 2
    #
    
    # Get height and width of grid
    height = len(grid)
    width = len(grid[0])
    total = 0 # To keep track of the sum of the new belief values.
    
    # Loop each row in grid.
    for i in range(height):
        row = [] # List to store belief values for this row.
        # Column loop.
        for j in range(width):
            # Check is sensor measurement matches the color of the current cell.
            hit = (color == grid[i][j])
            # Calculate the new belief value for this cell based on sensor probability
            new_belief = beliefs[i][j] * ((1-hit) * p_miss + hit * p_hit)
            # Add new belief value to total.
            total += new_belief
            # Append new belief value to the row.
            row.append(new_belief)
        # Append the row of belief values to the new_beliefs list.
        new_beliefs.append(row)
    
    # Normalize the belief values so they sum to 1
    for i in range(height):
        for j in range(width):
            new_beliefs[i][j] /= total
    
    return new_beliefs # Return updated beliefs.

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    #print(len(new_G),len(new_G[0]))
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % (height)
            new_j = (j + dx ) % (width)
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)