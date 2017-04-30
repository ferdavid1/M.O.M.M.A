import pandas as pd

data = pd.read_csv('dataSets/pop_density.csv', usecols=[0,10,11,21,22,32,33])

data = data.get_values()
data = [list(d) for d in data]

US_general = data[3]
States = data[4:len(data)]

print(States[3])
print(US_general)

print([d for d in data if d[0] == 'Arkansas']) #example of how to index by name.