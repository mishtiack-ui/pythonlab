
import pandas as pd

data = {"Name": ["Aman", "Rohit"], "Age": [20, 24]}

temp = pd.DataFrame(data)

temp.to_json("data.json", indent=6)

temp.to_csv("data.csv", index=False)

temp = pd.read_csv("data.csv")

print(temp)
