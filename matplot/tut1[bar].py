import matplotlib.pyplot as plt
import numpy as np

xaxis=np.array(["c","c++","java","python"])
c=['r','g','b','y']
yaxis=np.array([45,65,88,93])
plt.xlabel("Programmings",fontsize=15)
plt.ylabel("Rates")
plt.bar(xaxis,yaxis,color=c,width=0.2,edgecolor='r',linewidth=1,label="shivay")
plt.bar(xaxis,yaxis,color=c,width=0.2,edgecolor='r',linewidth=1,label="shivay2")
plt.legend()
plt.title("Testing123")
plt.show()