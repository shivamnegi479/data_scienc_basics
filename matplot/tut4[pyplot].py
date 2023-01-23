import matplotlib.pyplot as plt
import numpy as np

x=[34,55,33,22]
y=["C","JS","PY","GO"]
expl=[0.2,0,0,0.1]
plt.pie(x,labels=y,explode=expl,autopct="%0.1f%%",startangle=120,wedgeprops={"edgecolor":"k",'linewidth': 0.5, 'linestyle': 'solid', 'antialiased': True})
plt.show()