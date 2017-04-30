import matplotlib as mpl
mpl.use('TKagg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm



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

plt.show()