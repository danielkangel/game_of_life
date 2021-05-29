import random as rand
import pygame

# set the alive and dead cell colors
alive_cell = (0, 0, 0)
dead_cell = (236, 236, 236)


class Board:
    def __init__(self, width=10, height=10):
        """Creates a blank 2D array based on the passed width and height"""
        self.width = width
        self.height = height
        self.board = [[dead_cell for val in range(0, width)] for val in range(0, height)]

    def random_state(self, rand_control=0.5):
        """Updates the board with a new 2D array of cells"""

        # Populate the board with random amount of alive cells
        for row in range(0, self.height):
            for index in range(0, self.width):
                random_number = rand.random()
                if random_number >= rand_control:
                    cell_state = dead_cell
                else:
                    cell_state = alive_cell
                self.board[row][index] = cell_state

    def render(self, surface, cell_size):
        """Formats the board state and prints it to the console"""
        y = 0
        for r in self.board:
            x = 0
            for c in r:
                pygame.draw.rect(surface, c, (x, y+2*cell_size, cell_size - 1, cell_size - 1))
                x += cell_size
            y += cell_size

    def check_cell(self, location):
        """Scans surrounding cells to check whether or not the given cell should die or not"""
        row = location[0]
        index = location[1]
        surrounding_cells = 0

        # Loops through each surrounding element and checks the amount of surrounding living cells
        for scan_row in range((row - 1), (row + 1) + 1):
            for scan_index in range((index - 1), (index + 1) + 1):
                if (scan_index == index) and (scan_row == row):
                    continue
                if (scan_row >= self.height) or (scan_row < 0):
                    continue
                if (scan_index >= self.width) or (scan_index < 0):
                    continue

                if self.board[scan_row][scan_index] == alive_cell:
                    surrounding_cells += 1

        # Returns the correct status based on the surrounding cells
        if self.board[row][index] == alive_cell:
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
        new_board = [[dead_cell for x in range(0, self.width)] for y in range(0, self.height)]
        for row in range(0, self.height):
            for index in range(0, self.width):
                if self.check_cell((row, index)):
                    new_board[row][index] = alive_cell
        self.board = new_board[:][:]

    def clear_board(self):
        self.board = [[dead_cell for val in range(0, self.width)] for val in range(0, self.height)]

    def swap_cell(self, x, y):
        if self.board[y][x] == alive_cell:
            self.board[y][x] = dead_cell
        else:
            self.board[y][x] = alive_cell
