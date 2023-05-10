import numpy as np
import matplotlib.pyplot as plt

def genereate_data(n):
    e_values = []
    for i in range(n):
        e= np.random.randn()
        e_values.append(e)
    return e_values

data = genereate_data(100)
plt.plot(data)
plt.show()