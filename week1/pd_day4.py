import pandas as pd

#print(pd.__version__)

print("########### SERIES ############")

data = [12, 54, 30]

print("data[] = ", data)
serie1 = pd.Series(data)

print("Serie1 :")
print(serie1)

print()
data = [10.5, 54.2, 78.3, 5.8]

print("data[] = ", data)
serie2 = pd.Series(data)

print("Serie2 :")
print(serie2)


print("\n### LABELS ###\n")

data = [10.5, 54.2, 78.3, 5.8]

serie = pd.Series(data, index = ["a", "b", "c", "d"])

print("serie : ")
print(serie)
print("a = ", serie["a"])
print(f"c = {serie["c"]}")

serie["d"] = 20.7
print("serie : ")
print(serie)

"""
	> We can access to the serie using 
	* label : serie.loc[label]
	* index : serie.iloc[index]
"""

print()
calories = {"day 1" : 1200, "day 2" : 2300, "day 3" : 3000, "day 4" : 2600}

c = pd.Series(calories)

print("Calories :")
print(c)

print("Calories > 2000 : ")
print(c[c > 2000])



print("\n######## DATAFRAMES #########\n")


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#df = pd.DataFrame(data, )
df = pd.DataFrame(data, index = ["Week 1", "Week 2", "Week 3"]) # We can use indexes
print("DataFrame :")
print(df)
print("Week 1 :")
print(df.loc["Week 1"])

"""
	We can also acces to df using index 
	> df.iloc[0]
	
		#############################
		# calories    420	    #
		# duration     501	    #
		# Name: Day 1, dtype: int64 #
		#############################
"""

df["Weight"] = [62, 63, 61]
print(df)
print()
row = pd.DataFrame([{"calories" : 500, "duration" : 48, "Weight" : 63}],
		  index = ["Week 4"])

df = pd.concat([df, row])

print(df)


rows = pd.DataFrame([{"calories" : 500, "duration" : 48, "Weight" : 63},
		     {"calories" : 480, "duration" : 46, "Weight" : 62},
		     {"calories" : 410, "duration" : 42, "Weight" : 60}],
                  index = ["Week 5", "Week 6", "Week 7"]) 

df = pd.concat([df, rows])
print(df)
