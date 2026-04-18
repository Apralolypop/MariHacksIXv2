#from Euler import * #This works as a template
import numpy as np
import matplotlib.pyplot as plt
import pygame
import math

#CHANGE THIS FUNCTION TO CHANGE THE EQUATION OF MOTION
def f1(x, t):
    #x''(t) = 2
    return np.array([x[1], 2]) # velocity

def f2(t):
    return t**2 # real results for exponential growth


def euler(f, x0, dt, N, order):
    x = np.zeros((N, 2))
    x[0] = x0
    var = 0
    for i in range(1, N):
        t_prev = t0 + dt * (i - 1)
        x[i] = x[i-1] + dt * f(x[i-1], t_prev)
        #print(x[i][0], f2(t_prev)[0]) dont print, it will make it slow
        var += (x[i][0] - f2(t_prev)) ** 2
    return x,  math.sqrt(var / N)

for i in range(10):
    #YOU NEED THIS
    t0 = 0
    T = 10 # Change this, dont make it too big or it will break
    N = int(input("Choose a N:")) #TEMP #make a slider for this
    dt = (T - t0) / N

    x0 = np.array([0.0, 0.0])  # Initial position = 1, velocity = 0

    t = np.linspace(t0, T, N) # array of time difference
    results, sd = euler(f1, x0, dt, N, 1)
    real_results = np.array([f2(ti) for ti in t]) # real results for exponential growth

    # Plotting the results
    plt.figure(figsize=(12, 6))         
    plt.plot(t, results[:, 0], label='Position (x)')
    plt.plot(t, real_results[:], label='Real Position (x)', linestyle='dashed')
    print(f"Standard Deviation: {sd:.10f}")
    plt.title(f'Harmonic Oscillator: Position vs Time (sd = {sd:.20f})')
    plt.xlabel('Time (t)')  
    plt.ylabel('Position (x)')
    plt.grid()
    plt.legend()
    plt.show()