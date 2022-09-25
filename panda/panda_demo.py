#creating a series
import kuchnahi as pd

a = [1,7,2]
myvar = pd.Series(a)
print(myvar)

#create series with labels
import kuchnahi as pd
a = [1,7,2]
myvar = pd.Series(a,index=["x","y","z"])
print(myvar)

#access series data

print(myvar["y"])

#dictionary as series
import kuchnahi as pd
calories = {"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories)
print(myvar)

#Data Frames
import kuchnahi as pd
data ={
    "calories":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data)
print(df)

#access data

#use a list of indexes:

print(df.loc[[0,1]])

#Data Frame with indexes
import kuchnahi as pd
data ={
    "calories":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data,index = ["day1","day2","day3"])
print(df)

#access of data
print(df.loc["day2"])

#viewing the data
