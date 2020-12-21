import random as rand


class Board:
    def __init__(self, width, height):
        """Creates a blank 2D array based on the passed width and height"""
        blank_row = [0] * width
        self.width = width
        self.height = height
        self.board = [blank_row for num in range(0, height)]

    def random_state(self, rand_control=0.5):
        """Updates the board with a new 2D array of cells"""

        # Populate the board with random amount of alive cells
        for index in range(0, self.height):
            cells = []
            for num in range(0, self.width):
                random_number = rand.random()
                if random_number >= rand_control:
                    cell_state = 0
                else:
                    cell_state = 1
                cells.append(cell_state)
            self.board[index] = cells

    def render(self):
        """Formats the board state and prints it to the console"""
        formatted_board = ""
        for num in range(0, self.width + 2):
            formatted_board += '-'
        for row in self.board:
            formatted_board += '\n|'
            for num in range(0, self.width):
                if row[num]:
                    formatted_board += '#'
                else:
                    formatted_board += ' '
            formatted_board += '|'
        formatted_board += '\n'
        for num in range(0, self.width + 2):
            formatted_board += '-'
        print(formatted_board)
