import pandas as pd
df=pd.read_csv("fdny-firehouse-listing.csv")
df3=df.groupby(df["Borough"])

# print(df["FacilityName"])
# print(df3.size())
name=df[["Borough","Postcode"]][df["Borough"]=="Manhattan"]

name=name.drop(name.tail(1).index)
print(name)