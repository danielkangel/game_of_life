import random as rand


def dead_state(width, height):
    """Creates a blank 2D array based on the passed width and height"""
    blank_row = [0] * width
    return [blank_row for num in range(0, height)]


def random_state(width, height, rand_control=0.5):
    """Populates a blank 2D array with cells"""

    # Build a blank board using dead_state
    blank_board = dead_state(width, height)

    # Populate the board with random amount of alive cells
    board = []
    for row in blank_board:
        cells = []
        for num in range(0, width):
            random_number = rand.random()
            if random_number >= rand_control:
                cell_state = 0
            else:
                cell_state = 1
            cells.append(cell_state)
        board.append(cells)
    return board
