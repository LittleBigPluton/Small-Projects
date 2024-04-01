#!/usr/bin/python3/
import math
import matplotlib.pyplot as plt
import numpy as np
i = np.linspace(-10,10)
j = np.linspace(-10,10)
M,N = np.meshgrid(i,j)
z = np.sqrt(M**2 + N**2)
cp = plt.contourf(M,N,z)
plt.colorbar(cp)
plt.show()
