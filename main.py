import board as b
from os import system
from time import sleep

board_1 = b.Board(100, 50)
board_1.random_state()
while True:
    board_1.render()
    board_1.next_state()
    sleep(0.025)
    system('cls')
