"""
import pandas as pd
df=pd.read_csv('homeprices2.csv')
# print(df)
df['m_town']=df['town']
df['w_town']=df['town']
df['r_town']=df['town']
def repacler(x,c_name):
    if str(x)=='monroe township' and c_name=='m_town':
        x=str(x).replace(str(x),'1')
        return int(x)
    else:
        
        if str(x)=='west windsor' and c_name=='w_town':
            x=str(x).replace(str(x),'1')
            return int(x)
        else:
            
            if str(x)=='robinsville' and c_name=='r_town':
                x=str(x).replace(str(x),'1')
                return int(x)
            else:
                return 0

df['m_town']=df['m_town'].apply(lambda x:repacler(x,'m_town'))
df['w_town']=df['w_town'].apply(lambda x:repacler(x,'w_town'))
df['r_town']=df['r_town'].apply(lambda x:repacler(x,'r_town'))
print(df)

"""

# e=[3,4,5,6,7,87,4]
# print(e[-2:])


# class a():
#     name="shivam"
#     age=26
#     def get(self):
#         self.name="test"
#         self.age=34

# aa=a()
# bb=a()
# print(aa.name)
# print(aa.get())
# print(aa.name)
# print(bb.name)


a=list(set([161 ,182, 161, 154, 176, 170, 167, 171, 170, 174 ]))

print(sum(a)/len(a))
