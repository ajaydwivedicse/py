import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df)
record1 = np.array(['Name', 'Hindi', 'English', 'Computer', 'Mathematics', 'Science'])
record2 = np.array(['Ajay Dwivedi', 99, 72, 96, 89, 92])
record3 = np.array(['Amit Chauhan', 100, 100, 79, 99, 100])
record4 = np.array(["Sharad Chauhan", 100, 100, 100, 100, 100])
df = pd.DataFrame([record1, record2, record3, record4])
print(df)
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])
s3 = pd.Series([9, 10, 11, 12])
s4 = pd.Series([13, 14, 15, 16])
df1 = pd.DataFrame([s1, s2, s3, s4], columns = ['P', 'Q', 'R', 'S'])
print(df1)