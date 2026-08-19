print("hunhar4916")
print("it's just a flesh wound!")

import pandas as pd
import matplotlib.pyplot as plt


students = ["Hunter", "Dan", "Warner", "John", "Matt",
            "Mateo", "Tom", "Tim", "Todd", "Keith"]

subjects = ["Math", "History"]
index = pd.MultiIndex.from_product([students, subjects], names=["Student", "Subject"])


#Creating dataframe with hardcoded grades

grades = [
    92, 88,
    75, 81,
    67, 92,
    87, 88,
    73, 97,
    79, 83,
    89, 96,
    99, 84,
    87, 100,
    89, 76,]

df = pd.DataFrame(grades, index=index, columns=["Grades"])

#Displaying the DataFrame
print(df)

#Collapsing students into an average
subject_avg = df.groupby(level="Subject").mean()
print(subject_avg)

#Displaying the bar graph
subject_avg.plot(kind="bar", legend=False, color="pink")
plt.title("Average Grade by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Grade")
plt.tight_layout()
plt.show()
















    
