# import pandas as pd
# df=pd.read_csv("fdny-firehouse-listing.csv")
# print(df.columns)
# print(df[['FacilityName', 'FacilityAddress', 'Borough']])
# # print(df["FacilityName"][(df['Borough']=='Manhattan') and (df['FacilityAddress']==' 42 South Street' )])
# print(df['FacilityName'][(df['Borough']=='Manhattan') & (df['FacilityAddress']=='42 South Street')]) 


# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')

# import pandas as  pd
# df=pd.read_csv('titanic.csv')

# print(df.loc[:,"Name":"Fare"])
# print(df[df['Survived']==1])
# cabin=df[(df['Pclass'].isin([2, 3]) & (df['Survived']==1) & (df['Age']<18))]
# cabin=cabin[cabin["Cabin"].notna()]
# print(cabin)
# na=cabin[cabin["Cabin"].notna()]
# print(na.shape)
# print(df.loc[df['Age']<18,'Name'])


import pandas as pd
ser1=pd.Series([1,2,4,5,"shivam","negi"])
print(ser1)