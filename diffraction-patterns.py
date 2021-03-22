import numpy as np
import matplotlib.pyplot as plt

a = 1

def aperture(x):
    if np.abs(x) <= a/2:
        return 1
    else:
        return 0

def gaussian(x):
    return np.exp(-x**2/(0.00004*a))


x_in = np.linspace(-10, 10, 10000)

E_in = np.asarray([gaussian(i) for i in x_in])

E_out = np.fft.fft(E_in)
X_out = np.fft.fftfreq(len(x_in), 100)

X_out, E_out = zip(*sorted(zip(X_out, E_out)))

I_out = np.power(np.abs(E_out), 2)

plt.plot(X_out, I_out)
plt.show()
