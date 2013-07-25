GameOfLife
==========

Conway's Game of Life

Attached are three basic versions of Conway's Game of Life.  I am using Python 2.7.5 and matplotlib 1.2.1.

Here is a brief description:

1) GameLife.py is the Basic Version of the Game of Life.  Live cells must have 2 or 3 living neighbors to live.  Dead cells come back to life with exactly 3 living neighbors.
2) GameLifeZombie.py adds a variation to the rules explained above.  Here Live cells with < 2 or > 3 living neighbors are marked for death but it takes two generations of the game for them to die.  I am calling these "marked for death" cells zombies.  The live cells are marked in blue and the zombies are marked in red.
3)gLifeZombie is a different implementation of 2) without using named tuples.

Known Issues: 
1) Getting the plot into the foreground when the application starts up.
2) Redrawing the existing plot rather than starting up a new plot with each generation.


