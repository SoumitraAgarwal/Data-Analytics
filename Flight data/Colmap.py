import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import calmap

data = pd.read_csv("Results.csv")
all_days = pd.date_range('1/1/2015', periods=365, freq='D')
all_days = np.array(all_days.to_pydatetime(), dtype=np.datetime64)

events = pd.Series(data["Values"].values, index=all_days)
calmap.yearplot(events, year=2015, cmap='YlGn')
plt.show()