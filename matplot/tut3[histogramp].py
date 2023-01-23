import numpy as np
import matplotlib.pyplot as plt

x=np.random.randint(20,30,(50))
# y=["C","cpp","js","ss"]
x=[10,20,40,45]
# y=[10,20,23,30,30]
color=['r','g','b','m','y']
plt.hist(x,histtype='bar',color='r',edgecolor='b')
plt.title("Histogram")
plt.show()
# print(x)