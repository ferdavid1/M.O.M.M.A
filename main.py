from cmr import GranuleQuery

api = GranuleQuery()

granules = api.short_name("AST_L1T").point(42.5, 75.5).query()

for granule in granules:
	print(granule)