import pandas as pd

df=pd.read("summary.csv", engine='python')

with open("README.md", "w") as md:
  df.to_markdown(buf=md, tablefmt="grid")
