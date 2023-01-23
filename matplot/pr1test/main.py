import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# Index(['Age', 'Attrition', 'Department', 'DistanceFromHome', 'Education',
#        'EducationField', 'EnvironmentSatisfaction', 'JobSatisfaction',   
#        'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked',
#        'WorkLifeBalance', 'YearsAtCompany'],
#       dtype='object')


df=pd.read_csv('IBM Attrition Data.csv')
married=df[df['MaritalStatus']=="Married"]
unmarried=df[df['MaritalStatus']!="Married"]
devorce=df[df['MaritalStatus']=="Divorced"]
single=df[df['MaritalStatus']=="Single"]

m=(len(married))
un=(len(unmarried))
s=len(single)
d=len(devorce)
# print(m,un)
x=np.array(m)
y=np.array(un)
da=np.array(d)
sa=np.array(s)

status=[x,y,da,sa]
z=["Merried","Unmarried","single","devorced"]
color=['r','m','g','b']
plt.title("Marital Status of Employee",fontsize=15)
plt.bar(z,status,width=0.2,color=color,label="Empoyee of Comapny")
plt.xlabel("Empoyess Status")
plt.ylabel("Number of employee")
plt.legend()

plt.show()
# print(type(x))