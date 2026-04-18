import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

sig = 10.0
rho = 28.0
beta = 8/3

t0 = 0
T = 40
N = 10000

def f1(x, t):
    return np.array([sig * (x[1] - x[0]), x[0] * (rho - x[2]), -beta * x[2] + x[0] * x[1]])

def euler(f, x0, dt, N):
    x = np.zeros((N, 3))
    x[0] = x0
    for i in range(1, N):
        t_curr = t0 + dt * i
        x[i] = x[i-1] + dt * f(x[i-1], t_curr)
    return x

dt = (T - t0) / N
x0 = np.array([2.0, 1.0, 0.0])
results = euler(f1, x0, dt, N)

fig = plt.figure()
plt.subplots_adjust(bottom=0.25)
ax = fig.add_subplot(111, projection='3d')
ax.plot(results[:, 0], results[:, 1], results[:, 2], color='red', linewidth=0.5)
ax.scatter(results[0, 0], results[0, 1], results[0, 2], color='green')
ax.set_title(f'Lorenz (sig={sig}, rho={rho}, beta={beta:.2f})')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax_sig  = plt.axes((0.2, 0.10, 0.65, 0.03))
ax_rho  = plt.axes((0.2, 0.05, 0.65, 0.03))
ax_beta = plt.axes((0.2, 0.15, 0.65, 0.03))
slider_sig = Slider(ax_sig, 'sigma', 0.1, 50.0, valinit=sig, valstep=0.1)
slider_rho = Slider(ax_rho, 'rho',   0.1, 50.0, valinit=rho, valstep=0.1)
slider_beta = Slider(ax_beta, 'beta', 0.1, 10.0, valinit=beta, valstep=0.1)   

def update(val):
    global sig, rho, beta
    sig = slider_sig.val
    rho = slider_rho.val
    beta = slider_beta.val
    results = euler(f1, x0, dt, N)
    ax.clear()
    ax.plot(results[:, 0], results[:, 1], results[:, 2], color='red', linewidth=0.5)
    ax.scatter(results[0, 0], results[0, 1], results[0, 2], color='green')
    ax.set_title(f'Lorenz Attractor (sig={sig}, rho={rho}, beta={beta:.2f})')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.canvas.draw_idle()

slider_sig.on_changed(update)
slider_rho.on_changed(update)
slider_beta.on_changed(update)
plt.show()