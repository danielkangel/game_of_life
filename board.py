import random as rand


class Board:
    def __init__(self, width=10, height=10):
        """Creates a blank 2D array based on the passed width and height"""
        self.width = width
        self.height = height
        self.board = [[0 for val in range(0, width)] for val in range(0, height)]

    def random_state(self, rand_control=0.5):
        """Updates the board with a new 2D array of cells"""

        # Populate the board with random amount of alive cells
        for row in range(0, self.height):
            for index in range(0, self.width):
                random_number = rand.random()
                if random_number >= rand_control:
                    cell_state = 0
                else:
                    cell_state = 1
                self.board[row][index] = cell_state

    def render(self):
        """Formats the board state and prints it to the console"""
        formatted_board = ""
        for num in range(0, (self.width + 1) + 1):
            formatted_board += '-'
        for row in self.board:
            formatted_board += '\n|'
            for num in range(0, self.width):
                if row[num]:
                    formatted_board += '\u25A0'
                else:
                    formatted_board += ' '
            formatted_board += '|'
        formatted_board += '\n'
        for num in range(0, self.width + 2):
            formatted_board += '-'
        print(formatted_board)

    def check_cell(self, location):
        """Scans surrounding cells to check whether or not the given cell should die or not"""
        row = location[0]
        index = location[1]
        surrounding_cells = 0

        # Loops through each surrounding element and checks the amount of surrounding living cells
        for scan_row in range((row - 1), (row + 1) + 1):
            for scan_index in range((index - 1), (index + 1) + 1):
                if (scan_index == index) and (scan_row == row): continue
                if self.board[scan_row % self.height][scan_index % self.width] == 1:
                    surrounding_cells += 1

        # Returns the correct status based on the surrounding cells
        if self.board[row][index] == 1:
            if surrounding_cells < 2:
                return 0
            elif surrounding_cells <= 3:
                return 1
            else:
                return 0
        else:
            if surrounding_cells == 3:
                return 1
            else:
                return 0

    def next_state(self):
        """Checks each element and updates the board"""
        new_board = [[0 for x in range(0, self.width)] for y in range(0, self.height)]
        for row in range(0, self.height):
            for index in range(0, self.width):
                if self.check_cell((row, index)):
                    new_board[row][index] = 1
        self.board = new_board[:][:]
