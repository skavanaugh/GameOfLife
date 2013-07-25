import collections
import matplotlib.pyplot
import time

namedtuple = collections.namedtuple

class Game:

    Point = namedtuple("Point", "x y")
    Cell = namedtuple("Cell", "isAlive numLivingNeighbors")

    defaultLivingCell = Cell(isAlive = True, numLivingNeighbors = 0)
    defaultDeadCell = Cell(isAlive = False, numLivingNeighbors = 1)

    def __init__(self, initialLivingPoints, maxNumGames):
        
        self.currentLivingCells = {}
        self.futureLivingCells = {}
        self.relevantDeadCells = {}
        self.maxNumGames = maxNumGames
        self.numGamesPlayed = 0

        for p in initialLivingPoints:
            self.currentLivingCells[Game.Point(p[0],p[1])] = Game.defaultLivingCell

    def updateNumLivingNeighbors(self):

        for k in self.currentLivingCells.keys():
            for i in range(k.x - 1,k.x + 2):
                for j in range(k.y - 1, k.y + 2):
                    if (i,j) != k:
                        if self.currentLivingCells.has_key((i,j)):
                            self.currentLivingCells[Game.Point(i,j)] = Game.Cell(isAlive = True, 
                                    numLivingNeighbors = self.currentLivingCells[Game.Point(i,j)].numLivingNeighbors + 1)
                        elif self.relevantDeadCells.has_key((i,j)):
                            self.relevantDeadCells[Game.Point(i,j)] = Game.Cell(isAlive = False, 
                                    numLivingNeighbors = self.relevantDeadCells[Game.Point(i,j)].numLivingNeighbors + 1)
                        else:
                            self.relevantDeadCells[Game.Point(i,j)] = Game.defaultDeadCell


    def printBoard(self):
        
        f = matplotlib.pyplot.figure()
        # ax = f.add_subplot()

        for k in self.currentLivingCells.keys():
            matplotlib.pyplot.scatter(k.x, k.y)

        f.show()
        time.sleep(0.5)
        # f.clear()

    def playGame(self):
        
        self.updateNumLivingNeighbors()

        for k in self.currentLivingCells.keys():
            if self.currentLivingCells[k].numLivingNeighbors == 2 or self.currentLivingCells[k].numLivingNeighbors == 3:
                self.futureLivingCells[k] = Game.defaultLivingCell

        for k in self.relevantDeadCells.keys():
            if self.relevantDeadCells[k].numLivingNeighbors == 3:
                self.futureLivingCells[k] = Game.defaultLivingCell

        self.printBoard()

        self.relevantDeadCells = {}
        self.currentLivingCells = self.futureLivingCells.copy()
        self.futureLivingCells = {}
        self.numGamesPlayed += 1

        if self.numGamesPlayed < self.maxNumGames:
            self.playGame()

def main():

    # gameOfLife = Game([(1,1),(2,1),(2,2),(3,1),(3,2),(1,2),(4,1),(4,3)], 30)   
    # gameOfLife = Game([(1,0),(2,0),(3,0),(4,0),(2,1),(3,1)], 30)

    gameOfLife = Game([(1,1),(2,1),(3,1),(4,1),(5,1),(2,2),(3,2),(4,2),(3,3)], 13)
    gameOfLife.playGame()

main()

