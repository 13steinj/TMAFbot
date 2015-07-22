import time
import praw
import random
import re
import urllib2
import sys
import traceback
import requests
from pprint import pprint
import sys


# creates sets where the posts it has already counted are stored.
r = praw.Reddit('TMAFbot by /u/peoplma')
r.login("XXXXXXXXX","XXXXXXXXX")
already_done = set()
subName = 'TellMeAFact'
deleted = str('[deleted]')
nl = "\n"
subreddit_posts = r.get_content(url='https://www.reddit.com/r/TellMeAFact/top/', params=None, limit=10, place_holder=None, root_field=u'data', thing_field=u'children', after_field=u'after', object_filter=None)
for post in subreddit_posts:
		print post.score
		print post.title
		filename='TMAFbot/'+'TMAFbot.txt'
		post_score = str(post.score)
		post_title = str('**' + post.title + '**')
		obj=open(filename, 'ab+')
		strpost_score = str('*(' + post_score + ')*' + ' ')
		strpost_title = str(post_title)
		obj.write(nl + '***' + nl + nl + strpost_score)
		obj.write(strpost_title + nl + nl + '***' + nl)
		obj.close()
		submission = r.get_submission(submission_id = post.id)
		for comment in submission.comments:
			commentstr = str(comment.body)
			comment_score = str(comment.score)
			if commentstr != deleted and comment.score >= 3:
				print comment.body
				filename='TMAFbot/'+'TMAFbot.txt'
				obj=open(filename, 'ab+')
				strcomment_score = str('*(' + comment_score + ')*' + ' ')
				strcommentstr = str(commentstr)
				obj.write(strcomment_score)
				obj.write(strcommentstr + nl + nl)
				obj.close()
		#pprint(vars(post))
		data= {'user-agent':'archive by /u/healdb and /u/peoplma'}
		#manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
		if post.id not in already_done:
			#Create a folder called TMAFbot before running the script
			#print post_json
			already_done.add(post.id)
		else:
			continue
