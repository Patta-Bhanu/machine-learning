import pandas as pd
data=[100,120,200]
series=pd.Series(data,index=["a","b","c"],dtype='f')
series.loc["a"]+=1000
print(series[series>200])