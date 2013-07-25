GameOfLife
==========

Conway's Game of Life

Attached are three basic versions of Conway's Game of Life.  I am using Python 2.7.5 and matplotlib 1.2.1.

Here is a brief description:

1) GameLife.py is the Basic Version of the Game of Life.  Live cells must have 2 or 3 living neighbors to live.  Dead cells come back to life with exactly 3 living neighbors.
2) GameLifeZombie.py adds a variation to the rules explained above.  Here Live cells with < 2 or > 3 living neighbors are marked for death but it takes two generations of the game for them to die.  I am calling these "marked for death" cells zombies.  The live cells are marked in blue and the zombies are marked in red.
3) gLifeZombie is a different implementation of 2) without using named tuples.

I am using a dictionary to store currentLivingCells, futureLivingCells, and relevantDeadCells.  The keys are in the form of (x,y) coordinates and I used named tuples which are much like an immutable struct and give me the ability to access a Point p's values as p.x and p.y instead of p[0] and p[1].  I used another named tuple "Cell" for the values in the dictionary.  A Cell has a boolean value isAlive, numLivingNeighbors and another boolean isZombie.

Each living cell is a living neighbor to the eight cells around it.  Therefore, I iterated through the currentLivingCell dictionary and pushed the neighbor count outwards from each currentLivingCell.  This process determines which cells are relevantDeadCells and determines their neighbor count at the same time.  It also determines the neighbor count for each currentLivingCell.

Known Issues: 
1) Getting the plot into the foreground when the application starts up.
2) Redrawing the existing plot rather than starting up a new plot with each generation.


