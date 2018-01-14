import pymongo
from pymongo import MongoClient
import pprint
import math
from collections import Counter
import numpy
"""from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("try1").setMaster("local")
sc = SparkContext(conf=conf)
"""
def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def cosin(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)


#client = MongoClient("152.46.20.163", 27017)
client = MongoClient("localhost", 27017)


db = client.yelp_db
#collection = db.review
pdata = db.phoenixdata
business = db.business
review = db.review
tip = db.tip
user = db.user
checkin = db.checkin

data_business = business.find()
data_user = user.find()
data_tip = tip.find()
data_checkin = checkin.find()
data_review = review.find()

b=[]
u=[]
t=[]
c=[]
r=[]
i=0
"""phoenixdata = business.find({'$and':[{'$or':[{'city':'Phoenix,'},{'city':'Phoenix'},{'city':'Phoenix AZ'},{'city':'Phoneix'},{'city':'Phoneix AZ'},{'city':'Pheonix'}]},{'$or':[{'categories':'Restaurants'},{'categories':'Nightlife'},{'categories':'Hotels'}]}]})
for x in phoenixdata:
        pdata.insert(x)
        i=i+1
print i"""

"""for xx in x:
        pprint.pprint(xx)"""
"""u_business=[]
fooddata = business.find({"categories":"Food"})
print fooddata.count()
for d in fooddata:
        food_data.insert(d)"""
"""u_business=[]
for x in data_business:
	b.append(x)
	for z in x['categories']:
                if z not in u_business:
                        u_business.append(z)

pprint.pprint(u_business)
print len(u_business"""
	
"""print "business"
pprint.pprint(b)
for x in data_user:
	u.append(x)
print "user"
pprint.pprint(u)
for x in data_tip:
	t.append(x)
print "tip"
pprint.pprint(t)
for x in data_review:
	r.append(x)
print "review"
pprint.pprint(r)
for x in data_checkin:
	c.append(x)
print "checkin"
pprint.pprint(c)
"""
"""review_data = collection2.find()
review=[]
c = 0
for x in review_data:
        review.append(x)
        c += 1
        if (c%100000)==0.0:
                print c

reviews = filter(lambda x: x in business_id, review)

print len(reviews)"""

'''print collection.count()

data = collection.find({'$and':[{'state':'AZ'}]})

names = []
c = 0
for x in data:
	names.append(x['city'])
	c += 1
print c
names = list(set(names))
print names'''
more_states=[]
weird_rating=[]
no_friends=[]
same_business_comments=[]
similar_review=[]
weird_avegrage=[]
ucount=0
num=0
totalusers=user.find().count()
print totalusers
nofriends=user.find({"friends":"None"})
for f in nofriends:
    no_friends.append(f["user_id"])
print len(no_friends)
raw_input("no friends")
"""for user in data_user:
       ucount=ucount+1
       print ucount
       num=num+len(user["friends"])
       print len(user["friends"])
       raw_input("friends")
       if len(user["friends"])<2:
           print user["friends"]
           #no_friends.append(user)
print float(num/ucount)
raw_input("no friends")"""
same_business_comment=[]
weird_rating_list=[]
weird_average_list=[]
unique_business=[]
for user in no_friends[1:1000]:
    ucount=ucount+1
    print ucount
    data_review = review.find({"user_id":user})            
    num_review=0
    avg_rating=0
    weird_rating=0
    locations=[]
  
    
    """num_friends=len(user["friends"])
    if num_friends==0:
        no_friends.append(user)"""
    review_text=[]
    #print "number of friends: " +str(num_friends)
    for rev in data_review:
        num_review = num_review+1
        avg_rating=avg_rating+rev["stars"]
        b=business.find({"business_id":rev["business_id"]})
        review_text.append(rev["text"])
        for bus in b:
                b_std=review.find({"business_id":bus["business_id"]})
                sd=1.5
                """for std in b_std:
                    sd.append(float(std["stars"]))
                sd=numpy.std(sd)"""
                if float(rev["stars"])<float(bus["stars"])-sd or float(rev["stars"])>float(bus["stars"])+sd:
                        weird_rating=weird_rating+1
                if bus["state"] not in locations:
                        locations.append(bus["state"])
                if bus["business_id"] not in unique_business:
                        unique_business.append(bus["business_id"])
    simi=0
    c=0
    """for i in range(len(review_text)):
        for j in range(i+1,len(review_text)):
                #print review_text[i]
                #print review_text[j]
                
                r1,r2=build_vector(review_text[i],review_text[j])
                #print r1
                #print r2
                #print cosin(r1,r2)
                #raw_input("similarity")
                simi=simi+cosin(r1,r2)
                c=c+1
    simi=float(simi/c)"""
    num_locations=len(locations)
    """print "number of states: "+str(num_locations)
    print "number of reviews: "+str(num_review)
    print "number of weird ratings: "+str(weird_rating)
    print "average rating"+str(float(avg_rating/num_review))
    print "numer of unique business commented on: "+str(len(unique_business))
    print "similarity between his reviews: " +str(simi)"""
    if num_locations>3:
        more_states.append(user)
    if float(weird_rating/num_review)>.25:
        weird_rating_list.append(user)
    if float(avg_rating/num_review)>4.25 or float(avg_rating/num_review)<2.5:
        weird_average_list.append(user)
    if float(len(unique_business)/num_review)<.95:
        same_business_comment.append(user)
    #print "similarity between his reviews: " +str(simi)

print "no friends"
#print no_friends
print "more than 3 states"
print more_states
print "weird rating more than 1/4"
print weird_rating_list
print "avg rating too high or low"
print weird_average_list
print "more comments for same business"
print same_business_comment
        
client.close()
