import praw
from gtts import gTTS
import os
import random


#connect to reddit
reddit = praw.Reddit (
	# this content has been taken out since it's personal info 
)

#get the subreddit and open the file for writing
AskRedditSub = reddit.subreddit('StoryTime')
fileIndex = open("C://Users/mille/Documents/" + "index.txt", "w", encoding='utf-8')

#for loop to get hot posts
posts = ["0","1","2","3"]
n = 0
for post in AskRedditSub.hot(limit=5): #starts at post 0 instead of post 1
	if post.stickied:
		continue
	posts[n] = post.title
	n = n+1
RandomPost = random.choice(posts)
fileIndex.write(RandomPost + "\n")
fileIndex.write("\n")
fileIndex.write("\n")


for post in AskRedditSub.hot(limit=5):
	if post.title == RandomPost:
		submission = reddit.submission(post.id)
		break
	else:
		continue
fileIndex.write(post.selftext)

"""
submission.comments.replace_more(limit=0)
temp = 0
for top_level_comment in submission.comments:
	text = top_level_comment.body
	if text == '[removed]' or text == '[deleted]':
		continue
	fileIndex.write(text + '.' + '\n')
	fileIndex.write('\n')
	fileIndex.write("\n")
	temp = temp + 1
	if temp == 5:
		break

"""
fileIndex.close()

#open file again and convert to mp3
file = open('C://Users/mille/Documents/index.txt', 'r', encoding='utf-8').read().replace('\n',' ')
language = 'en'
speech = gTTS(text = str(file), lang = language, slow = False)
speech.save("Voice.mp3")