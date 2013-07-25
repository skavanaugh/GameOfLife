import collections
import matplotlib.pyplot
import time

namedtuple = collections.namedtuple

class Game:

    Point = namedtuple("Point", "x y")
    Cell = namedtuple("Cell", "isAlive numLivingNeighbors isZombie")

    defaultLivingCell = Cell(isAlive = True, numLivingNeighbors = 0, isZombie = False)
    defaultDeadCell = Cell(isAlive = False, numLivingNeighbors = 1, isZombie = False)
    defaultZombieCell = Cell(isAlive = True, numLivingNeighbors = 0, isZombie = True)

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
                                    numLivingNeighbors = self.currentLivingCells[Game.Point(i,j)].numLivingNeighbors + 1,
                                    isZombie = self.currentLivingCells[Game.Point(i,j)].isZombie)
                        elif self.relevantDeadCells.has_key((i,j)):
                            self.relevantDeadCells[Game.Point(i,j)] = Game.Cell(isAlive = False, 
                                    numLivingNeighbors = self.relevantDeadCells[Game.Point(i,j)].numLivingNeighbors + 1,
                                    isZombie = self.relevantDeadCells[Game.Point(i,j)].isZombie)
                        else:
                            self.relevantDeadCells[Game.Point(i,j)] = Game.defaultDeadCell


    def printBoard(self):
        f = matplotlib.pyplot.figure()
        
        for k in self.currentLivingCells.keys():
            if self.currentLivingCells[k].isZombie:
                matplotlib.pyplot.scatter(k.x, k.y, color = "r")
            else:
                matplotlib.pyplot.scatter(k.x, k.y, color = "b")

        # pylab.ylim([-12,15])
        # pylab.xlim([-12,15])
        f.show()
        time.sleep(0.4)
        # f.clear()

    def playGame(self):
        
        self.updateNumLivingNeighbors()

        for k in self.currentLivingCells.keys():
            if self.currentLivingCells[k].numLivingNeighbors == 2 or self.currentLivingCells[k].numLivingNeighbors == 3:
                if not self.currentLivingCells[k].isZombie:
                    self.futureLivingCells[k] = Game.defaultLivingCell
            elif self.currentLivingCells[k].numLivingNeighbors < 2 or self.currentLivingCells[k].numLivingNeighbors > 3:
                if not self.currentLivingCells[k].isZombie:
                    self.futureLivingCells[k] = Game.defaultZombieCell

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

    # gameOfLife = Game([(1,1),(2,1),(2,2),(3,1),(3,2),(1,2),(4,1),(4,3)], 50)
    # gameOfLife = Game([(1,1),(2,1),(3,1)], 15)
    # gameOfLife = Game([(1,1),(2,1),(3,1),(2,2)], 30)
    # gameOfLife = Game([(0,0),(1,0),(2,0),(2,1)], 20)
    
    gameOfLife = Game([(0,0),(1,0),(2,0),(3,0),(4,0),(1,1),(2,1),(3,1),(2,2)], 30)
    gameOfLife.playGame()

main()

