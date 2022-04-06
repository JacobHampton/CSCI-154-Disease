import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

tick = 1

class People():
    status = 1
    def __init__(self, status):
        self.contagious_ticks = 20
        #status = normal(1), not infected(2), recovered(3)
        self.status = 1

def plot_grid(grid):
    rows, cols = (20, 20)
    ax = plt.gca()
    major_ticks = np.arange(1, 21, 1)
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)
    for i in range(cols):
        for j in range(rows):
            if grid[i][j] == 0:
                rect = plt.Rectangle([i,j], 1, 1, facecolor = 'white', edgecolor = 'white')
                ax.add_patch(rect)
            if grid[i][j] == 1:
                rect = plt.Rectangle([i,j], 1, 1, facecolor = 'blue', edgecolor = 'blue')
                ax.add_patch(rect)
            if grid[i][j] == 2:
                rect = plt.Rectangle([i,j], 1, 1, facecolor = 'red', edgecolor = 'red')
                ax.add_patch(rect)
            if grid[i][j] == 3:
                rect = plt.Rectangle([i,j], 1, 1, facecolor = 'green', edgecolor = 'green')
                ax.add_patch(rect)

    ax.grid(which='both')
    plt.grid(True)

    #plt.show()
    plt.ion()
    plt.show(block=False)
    plt.pause(.5)
    plt.close()
    
def infect(grid):
    global tick
    tick += 1

    i = np.argwhere(grid == 2)
    print(i)
    for x in range(len(i)):
        x_pos = i[x][0]
        y_pos = i[x][1]
        if grid[x_pos][y_pos] == 2:
            if x_pos < 19:
                if grid[x_pos+1][y_pos] == 1:
                    grid[x_pos+1][y_pos] = 2
            if x_pos > 0:
                if grid[x_pos-1][y_pos] == 1:
                    grid[x_pos-1][y_pos] = 2
            if y_pos < 19:
                if grid[x_pos][y_pos+1] == 1:
                    grid[x_pos][y_pos+1] = 2
            if y_pos > 0:
                if grid[x_pos][y_pos-1] == 1:
                    grid[x_pos][y_pos-1] = 2
    return grid


def simulate():

    rows, cols = (20, 20)
    not_infected = People(1)
    infected = People(2)
    recovered = People(3)
    rand_row = random.randrange(20)
    rand_col = random.randrange(20)
    # 0 = empty(white), 1 = not infected, 2 = infected, 3 = recovered

    grid2 = [[0 for i in range(cols)] for j in range(rows)]
    grid = np.array(grid2)
    #populate infected person
    #grid[rand_col][rand_row] = People(2)
    grid[rand_col][rand_row] = 2
    grid2[rand_col][rand_row] = 2

    #populate not infected
    num = 1
    while num < 240:
        x, y = random.randrange(20), random.randrange(20)
        if grid[x][y] == 0:
            grid[x][y] = 1
            num += 1

    for i in range(cols):
        for j in range(rows):
            while grid[i][j] == 1:
                plot_grid(grid)

                #infect
                grid = infect(grid) 
                np.random.shuffle(grid)

    print(tick)
    


simulate()


    
