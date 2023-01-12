import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd 

def plot_depth(path, depth):
    print("plot depth")
    depth = np.rot90(depth)
    depth = np.rot90(depth)
    depth = np.rot90(depth)
    #depth = np.transpose(depth)
    #print(depth)
    x_max=len(depth)
    y_max=len(depth[0])
    print(x_max)
    print(y_max)
    borders = np.zeros((x_max, y_max))
    for x in range(5, y_max-5):
        for y in range(5, x_max-5):
            #print(x,y)
            #print(depth[y][x])
            difference = abs(depth[y][x]-depth[y][x-5])+abs(depth[y][x]-depth[y][x+5])+abs(depth[y][x]-depth[y][x-5])


    depth_flat = []
    for item in depth:
        for subitem in item:
            depth_flat.append(subitem)
    #print(len(depth))
    #print(len(depth[0]))
    print(np.shape(depth_flat))
    #print(type(depth))
    pd.DataFrame(depth).to_csv("depth.csv")
    
    y_max=len(depth[0])
    x_max=len(depth)

    x = []
    y = []
    for i in range(x_max):
        x.append([i] * y_max)
        y.append(list(range(0, y_max)))
    x_flat = []
    for item in x:
        for subitem in item:
            x_flat.append(subitem)
    y_flat = []
    for item in y:
        for subitem in item:
            y_flat.append(subitem)
    rand = []
    for i in range(len(x_flat)):
        rand.append(random.randint(1,100))
    #print(x_flat)
    #print(y_flat)
    #print(rand)
    print(len(x_flat))
    print(len(y_flat))
    #print(len(rand))
    # Create a scatterplot
    plt.scatter(x_flat, y_flat, c=depth_flat, s=0.01)
    plt.savefig('scatter.png')

    d = pd.DataFrame(np.zeros((y_max, x_max)))
    for x in range(5, x_max-5):
        for y in range(5, y_max-5):
            left = abs(depth[x][y] - depth[x-5][y])
            right = abs(depth[x][y] - depth[x+5][y])
            up = abs(depth[x][y] - depth[x][y-5])
            down = abs(depth[x][y] - depth[x][y+5])
            d[x][y] = left + right + up + down
    #d = np.rot90(d)
    max_d = d.max().max()*0.2
    print(max_d)
    d[d < max_d] = 0
    d[d > max_d] = 1
    d = d.transpose()
    print(d.shape)
    pd.DataFrame(d).to_csv("d.csv")
    d_flat = d.to_numpy().flatten()
    plt.clf()
    plt.scatter(x_flat, y_flat, c=d_flat, s=0.01)
    plt.savefig('scatter_d.png')
    
    #for x in range(5, x_max-5):
    #    for y in range(5, y_max-5):
    #        if d[x][y] < 
    return