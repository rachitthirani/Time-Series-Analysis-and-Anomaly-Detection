import pymongo
from pymongo import MongoClient
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import itertools

client = MongoClient("152.46.20.163", 27017)

db = client.yelp_db
collection = db.checkin_1_temp

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

checkins = list(collection.find().limit(4))

checkin_data = map(lambda x: x['time'], checkins)
days_d = {}
days_d['Wed'] = 3
days_d['Sun'] = 0
days_d['Fri'] = 5
days_d['Thu'] = 4
days_d['Mon'] = 1
days_d['Tue'] = 2
days_d['Sat'] = 6

fig = plt.figure(figsize=(18,16))

ax = fig.add_subplot(111,projection='3d')
color = ['red', 'blue', 'green', 'yellow']
for i in range(len(checkin_data)):
	days = map(lambda x:days_d[x.split('-')[0]],checkin_data[i])
	time = map(lambda x:int(x.split('-')[1].split(':')[0]),checkin_data[i])
	checkins = map(lambda x:int(x.split(':')[1]),checkin_data[i])
	n = 2
	xs = days
	ys = time
	zs = checkins
	the_fourth_dimension = randrange(n,0,100)
	colors = cm.hsv(the_fourth_dimension/max(the_fourth_dimension))
	colmap = cm.ScalarMappable(cmap=cm.hsv)
	colmap.set_array(the_fourth_dimension)

	yg = ax.scatter(xs, ys, zs, c=color[i], marker='o')
cb = fig.colorbar(colmap)

ax.set_xlabel('Days')
ax.set_ylabel('Time')
ax.set_zlabel('# of Checkins')


plt.show()
