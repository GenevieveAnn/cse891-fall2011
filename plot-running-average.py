import random
from matplotlib import pyplot
# import dhtml
image_file = '/root/Dropbox/graph.png'

def roll():
	avgs = []
	x = []
	y = []
	for i in range(150):
		y.append(random.randint(1, 1000))
		x.append(i)
		avgs.append( sum(y) / float(len(y)) )
	return x, avgs

x, y = roll()
pyplot.plot( x, y )
pyplot.savefig(image_file)
# dhtml.image(image_file)

