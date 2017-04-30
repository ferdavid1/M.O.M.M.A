import matplotlib as mpl
mpl.use('TKagg')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
import pandas as pd
import re
from matplotlib.patches import Polygon

columns = [0,10,11,12,13,14,15,16,17,18,19,20,21,22,32,33]
ind = 0
for index in columns[3:13]:
	data = pd.read_csv('dataSets/pop_density.csv', usecols=columns)

	data = data.get_values()
	data = [list(d) for d in data]

	US_general = data[3]
	stateDens = data[4:len(data)]



	states_names=['Washington', 'Wisconsin', 'West Virginia', 'Florida', 'Wyoming', 'New Hampshire', 'New Jersey', 'New Mexico', 'National', 'North Carolina', 'North Dakota', 'Nebraska', 'New York', 'Rhode Island', 'Nevada', 'Guam', 'Colorado', 'California', 'Georgia', 'Connecticut', 'Oklahoma', 'Ohio', 'Kansas', 'South Carolina', 'Kentucky', 'Oregon', 'South Dakota', 'Delaware', 'District of Columbia', 'Hawaii', 'Puerto Rico', 'Texas', 'Louisiana', 'Tennessee', 'Pennsylvania', 'Virginia', 'Virgin Islands', 'Alaska', 'Alabama', 'American Samoa', 'Arkansas', 'Vermont', 'Illinois', 'Indiana', 'Iowa', 'Arizona', 'Idaho', 'Maine', 'Maryland', 'Massachusetts', 'Utah', 'Missouri', 'Minnesota', 'Michigan', 'Montana', 'Northern Mariana Islands', 'Mississippi']
	data = pd.read_csv('dataSets/NPL.csv', usecols=[2,3]).get_values()


	fig = plt.figure()

	blcLat=20.309974
	blcLon=-128.068124
	trcLat=49.592734
	trcLon=-51.315958

	m = Basemap(projection='stere',lat_0=39.5,lon_0=-98.35,resolution='l',llcrnrlon=blcLon,llcrnrlat=blcLat,urcrnrlon=trcLon,urcrnrlat=trcLat)
	# draw coastlines.
	m.drawcoastlines()
	# draw parallels and meridians.
	m.drawparallels(np.arange(-60.,90.,30.),labels=[1,0,0,0])

	m.drawcountries()

	m.readshapefile('st99_d00', name='states', drawbounds=False)

	# collect the state names from the shapefile attributes so we can
	# look up the shape obect for a state by it's name

	cm= plt.get_cmap('YlOrBr')
	ax = plt.gca() # get current axes instance
	states_names = []
	dens=[x[index] for x in stateDens]
	dens=[x.replace(',','') for x in dens]
	dens=[float(x) for x in dens]
	color=[x/max(dens) for x in dens]
	for a,b in enumerate(stateDens):
		stateDens[a].append(color[a])

	for shape_dict in m.states_info:
	    states_names.append(shape_dict['NAME'])

	# get Texas and draw the filled polygon
	for state in states_names:
		stateD= [x for x in stateDens if x[0] == state]
		if stateD:
			stateD=stateD[0]
			seg = m.states[states_names.index(state)]
			poly = Polygon(seg, facecolor=cm(stateD[-1]),zorder=0)
			ax.add_patch(poly)

	lats=[i[0] for i in data]
	lons=[i[1] for i in data]

	#CS = m.hexbin(lats,lons,latlon=True,C=z,gridsize=bins,cmap=plt.cm.jet)
	m.scatter(lons,lats,latlon=True,zorder=2,s=1, color="black")
	#plt.show()
	ind += 10
	plt.savefig(str(1900 + ind) + '.png')