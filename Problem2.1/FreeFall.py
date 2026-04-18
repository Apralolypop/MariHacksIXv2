#from Euler import * #This works as a template
import numpy as np
import matplotlib.pyplot as plt
import pygame
import math

#CHANGE THIS FUNCTION TO CHANGE THE EQUATION OF MOTION
def f1(x, t):
    k = 1
    m = 1
    #d = vo * t - 9.8 * t**2 / 2
    return np.array([x[1], -9.8]) # velocity for vo = 0

def f2(t):
    return np.array([1 - 4.9 * t**2, -9.8 * t])



def euler(f, x0, dt, N, order):
    x = np.zeros((N, 2))
    x[0] = x0
    var = 0
    for i in range(1, N):
        t_curr = t0 + dt * (i)
        x[i] = x[i-1] + dt * f(x[i-1], t_curr)
        #print(x[i][0], f2(t_prev)[0]) dont print, it will make it slow
        var += (x[i][0] - f2(t_curr)[0]) ** 2
    return x,  math.sqrt(var / N)

for i in range(10):
    #YOU NEED THIS
    t0 = 0
    T = 1 #Change this, dont make it too big or it will break
    N = int(input("Choose a N:")) #TEMP #make a slider for this
    dt = (T - t0) / N

    x0 = np.array([1.0, 0.0])  # Initial position = 1, velocity = 0

    t = np.linspace(t0, T, N) # array of time difference
    results, sd = euler(f1, x0, dt, N, 1)
    real_results = np.array([[ 1 -4.9 * ti**2, -9.8 * ti ] for ti in t])
 

    # Plotting the results
    plt.figure(figsize=(12, 6))         
    plt.plot(t, results[:, 0], label='Position (x)')
    plt.plot(t, real_results[:, 0], label='Real Position (x)', linestyle='dashed')
    print(f"Standard Deviation: {sd:.10f}")
    plt.title(f'Harmonic Oscillator: Position vs Time (sd = {sd:.20f})')
    plt.xlabel('Time (t)')  
    plt.ylabel('Position (x)')
    plt.grid()
    plt.legend()
    plt.show()