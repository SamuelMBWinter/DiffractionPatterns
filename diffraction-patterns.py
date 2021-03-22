import numpy as np
from scipy.fft import fft2, fftfreq, fftshift
import matplotlib.pyplot as plt

# a in cm
a = 0.05
E_0 = 1

# Transmission Functions

## Square aperture of width a centred at the origin
def aperture_sq(x, y):
    if np.abs(x) <= a/2 and np.abs(y) <= a/2:
        return 1
    else:
        return 0

## Sqare rod of width a centred at the origin
def rod_sq(x, y):
    return 1 - aperture_sq(x, y)

## Gaussian Transmission
def gaussian_sq(x, y):
    return np.exp(-(x/a)**2) * np.exp(-(y/a)**2)

# Grid in the plan of the aperture
x_in = np.linspace(-2, 2, 100)
y_in = np.linspace(-2, 2, 100)
x_in, y_in = np.meshgrid(x_in, y_in)
grid_in = np.vstack((x_in.flatten(), y_in.flatten())).T

# The Electric field in the plane of the aperture
E_in = np.array([E_0 * gaussian_sq(g[0], g[1]) for g in grid_in ])
E_in = np.reshape(E_in, (len(x_in), len(y_in)))

# The output frequencies
X_out = fftshift(fftfreq(len(x_in), 1000))
Y_out = fftshift(fftfreq(len(y_in), 1000))

E_out = fftshift(fft2(E_in))
I_out = np.power(np.abs(E_out), 2)

plt.pcolormesh(X_out, Y_out, I_out, shading='nearest')
plt.colorbar()
plt.show()
