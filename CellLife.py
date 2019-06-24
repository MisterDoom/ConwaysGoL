import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class CellLife:
    def __init__(self, gridSize=None, updateInterval=None, genRandom=None):
        # set grid size
        if gridSize == None:
            self.gridSize = 100
        else:
            self.gridSize = gridSize

        if updateInterval == None:
            self.updateInterval = 50
        else:
            self.updateInterval = updateInterval

        self.grid = np.array([])
        if genRandom == 1:
            self.grid = CellLife.randomGrid(0.2)
        else:
            self.grid = np.zeros(
                self.gridSize *
                self.gridSize).reshape(self.gridSize, self.gridSize)

    def startSimulation(self):
        self.fig, self.ax = plt.subplots()
        self.img = self.ax.imshow(self.grid, interpolation='nearest')
        self.ani = animation.FuncAnimation(self.fig, CellLife.update,
                                           fargs=(self.img, self.grid,
                                                  self.gridSize, ),
                                           frames=10,
                                           interval=self.updateInterval,
                                           save_count=50)

        """
        # set the output file
        if args.movfile:
            ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
        """
        plt.show()

    def addGlider(self, i, j):
        glider = np.array([[0,   0, 255],
                           [255,   0, 255],
                           [0, 255, 255]])
        self.grid[i:i + 3, j:j + 3] = glider

    def addGosperGun(self, i, j):
        gosperGun, size = CellLife.addPattern("GosperGun.txt")
        self.grid[i:i + size, j:j + size] = gosperGun

    @staticmethod
    def addPattern(inputFile):
        code = open(inputFile, "r").readlines()
        size = int(code[0].strip())
        pattern = np.zeros((size, size))

        for i in range(1, len(code)):
            for j in range(len(code[i].strip())):
                if code[i][j] == 'X':
                    pattern[i][j] = 255

        return pattern, size

    @staticmethod
    def update(frames, img, grid, gridSize):
        newGrid = grid.copy()
        for i in range(gridSize):
            for j in range(gridSize):
                total = int((grid[i, (j - 1) % gridSize] +
                             grid[i, (j + 1) % gridSize] +
                             grid[(i - 1) % gridSize, j] +
                             grid[(i + 1) % gridSize, j] +
                             grid[(i - 1) % gridSize, (j - 1) % gridSize] +
                             grid[(i - 1) % gridSize, (j + 1) % gridSize] +
                             grid[(i + 1) % gridSize, (j - 1) % gridSize] +
                             grid[(i + 1) % gridSize, (j + 1) % gridSize]) / 255)
                # Apply Conway's rules
                if grid[i, j] == 255:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = 0
                else:
                    if total == 3:
                        newGrid[i, j] = 255

        # update data
        img.set_data(newGrid)
        grid[:] = newGrid[:]
        return img,

    @staticmethod
    def randomGrid(aliveCellProb, gridSize):
        if aliveCellProb < 0 or aliveCellProb > 1:
            aliveCellProb = 0.2

        return np.random.choice([0, 255], gridSize * gridSize,
                                p=[1 - aliveCellProb, aliveCellProb]).reshape(gridSize,
                                                                              gridSize)
