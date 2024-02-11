import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

data = pd.read_csv("climate_change.csv")

sns.lmplot(x="Year", y="Temp", data=data)
plt.show()












