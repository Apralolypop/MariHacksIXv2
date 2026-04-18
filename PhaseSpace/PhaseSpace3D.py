import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

L = 1
g = 9.8

t0 = 0
T = 100
N = 5000

def f1(x, t):
    return np.array([x[1], -g / L * math.sin(x[0]), x[2]]) # x[1] is velocity, x[2] is time, x[0] is position

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
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)
ax.plot(results[:, 0], results[:, 1], results[:, 2], color='red', linewidth=0.5)
ax.set_title(f'PhaseSpace representation of a pendulum (L={L:.2f}, g={g:.2f})')
ax.set_xlabel('0(t)')
ax.set_ylabel("0'(t)")
ax.set_zlabel('time')


ax_l = plt.axes((0.2, 0.05, 0.65, 0.03))
ax_g = plt.axes((0.2, 0.15, 0.65, 0.03))

slider_l = Slider(ax_l, 'L', 0.1, 10.0, valinit=L, valstep=0.1)
slider_g = Slider(ax_g, 'g', 0.1, 20.0, valinit=g, valstep=0.1)

def update(val):
    global L, g
    L = slider_l.val
    g = slider_g.val
    results = euler(f1, x0, dt, N)
    ax.clear()
    ax.plot(results[:, 0], results[:, 1], results[:, 2], color='red', linewidth=0.5)
    ax.set_title(f'PhaseSpace representation of a pendulum (L={L:.2f}, g={g:.2f})')
    ax.set_xlabel('0(t)')
    ax.set_ylabel("0'(t)")
    ax.set_zlabel('time')
    fig.canvas.draw_idle()

slider_l.on_changed(update)
slider_g.on_changed(update)
plt.show()