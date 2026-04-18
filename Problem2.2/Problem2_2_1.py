#from Euler import * #This works as a template
import numpy as np
import matplotlib.pyplot as plt
import pygame
import math

#CHANGE THIS FUNCTION TO CHANGE THE EQUATION OF MOTION
def f1(x, t):
    k = 1
    #x'(t) = cx(t)
    return np.array([k * x[0]]) # x[1] is velocity, x[0] is position

def f2(t):
    return np.array([math.exp(t)]) # real results for exponential growth



def euler(f, x0, dt, N, order):
    x = np.zeros((N, 2))

    x[0] = x0
    var = 0
    for i in range(1, N):
        t_prev = t0 + dt * (i - 1)
        x[i] = x[i-1] + dt * f(x[i-1], t_prev)
        #print(x[i][0], f2(t_prev)[0]) dont print, it will make it slow
        var += (x[i][0] - f2(t_prev)[0]) ** 2
    return x,  math.sqrt(var / N)

itr = 1000
t0 = 0
T = 300 # Change this, dont make it too big or it will break (max around 700 for exponential growth)

var_graph = np.zeros(itr)
for i in range(1, itr):
    #YOU NEED THIS

    N = i #int(input("Choose a N:")) #TEMP #make a slider for this
    dt = (T - t0) / N

    x0 = np.array([1.0, 0.0])  # Initial position = 1, velocity = 0

    t = np.linspace(t0, T, N) # array of time difference
    results, sd = euler(f1, x0, dt, N, 1)
    var_graph[i] = sd
    #real_results = np.array([math.exp(ti) for ti in t]) # real results for exponential growth

    # Plotting the results
    '''plt.figure(figsize=(12, 6))         
    plt.plot(t, results[:], label='Position (x)')
    plt.plot(t, real_results[:], label='Real Position (x)', linestyle='dashed')
    print(f"Standard Deviation: {sd:.10f}")
    plt.title(f'Harmonic Oscillator: Position vs Time (sd = {sd:.20f})')
    plt.xlabel('Time (t)')  
    plt.ylabel('Position (x)')
    plt.grid()
    plt.legend()
    plt.show()'''
plt.plot(range(1, itr), var_graph[1:])
plt.title('Standard Deviation vs N for exponential function from 0 to 100 t')
plt.xlabel('N')
plt.ylabel('Standard Deviation')
plt.grid()
plt.show()