import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (np.sin(x))**2 + np.cos(x)

x = np.arange(-5.0, 5.0, 0.1)
plt.plot(x, f(x))
plt.show()



