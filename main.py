import board as b

board_1 = b.Board(50, 50)
board_1.random_state()
board_1.render()

print()

board_2 = b.Board(10, 10)
board_2.render()

print()

board_3 = b.Board(30, 10)
board_3.random_state(0.1)
board_3.render()
