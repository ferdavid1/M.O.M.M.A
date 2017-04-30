import matplotlib as mpl
mpl.use('TKagg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
import pandas as pd
from geopy.geocoders import Nominatim
import re

['Washington', 'Wisconsin', 'West Virginia', 'Florida', 'Wyoming', 'New Hampshire', 'New Jersey', 'New Mexico', 'National', 'North Carolina', 'North Dakota', 'Nebraska', 'New York', 'Rhode Island', 'Nevada', 'Guam', 'Colorado', 'California', 'Georgia', 'Connecticut', 'Oklahoma', 'Ohio', 'Kansas', 'South Carolina', 'Kentucky', 'Oregon', 'South Dakota', 'Delaware', 'District of Columbia', 'Hawaii', 'Puerto Rico', 'Texas', 'Louisiana', 'Tennessee', 'Pennsylvania', 'Virginia', 'Virgin Islands', 'Alaska', 'Alabama', 'American Samoa', 'Arkansas', 'Vermont', 'Illinois', 'Indiana', 'Iowa', 'Arizona', 'Idaho', 'Maine', 'Maryland', 'Massachusetts', 'Utah', 'Missouri', 'Minnesota', 'Michigan', 'Montana', 'Northern Mariana Islands', 'Mississippi']
data = pd.read_csv('dataSets/NPL.csv', usecols=[2,3]).get_values()
print data[0]

fig = plt.figure()

blcLat=25.309974
blcLon=-128.068124
trcLat=49.592734
trcLon=-51.315958

m = Basemap(projection='stere',lat_0=39.5,lon_0=-98.35,resolution='l',llcrnrlon=blcLon,llcrnrlat=blcLat,urcrnrlon=trcLon,urcrnrlat=trcLat)
# draw coastlines.
m.drawcoastlines()
# draw parallels and meridians.
m.drawparallels(np.arange(-60.,90.,30.),labels=[1,0,0,0])

m.drawstates()
m.drawcountries()

lats=[x[0] for x in data]
lons=[x[1] for x in data]

m.scatter(lons,lats,latlon=True)
plt.show()