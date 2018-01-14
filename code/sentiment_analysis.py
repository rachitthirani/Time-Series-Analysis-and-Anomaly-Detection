import pymongo
from pymongo import MongoClient
import json
import nltk
from nltk import ne_chunk, word_tokenize, pos_tag
from nltk.tree import Tree
import string
client = MongoClient("152.46.20.163", 27017)
stopwords = set(nltk.corpus.stopwords.words('english'))

def getReviewDataFromDB():
	db = client.yelp_db
	collection_r = db.review_p
	reviews = list(collection_r.find({},{'review_id':1,'business_id':1,'stars':1,'text':1,'date':1,'_id':0}))
	file = open('reviews1.txt','w')
	for x in reviews:
		file.write(str(x)+'\n')
	file.close()
	client.close()

def flattenList(list):
    temp_list = []
    for word in list:
        word = word[0].encode('utf-8').translate(None, string.punctuation)
        if word not in stopwords and word <> '':
            temp_list.append(word)
    #print temp_list
    return temp_list

def get_nouns(text):
    words = word_tokenize(text)
    chunks = pos_tag(words)
    return flattenList(chunks)

def getReviewDataFromFile():
	file = open('reviews.txt','r')
	for lines in file:
		text = eval(lines)['text']
		text = get_nouns(text)
		print text
		file.close()

getReviewDataFromDB()