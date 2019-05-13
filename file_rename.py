import os

ragaFiles = os.listdir("data")

for j,raga in enumerate(ragaFiles):
    os.system(f"mv data/{raga} renamed_data/{j+1}.png")
