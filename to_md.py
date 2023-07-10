import pandas as pd

df=pd.read_csv("summary.csv", engine='python')

with open("README.md", "w") as md:
  df.to_markdown(buf=md, tablefmt="grid")
