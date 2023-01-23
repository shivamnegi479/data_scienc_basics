import numpy as np
import matplotlib.pyplot as plt

x=["a","b","c","d"]
color=['r','g','b','m']
size=[100,200,50,200]
y=[12,324,45,56]
plt.scatter(x,y,color=color,s=size)
plt.colorbar()
plt.xlabel("Demo")
plt.show()