import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import calmap

data 		= pd.read_csv("Results.csv")
all_days 	= pd.date_range('1/1/2015', periods=365, freq='D')
all_days 	= np.array(all_days.to_pydatetime(), dtype=np.datetime64)

events 	= pd.Series(data["Values"].values, index=all_days)
fig 	= plt.figure(figsize=(20,8))
ax 		= fig.add_subplot(111)
cax 	= calmap.yearplot(events, year=2015, ax=ax, cmap='rainbow')
fig.colorbar(cax.get_children()[1], ax=cax, orientation='horizontal')
plt.show()