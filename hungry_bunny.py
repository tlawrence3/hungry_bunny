import numpy as np

def is_even(x):
    """
    helper function to determine if matrix dims are even
    """
    return x%2 == 0

def get_centers(shape): #Used to determine center cell(s) of garden
    """
    Returns row and col coord(s) for center cell(s)
    """
    dim_row = shape[0]
    dim_col = shape[1]
    row_coords = []
    col_coords = []

    #grab row center coord(s): will return one value if row dim is odd, or two if even
    if is_even(dim_row):
        row_coords.append(dim_row // 2)
        row_coords.append((dim_row // 2) -1)
    else:
        row_coords.append(dim_row // 2)
    #grab col center coord(s); will return one value if col dim is odd, or two if even
    if is_even(dim_col):
        col_coords.append(dim_col  // 2)
        col_coords.append((dim_col // 2) - 1)
    else:
        col_coords.append(dim_col // 2)

    return row_coords, col_coords


def get_max_center_cell(garden, row_coords, col_coords):
    """
    Given a set of coords for center cell(s) return cell with max carrots
    """
    current_max = 0
    start_row_coord = 0
    start_col_coord = 0
    for row_coord in row_coords:
        for col_coord in col_coords:
            if garden[row_coord, col_coord] > current_max:
                current_max = garden[row_coord, col_coord]
                start_row_coord = row_coord
                start_col_coord = col_coord

    return (start_row_coord, start_col_coord)

def get_adj_coords(garden_shape, current_position):
    """
    Helper function to return coords of all adjacent cells given current position
    """
    adj = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, garden_shape[0])  # X bounds
            rangeY = range(0, garden_shape[1])  # Y bounds

            (newX, newY) = (current_position[0]+dx, current_position[1]+dy)  # adjacent cell

            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))

    return adj

def event_loop(garden, starting_position):
    """
    Hungry bunny logic!
    Will loop until bunny has no adjacent cells with carrots at which point it
    will go to sleep
    """
    carrots_consumed = 0
    current_position = starting_position
    while True:
        carrots_consumed += garden[current_position] #track num carrots bunny consumed
        garden[current_position] = 0
        adj_cells = get_adj_coords(garden.shape, current_position)
        max_carrots_potential_move = 0
        max_carrots_potential_move_coords = (0,0)
        for potential_move in adj_cells: #search adjacent cells for carrots
            if garden[potential_move] > max_carrots_potential_move:
                max_carrots_potential_move = garden[potential_move]
                max_carrots_potential_move_coords = potential_move
        if max_carrots_potential_move == 0:
            break #Bunny goes to sleep
        else:
            current_position = max_carrots_potential_move_coords # bunny found adjacent cell with carrots
    return carrots_consumed

def main(garden):

    row_coords, col_coords = get_centers(garden.shape) #get coords center cell(s)
    starting_pos = get_max_center_cell(garden, row_coords, col_coords) #get coords of max center cell
    num_carrots_consumed = event_loop(garden, starting_pos) #hungry bunny logic and tracking
    print(num_carrots_consumed) #print num carrots consumed

if __name__ == "__main__": #call main function with garden matrix
    garden = np.array([[5,7,8,6,3], [0,0,7,0,4], [4,6,3,4,9], [3,1,0,5,8]]) #input garden
    main(garden)
