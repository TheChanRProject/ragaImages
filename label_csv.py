import pandas as pd
import os

columnDict = {}

fileList = os.listdir("data")
print(len(fileList))

columnDict['file_name'] = fileList

print(columnDict)

labels = []

for i in range(202):
    labels.append("bhairav")

for i in range(183):
    labels.append("bhup")

for i in range(137):
    labels.append("des")

for i in range(258):
    labels.append("yaman")

print(len(labels))

columnDict['raga'] = labels

df = pd.DataFrame.from_dict(columnDict)

df.to_csv("csv/miml_labels_2.csv")

frame = pd.read_csv("csv/miml_labels_2.csv")
