#https://pandas.pydata.org/docs/user_guide/dsintro.html

import pandas as pd

# print(pd.__version__)

##________________________________________________________________________________________________________________________


#Series (1-dimensional labled array that can hold any data type )

# data = [100,101,102]
# series = pd.Series(data,index=['a','b','c']) #here index is specified if not start from 0,1,2...n
# print(series)

# dt2 = {'a':100,'b':102,'c':103} #here key will be index if index is not specified
# s2 = pd.Series(dt2)
# print(s2) 

##________________________________________________________________________________________________________________________

#Dataframe 

# data = {
#     "name":["sam","messi","ronaldo"],
#     "Age" : [19,30,20]
# }

# df = pd.DataFrame(data,index = ["std1","std2","std3"])

#loc locate using lable ,iloc locate using index

# print(df.loc["std1"])
# print('---------------')
# print(df.iloc[0])

#add new column 
# df["reg_no"] = [1234,1235,1236]

#add new row we need to concat new record to existing df)
# new_row = pd.DataFrame([{"name":"vijay","Age":53,"reg_no":1237}],index = "std4")

# df = pd.concat([df,new_row]) #concat create new df not change existing one
# print(df)

##________________________________________________________________________________________________________________________

#Reading csv file

df = pd.read_csv("pd.csv",index_col = "Name") # index_col helps to search using the col Name
# df = pd.read_json("fname.json") remaing all same

# print(df.to_string())
# print(type(df.to_string()))

#Selecting by col
# print(df["Name"]) #1 col
# print(df[["Name","Height","Weight"]]) # mul col

#Selecting by row
# print(df.iloc[0])
# print(df.loc["Pidgey"])
# print(df.iloc[0:4])
# print(df.loc["Pikachu",["Height","Weight"]])
# print(df.iloc[:4:2])

# pokemon = input("Enter a pokemon name to search: ").capitalize()
# try:
#     print(df.loc[pokemon])
# except:
#     print("Sorrry we can't fetch details of ",pokemon)

##________________________________________________________________________________________________________________________

# Filtering (keeping the row that matcches)

# tall_poki = df[df["Height"] >= 2]
# print(tall_poki)

# legendary_poki = df[df["Legendary"] >0]
# print(legendary_poki)

# water_poki = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
# print(water_poki)

##________________________________________________________________________________________________________________________

# Aggregate function (Reduce a set of values into a single value, often used with group by)

# avg_weight = df["Weight"].mean()
# print(avg_weight)


# print(df["Height"].min())
# print(df["Height"].max())

# t1 = df[df["Type1"] == "Water"]
# print(t1["Legendary"].sum()) #this tell how many legendary in type1 

# Group By

# df = df.groupby("Type1") # i groupby using type1

# print(df["Height"].mean())
# print(df["Legendary"].sum()) #tells no:of legendary in each type

##________________________________________________________________________________________________________________________

# Cleaning data

# droping irrelavent columns
# df = df.drop(columns=["Type2","No","Legendary"])

# Missing values
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2":"None"})

# Fixing inconsistance 
# df["Type1"] = df["Type1"].replace({"Water":"Pani"})

# Standerdize txt
# df["Type1"] = df["Type1"].str.lower()
# print(df.to_string()) #print(df) won't written complete df

# Fix data type
# df["Legendary"] = df["Legendary"].astype(bool)

# Remove duplicate
# df = df.drop_duplicates()

print(df.to_string)

##________________________________________________________________________________________________________________________










