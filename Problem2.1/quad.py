#from Euler import *
import numpy as np
import matplotlib.pyplot as plt
import pygame
import math

#CHANGE THIS FUNCTION TO CHANGE THE EQUATION OF MOTION
def f1(x, t):
    return np.array([x[1], -9.8]) # velocity

def f2(x, t):
    A = 1
    w = 1
    #−kx(t) = mx′′(t)
    return np.array([x[1], -1 * A * w**2 * math.sin(w * t)]) # velocity


t0 = 0 #keep
var = 0 #keep

def euler(f, x0, dt, N, order):
    x = np.zeros((N, 2))
    x[0] = x0
    for i in range(1, N):
        t_prev = t0 + dt * (i - 1)
        x[i] = x[i-1] + dt * f(x[i-1], t_prev)
    return x

for i in range(10):
    #YOU NEED THIS
    t0 = 0
    T = math.pi * 4 # Change this, dont make it too big or it will break
    N = int(input("Choose a N:")) #TEMP #make a slider for this
    dt = (T - t0) / N

    x0 = np.array([1.0, 0.0])  # Initial position = 1, velocity = 0

    t = np.linspace(t0, T, N) # array of time difference
    results = euler(f1, x0, dt, N)
    real_results =  f2# real results for harmonic oscillator

    # Plotting the results
    plt.figure(figsize=(12, 6))         
    plt.plot(t, results[:, 0], label='Position (x)')
    plt.plot(t, real_results[:, 0], label='Real Position (x)', linestyle='dashed')
    plt.title('Harmonic Oscillator: Position vs Time')
    plt.xlabel('Time (t)')  
    plt.ylabel('Position (x)')
    plt.grid()
    plt.legend()
    plt.show()