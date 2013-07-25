import matplotlib.pyplot
import time

class Game:

    def __init__(self, initialLivingPoints, maxNumGames):
        
        self.currentLivingCells = {}
        self.futureLivingCells = {}
        self.relevantDeadCells = {}
        self.currentZombieCells = {}
        self.futureZombieCells = {}
        self.maxNumGames = maxNumGames
        self.numGamesPlayed = 0

        for p in initialLivingPoints:
            self.currentLivingCells[p] = 0

    def updateNumLivingNeighbors(self):

        for k in self.currentLivingCells.keys():
            for i in range(k[0] - 1,k[0] + 2):
                for j in range(k[1] - 1, k[1] + 2):
                    if (i,j) != k:
                        if self.currentLivingCells.has_key((i,j)):
                            self.currentLivingCells[(i,j)] = self.currentLivingCells[(i,j)] + 1 
                        # elif self.currentZombieCells.has_key((i,j)):
                        #    self.currentZombieCells[(i,j)] = self.currentZombieCells[(i,j)] + 1
                        elif self.relevantDeadCells.has_key((i,j)):
                            self.relevantDeadCells[(i,j)] = self.relevantDeadCells[(i,j)] + 1
                        else:
                            self.relevantDeadCells[(i,j)] = 1
        
        for k in self.currentZombieCells.keys():
            for i in range(k[0] - 1,k[0] + 2):
                for j in range(k[1] - 1, k[1] + 2):
                    if (i,j) != k:
                        if self.currentLivingCells.has_key((i,j)):
                            self.currentLivingCells[(i,j)] = self.currentLivingCells[(i,j)] + 1 
                        elif self.relevantDeadCells.has_key((i,j)):
                            self.relevantDeadCells[(i,j)] = self.relevantDeadCells[(i,j)] + 1
                        else:
                            self.relevantDeadCells[(i,j)] = 1


    def printBoard(self):
        
        f = matplotlib.pyplot.figure()
        
        for k in self.currentLivingCells.keys():
            matplotlib.pyplot.scatter(k[0], k[1], color = "b")
         
        for k in self.currentZombieCells.keys():
            matplotlib.pyplot.scatter(k[0], k[1], color = "r")

        f.show()
        time.sleep(0.4)
        # f.clear()

    def playGame(self):
        
        self.updateNumLivingNeighbors()

        for k,v in self.currentLivingCells.iteritems():
            if v == 2 or v == 3:
                if not self.currentZombieCells.has_key(k):
                    self.futureLivingCells[k] = 0
            elif v < 2 or v > 3:
                if not self.currentZombieCells.has_key(k):
                    self.futureZombieCells[k] = 0

        for k,v in self.relevantDeadCells.iteritems():
            if v == 3:
                if not self.currentZombieCells.has_key(k):
                    self.futureLivingCells[k] = 0

        self.printBoard()

        self.relevantDeadCells = {}
        self.currentLivingCells = self.futureLivingCells.copy()
        self.futureLivingCells = {}
        self.currentZombieCells = self.futureZombieCells.copy()
        self.futureZombieCells = {}
        self.numGamesPlayed += 1

        if self.numGamesPlayed < self.maxNumGames:
            self.playGame()

def main():

    # gameOfLife = Game([(1,1),(2,1),(2,2),(3,1),(3,2),(1,2),(4,1),(4,3)], 4)
    # gameOfLife = Game([(1,1),(2,1)], 20)
    # gameOfLife = Game([(1,1),(2,1),(3,1),(2,2)], 30)
    # gameOfLife = Game([(0,0),(1,0),(2,0),(2,1)], 20)
    # gameOfLife = Game([(0,0),(1,0),(2,0),(3,0),(4,0),(1,1),(2,1),(3,1),(2,2)], 30)
    # gameOfLife = Game([(0,0),(1,0)],5)

    gameOfLife = Game([(1,1),(2,1),(3,1)], 15)
    gameOfLife.playGame()

main()

