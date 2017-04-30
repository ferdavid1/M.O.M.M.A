try:
	from cmr import GranuleQuery
except ImportError:
	from python_cmr.cmr import GranuleQuery

api = GranuleQuery()

granules = api.short_name("AST_L1T").point(42.5, 75.5).query()

print(granules[0])