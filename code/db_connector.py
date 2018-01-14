import pymongo
from pymongo import MongoClient
import json
from collections import Counter
import itertools
import collections
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
client = MongoClient("152.46.20.163", 27017)

db = client.yelp_db
collection_b= db.business_p
collection_r = db.review_p
collection_c = db.checkin_p

#b_data = list(collection_b.find())
#r_data = list(collection_r.find())
#c_data = list(collection_c.find())
#print len(b_data)
#print len(r_data)
#print len(c_data)

def find_top_stars(flag):
	if flag == True:
		top_stars = sorted(b_data, key=lambda x:x['stars'],reverse=flag)[:50]
		file = open('top_stars.txt','w')
	elif flag == False:
		top_stars = sorted(b_data, key=lambda x:x['stars'],reverse=flag)[:50]
		file = open('least_stars.txt','w')
	for x in top_stars:
		temp = {}
		temp['business_id'] = x['business_id']
		temp['stars'] = x['stars']
		temp['longitude'] = x['longitude']
		temp['latitude'] = x['latitude']
		file.write(str(temp)+'\n')
	file.close()

def find_top_review_counts(flag):
	if flag == True:
		top_review_count = sorted(b_data, key=lambda x:x['review_count'],reverse=flag)[:50]
		file = open('top_review_count.txt','w')
	elif flag == False:
		top_review_count = sorted(b_data, key=lambda x:x['review_count'],reverse=flag)[:50]
		file = open('least_review_count.txt','w')
	for x in top_review_count:
		temp = {}
		temp['business_id'] = x['business_id']
		temp['review_count'] = x['review_count']
		temp['longitude'] = x['longitude']
		temp['latitude'] = x['latitude']
		file.write(str(temp)+'\n')
	file.close()

def find_top_checkin_counts(flag):
	top_checkin_count = {}
	checkins = list(db.checkin_p.find())
	for x in checkins:
		b_id = x['business_id']
		checkin_sum = reduce(lambda x,y:x+int(y.split(':')[1]),x['time'],0)
		top_checkin_count[b_id] = checkin_sum
	if flag == True:
		top_checkin_count = sorted(top_checkin_count.items(), key=lambda x : x[1], reverse=flag)[:50]
		file = open('top_checkin_count.txt','w')
	elif flag == False:
		top_checkin_count = sorted(top_checkin_count.items(), key=lambda x : x[1], reverse=flag)[:50]
		file = open('least_checkin_count.txt','w')
	boj = {}
	for x in top_checkin_count:
		id = x[0]
		boj = filter(lambda y:y['business_id']==id,b_data)
		temp = {}
		temp['business_id'] = id
		temp['checkins'] = x[1]
		temp['longitude'] = boj[0]['longitude']
		temp['latitude'] = boj[0]['latitude']
		file.write(str(temp)+'\n')
	file.close()

def plotStarsScatter():
	file1 = open('top_stars.txt','r')
	file2 = open('least_stars.txt','r')
	top_stars = []
	least_stars = []
	for x in file1:
		top_stars.append(x)
	for y in file2:
		least_stars.append(y)

	x1 = []
	y1 = []
	x1 = map(lambda x:eval(x)['longitude'],top_stars)
	y1 = map(lambda x:eval(x)['latitude'],top_stars)

	x2 = []
	y2 = []
	x2 = map(lambda x:eval(x)['longitude'],least_stars)
	y2 = map(lambda x:eval(x)['latitude'],least_stars)

	trace0 = go.Scatter(
    	x = x1,
    	y = y1,
    	mode = 'markers',
    	name = 'Top 50 Stars'
	)

	trace1 = go.Scatter(
    	x = x2,
    	y = y2,
    	mode = 'markers',
    	name = 'Least 50 Stars',
	)

	data = [trace0, trace1]
	layout = dict(title = 'Business locations vs Stars')
	# Plot and embed in ipython notebook!
	fig = dict(data=data, layout=layout)
	plot(fig, filename='stars-scatter')

def plotReviewsScatter():
	file1 = open('top_review_count.txt','r')
	file2 = open('least_review_count.txt','r')
	top_stars = []
	least_stars = []
	for x in file1:
		top_stars.append(x)
	for y in file2:
		least_stars.append(y)

	x1 = []
	y1 = []
	x1 = map(lambda x:eval(x)['longitude'],top_stars)
	y1 = map(lambda x:eval(x)['latitude'],top_stars)

	x2 = []
	y2 = []
	x2 = map(lambda x:eval(x)['longitude'],least_stars)
	y2 = map(lambda x:eval(x)['latitude'],least_stars)

	trace0 = go.Scatter(
    	x = x1,
    	y = y1,
    	mode = 'markers',
    	name = 'Top 50 Review counts'
	)

	trace1 = go.Scatter(
    	x = x2,
    	y = y2,
    	mode = 'markers',
    	name = 'Least 50 Review counts',
	)

	data = [trace0, trace1]
	layout = dict(title = 'Business locations vs Review counts')
	# Plot and embed in ipython notebook!
	fig = dict(data=data, layout=layout)
	plot(fig, filename='review-scatter')

def plotCheckinScatter():
	file1 = open('top_checkin_count.txt','r')
	file2 = open('least_checkin_count.txt','r')
	top_stars = []
	least_stars = []
	for x in file1:
		top_stars.append(x)
	for y in file2:
		least_stars.append(y)

	x1 = []
	y1 = []
	x1 = map(lambda x:eval(x)['longitude'],top_stars)
	y1 = map(lambda x:eval(x)['latitude'],top_stars)

	x2 = []
	y2 = []
	x2 = map(lambda x:eval(x)['longitude'],least_stars)
	y2 = map(lambda x:eval(x)['latitude'],least_stars)

	trace0 = go.Scatter(
    	x = x1,
    	y = y1,
    	mode = 'markers',
    	name = 'Top 50 Checkin counts'
	)

	trace1 = go.Scatter(
    	x = x2,
    	y = y2,
    	mode = 'markers',
    	name = 'Least 50 Checkin counts',
	)

	data = [trace0, trace1]
	layout = dict(title = 'Business locations vs Checkin counts')
	# Plot and embed in ipython notebook!
	fig = dict(data=data, layout=layout)
	plot(fig, filename='checkin-scatter')


'''flag = True
find_top_stars(flag)
print 'done stars!'
find_top_review_counts(flag)
print 'done review!'
find_top_checkin_counts(flag)
print 'done checkins!'''

plotStarsScatter()
plotReviewsScatter()
plotCheckinScatter()

client.close()