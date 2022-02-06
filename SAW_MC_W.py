import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import colors

N = 100  #set number of grids here!
init_co = [20, 50]  #set initial cordinates here!

traced = 1
untraced = 0
maze = [traced, untraced]
colormap = colors.ListedColormap(["black","cyan"]) #grid colors
direction = [1, 2, 3, 4]

grid = np.zeros(N*N).reshape(N, N)
grid[init_co[0]][init_co[1]] = traced
x = init_co[0]
y = init_co[1]
blockCount = 0
nos = 1000  #set number of steps here!

def update(data):
    global grid, x, y, blockCount
    stepCount = 0
    newGrid = grid.copy()

    #weight factors
    w1 = 4 - (grid[(x-1)%N][(y-1)%N] + grid[(x+1)%N][(y-1)%N] + grid[x][(y-2)%N])
    w2 = 4 - (grid[(x-1)%N][(y+1)%N] + grid[(x+1)%N][(y+1)%N] + grid[x][(y+2)%N])
    w3 = 4 - (grid[(x-1)%N][(y-1)%N] + grid[(x-1)%N][(y+1)%N] + grid[(x-2)%N][y])
    w4 = 4 - (grid[(x+1)%N][(y-1)%N] + grid[(x+1)%N][(y+1)%N] + grid[(x+2)%N][y])
    w = w1 + w2 + w3 + w4

    #neighbours
    pathBlock = grid[(x-1)%N][y] + grid[(x+1)%N][y] + grid[x][(y-1)%N] + grid[x][(y+1)%N]
    neighbour = pathBlock + grid[(x-1)%N][(y-1)%N] + grid[(x-1)%N][(y+1)%N] + grid[(x+1)%N][(y-1)%N] + grid[(x+1)%N][(y+1)%N] 
    if pathBlock == 4:
        newGrid = np.zeros(N*N).reshape(N, N)
        newGrid[init_co[0]][init_co[1]] = traced
        x = init_co[0]
        y = init_co[1]
        blockCount = 0
        print("resetting...")

    if blockCount < nos:
        stepChoice = np.random.choice(direction, 1, p=[w1/w, w2/w, w3/w, w4/w])
        if stepChoice == 1:
            if grid[x][(y-1)%N] == untraced:
                newGrid[x][(y-1)%N] = traced
                y = (y-1)%N

        elif stepChoice == 2:
            if grid[x][(y+1)%N] == untraced:
                newGrid[x][(y+1)%N] = traced
                y = (y+1)%N

        elif stepChoice == 3:
            if grid[(x-1)%N][y] == untraced:
                newGrid[(x-1)%N][y] = traced
                x = (x-1)%N

        else:
            if grid[(x+1)%N][y] == untraced:
                newGrid[(x+1)%N][y] = traced
                x = (x+1)%N
    
    mat.set_data(newGrid)
    grid = newGrid
    for i in range(N):
        for j in range(N):
            if grid[i][j] == traced:
                stepCount = stepCount+1
    blockCount = stepCount
    if stepCount == nos:
        print("Stopped with ",stepCount," successful steps!")
    else:
        print("Trying Step ",data," with ",stepCount," successful steps!")
    return [mat]

fig, ax = plt.subplots()
mat = plt.imshow(grid, cmap=colormap)
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
#ani.save('saw_mc_w.gif', writer='imagemagick', fps=60)
plt.show()
