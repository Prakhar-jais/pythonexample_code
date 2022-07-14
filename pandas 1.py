import pandas as pd
import numpy as np

dict1={
    "name":["prakhar","sam","nandu","cary"],
    "marks":[92,78,70,80],
    "city":["indore","pune","bhopal","delhi"]
}
df=pd.DataFrame(dict1)
print(df)



print(df.describe())
sheet=pd.read_csv("panda_sheet.csv")
print(sheet)

#to change any data by indexes
sheet["income"][0]=500000
sheet["income"][2]=300000
sheet.index=[1,2,3,4]
print(sheet)

#to make series of data
values=pd.Series(np.random.rand(34))
print(values)

#to make frames of data
newframe=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
print(newframe)

#newfeme is contain what type of data
print(newframe.dtypes)

#changing the data
newframe[0][1]="PRAKHAR"
newframe[0][0]="peelu"
print(newframe)
print(newframe.dtypes)

newframe[0][1]=0.02
newframe[0][0]=0.04
print(newframe)

#to convert all data in a numpy array
print(newframe.to_numpy())

#to make transpose of row n column
print(newframe.T)

newframe.head(5)
#use this function to set the values again
newframe.loc[0,0]=654
print(newframe)


#to delete any column
newframe=newframe.drop(4,axis=1)
print(newframe.head())

#to get a part of data frame use loc function
part1_frame=newframe.loc[[0,1],[0,1]]
print(part1_frame)

#to get all columns or rows
part2_frame=newframe.loc[:,[0,1]]  #same can be done for rows too i.e colon on right side
print(part2_frame)

#if i want particular values only in particular interval than also i use loc function
newframe=newframe.loc[(newframe[1]<0.3) & (newframe[2]>0.1)]
print(newframe)

#to get the particular value by using iloc function  syntax:.iloc[row,col]
value=newframe.iloc[3,3]
print(value)