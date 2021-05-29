# Conway's Game of Life
![Conway's Demo Program](./assets/demo/conway's_demo.gif)

# Rules
Conway's Game of Life is a zero-player game created by John Horton Conway. 
During the game, cells interact with their eight neighboring cells based on a set of rules.

1. Any alive cell with **two** or **three** neighboring cell remains alive.
2. Any dead cell with **exactly three** alive neighbors becomes alive.
3. Any other cell will die or remain dead.

For more information, please see this [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) page.

# Requirements
PyGame is required for this project. Please use `pip install -r requirements.txt` to install PyGame 2.0.1.