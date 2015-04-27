import json

def addtoFlist(entry, flist):
	year = entry['Year'] 
	pop = float(entry['Value'])
	pop = int(pop - pop%10)

	if entry['Year'] in flist:
		flist[year] += pop
	else:
		flist[year] = pop

usa = {}
am = {}
world = {}

with open("json/worldpop.json") as f:
	alldat = json.load(f)
	for entry in alldat:
		code = entry["Country Code"]
		if code == "USA":
			addtoFlist(entry, usa)
		if code == "NAC" or code == "LCN":
			addtoFlist(entry, am)
		if code == "WLD":
			addtoFlist(entry, world)

with open("json/us_pop.json", "w") as f:
	json.dump(usa, f, sort_keys=True, indent=2)
with open("json/world_pop.json", "w") as f:
	json.dump(world, f, sort_keys=True, indent=2)
with open("json/america_pop.json", "w") as f:
	json.dump(am, f, sort_keys=True, indent=2)