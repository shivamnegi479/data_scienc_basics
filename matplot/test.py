import numpy as np

# ar=np.arange(5,10)
# print(type(ar))

li=[]
for i in range(1,51):
    li.append(i)
# print(li)
li2=list(filter(lambda x:str(x).endswith('1'),li))
print(li2)

