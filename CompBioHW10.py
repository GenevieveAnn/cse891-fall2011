import csv, urllib

## create function to open csv file and create dictionary of fish eaten on each date
def load_csv(url):
	fish_d = {}
	fp = urllib.urlopen(url)
	
	for row in csv.DictReader(fp):
		key = row['date']
		value = row['fish']
		
		x = fish_d.get(key, [])
		x.append(value)
		fish_d[key] = x
	
	return fish_d

# fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')

# print fish_d

## create function to create dictionary of dates each fish was eaten from fish_d
def make_dates_dict(fish_d):
        dates_d = {}
        
        fishies=[]
        for key in fish_d.keys():
                for item in fish_d[key]:
                        fishies.append(item)
        
        fish_set=set(fishies)
        
        for item in fish_set:
                dates_d[item] = []
                for key in fish_d:
                        if item in fish_d[key]:
                                dates_d[item].append(key)
        
        
        return dates_d


# dates_d = make_dates_dict(fish_d)

# print dates_d

## create function to report the fish eaten on a particular day from fish_d
def get_fishes_by_date(fish_d, date):
	fishlist = []
	if date in fish_d.keys():
		fishlist = fish_d[date]
	
	return fishlist

# get_fishes_by_date(fish_d, '10/9')
# get_fishes_by_date(fish_d, '13/9')

## create function to report the dates a particular type of fish was eaten from dates_d
def get_dates_by_fish(dates_d, fish):
	dateslist = []
	if fish in dates_d.keys():
		dateslist = dates_d[fish]
	
	return dateslist

# get_dates_by_fish(dates_d, 'ahi')
# get_dates_by_fish(dates_d, 'flounder')


datelist = ["10/9", "12/1"]
## create function to report the fish eaten on a list of dates from fish_d
def get_fishes_by_datelist(fish_d, datelist):
	fishlist = []
	for date in datelist:
		if date in fish_d.keys():
			fishlist.extend(fish_d[date])
	
	return fishlist

fishlist = ["cod", "ahi"]
## create function to report the dates fish from a list were eaten from dates_d
def get_dates_by_fishlist(dates_d, fishlist):
	dateslist = []
	for fish in fishlist:
		if fish in dates_d.keys():
			dateslist.extend(dates_d[fish])
	
	return dateslist



# this code is outside the functions and USES the functions to
# load data and ask questions of the data.

fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
dates_d = make_dates_dict(fish_d)

list_of_fish = get_fishes_by_date(fish_d, datelist)
print list_of_fish

# print get_dates_by_fish(dates_d, fishlist)

###

# test 1
x = get_fishes_by_date(fish_d, '1/1')
assert 'salmon' in x
print x

###

# test 2
x = get_dates_by_fish(dates_d, 'salmon')
assert '1/1' in x
assert '1/2' in x
print x

###

# test 3
x = get_fishes_by_datelist(fish_d, ['1/1'])
assert 'salmon' in x, x
print x

###

# test 4
x = get_dates_by_fishlist(dates_d, ['salmon'])
assert '1/1' in x
print x
