import numpy as np
import matplotlib.pyplot as plt
import pygame
import math

t0 = 0 #keep
var = 0 #keep

def euler(f, x0, dt, N, order):
    x = np.zeros((N, 2))
    x[0] = x0
    for i in range(1, N):
        t_prev = t0 + dt * (i - 1)
        x[i] = x[i-1] + dt * f(x[i-1], t_prev)
    return x
