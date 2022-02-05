import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import colors

N = 100
init_co = [20, 50]

traced = 1
untraced = 0
maze = [traced, untraced]
colormap = colors.ListedColormap(["black","cyan"])
direction = [1, 2, 3, 4]

grid = np.zeros(N*N).reshape(N, N)
grid[init_co[0]][init_co[1]] = traced
x = init_co[0]
y = init_co[1]

def update(data):
    global grid, x, y
    stepCount = 0
    newGrid = grid.copy()

    stepChoice = np.random.choice(direction)
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
    print("Trying Step ",data," with ",stepCount," successful steps!")
    return [mat]

fig, ax = plt.subplots()
mat = plt.imshow(grid, cmap=colormap)
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
#ani.save('sarw.gif', writer='imagemagick', fps=60)
plt.show()
