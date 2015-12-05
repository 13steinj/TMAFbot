from __future__ import print_function
import praw

# creates sets where the posts it has already counted are stored.
r = praw.Reddit('TMAFbot by /u/peoplma')
r.login("XXXXXXXXX","XXXXXXXXX")
already_done = set()
subName = 'TellMeAFact'
deleted = '[deleted]'
nl = "\n"
s = r.get_subreddit(subName)
subreddit_posts = s.get_top_from_week(limit=10)
for post in subreddit_posts:
		print(post.score)
		print(post.title)
		filename='TMAFbot/TMAFbot.txt'
		post_score = str(post.score)
		post_title = '**{0}**'.format(post.title)
		obj=open(filename, 'ab+')
		strpost_score = '*({0})*'.format(post_score)
		obj.write(nl + '***' + nl + nl + strpost_score)
		obj.write(post_title + nl + nl + '***' + nl)
		obj.close()
		submission = r.get_submission(submission_id=post.id)
		for comment in submission.comments:
			commentstr = comment.body
			comment_score = str(comment.score)
			if commentstr != deleted and comment.score >= 3:
				print(comment.body)
				filename='TMAFbot/TMAFbot.txt'
				obj=open(filename, 'ab+')
				strcomment_score = '*({0})*'.format(comment_score)
				obj.write(strcomment_score)
				obj.write(commentstr + nl + nl)
				obj.close()
		#manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
		if post.id not in already_done:
			#Create a folder called TMAFbot before running the script
			#print post_json
			already_done.add(post.id)
		else:
			continue
