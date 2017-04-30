import pandas as pd

data = pd.read_csv('dataSets/pop_density.csv', usecols=[0,10,11,21,22,32,33])

data = pd.DataFrame(data)

print(data[0])