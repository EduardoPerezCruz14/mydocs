import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(x, y):
    return x ** 2

# Valores que toma (grafica) las 2 variables independientes
x = np.linspace(-50, 50, 50) # 
y = np.linspace(-50, 50, 50) # 

X, Y = np.meshgrid(x, y)
Z = f(X,Y)

fig = plt.figure(figsize = (10,7))

ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='Pastel2', edgecolor='none')

ax.set_title("Surface", fontsize = 13)
ax.set_xlabel('x', fontsize = 11)
ax.set_ylabel('y', fontsize = 11)
ax.set_zlabel('Z', fontsize = 10)

plt.show()