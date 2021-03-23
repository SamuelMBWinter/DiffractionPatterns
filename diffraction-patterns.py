import numpy as np
from scipy.fft import fft2, fftfreq, fftshift
import matplotlib.pyplot as plt

# Dimensions in cm
a = 0.01
d = 0.04

# Electric field intensity
E_0 = 1

# Transmission Functions
## Square aperture of width a centred at the origin
def aperture_sq(x, y):
    a = 0.01
    if np.abs(x) <= a/2 and np.abs(y) <= a/2:
        return 1
    else:
        return 0

## Sqare rod of width a centred at the origin
### Note that this yields a hug bright peak in the centre (delta function)
def rod_sq(x, y):
    return 1 - aperture_sq(x, y)

## Gaussian Transmission
def gaussian_sq(x, y):
    return np.exp(-(x/a)**2) * np.exp(-(y/a)**2)

##double aperture
def double_sq(x, y):
    a = 0.01
    d = 0.06
    if np.abs(x) > (d - a) and np.abs(x) < (d + a) and np.abs(y) < a/2:
        return 1
    else:
        return 0

def triple_sq(x, y):
    a = 0.01
    d = 0.06
    if (np.abs(x) < a or (np.abs(x) > (d - a) and np.abs(x) < (d + a))) and np.abs(y) < a/2:
        return 1
    else:
        return 0


def apertur_cir(x, y):
    a = 0.02
    if np.abs(x**2 + y**2) < (a/2)**2:
        return 1 
    else:
        return 0

def ring(x, y):
    a = 0.02
    d = 0.1
    if np.abs(x**2 + y**2) < (a+d)**2 and np.abs(x**2 + y**2) < (a+d)**2:
        return 1
    else:
        return 0


    

# Grid in the plan of the aperture
x_in = np.linspace(-2, 2, 1000)
y_in = np.linspace(-2, 2, 1000)
x_in, y_in = np.meshgrid(x_in, y_in)
grid_in = np.vstack((x_in.flatten(), y_in.flatten())).T

# The Electric field in the plane of the aperture
E_in = np.array([E_0 * triple_sq(g[0], g[1]) for g in grid_in ])
E_in = np.reshape(E_in, (len(x_in), len(y_in)))

# The output frequencies
X_out = fftshift(fftfreq(len(x_in), 1000))
Y_out = fftshift(fftfreq(len(y_in), 1000))

E_out = fftshift(fft2(E_in))
I_out = np.power(np.abs(E_out), 2)

plt.pcolormesh(X_out, Y_out, I_out, shading='nearest', cmap='gray')
plt.colorbar()
plt.show()
