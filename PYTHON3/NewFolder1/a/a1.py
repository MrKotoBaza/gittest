import matplotlib.pyplot as plt
import numpy as np
from math import sin

x = np.linspace(-10, 20, 50)

y = [sin(i) for i in x]

y0 = [0 for i in x]


plt.plot(x, y, x, y0)






plt.show()