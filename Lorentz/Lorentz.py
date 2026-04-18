#from Euler import * #This works as a template
import numpy as np
import matplotlib.pyplot as plt
import pygame
import math

#Variables
sig = 28
rho = 28
beta = 2.66666666666

#CHANGE THIS FUNCTION TO CHANGE THE EQUATION OF MOTION #x[1] is velocity (y), x[0] is position (x), x[2] is z
def f1(x, t):
    return np.array([sig * (x[1] - x[0]), x[0] * (rho - x[2]), -beta * x[2] + x[0] * x[1]]) # velocity

def euler(f, x0, dt, N):
    x = np.zeros((N, 3)) # 3 dimensions for x, y, z
    x[0] = x0
    #var = 0
    for i in range(1, N):
        t_curr = t0 + dt * (i)
        x[i] = x[i-1] + dt * f(x[i-1], t_curr)
        #print(x[i][0], f2(t_prev)[0]) dont print, it will make it slow
        #var += (x[i][0] - f2(t_prev)[0]) ** 2
    return x#,  math.sqrt(var / N)

for i in range(10):
    #YOU NEED THIS
    t0 = 0
    T = 100 # Change this, dont make it too big or it will break
    N = 100000 #TEMP #make a slider for this
    #sig = float(input("Choose a sigma:")) #TEMP #make a slider for this
    #rho = float(input("Choose a rho:")) #TEMP #make a slider for this
    #beta = float(input("Choose a beta:")) #TEMP #make a slider for this
    dt = (T - t0) / N

    x0 = np.array([2.0, 1.0, 0.0])  # Z = 2, Y = 1, X = 0

    t = np.linspace(t0, T, N) # array of time difference
    results = euler(f1, x0, dt, N)

    # Plotting the results

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(results[:, 0], results[:, 1], results[:, 2], color='red', linewidth=0.5)
    ax.scatter(results[0, 0], results[0, 1], results[0, 2], color='green')

    ax.set_title(f'Lorenz Function (sig={sig}, rho={rho}, beta={beta})')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
    