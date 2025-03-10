# Alex Miller
# Reddit Bot Version 2.0

import praw # grab posts from reddit
import random # get random post
from gtts import gTTS # text to speech
import moviepy.editor as mp # combine MP3 to stock video
from pathlib import Path # file stuff
import os # file stuff
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip as fp # cut the video down
from mutagen.mp3 import MP3 # get length of MP3
from datetime import datetime # date and time from machine
import shutil # moving files


def getpost(subr,usernum,comment): # gets the post from reddit and makes the index.txt and voice.mp3 files

    # reddit credentials
    reddit = praw.Reddit(
        # this content has been taken out due to having personal data
    )

    # get the subreddit, if it's private ask for a new one all over again
    try:
        subreddit = reddit.subreddit(subr).public_description
        print(subr)
        for i in range(0,5):
            print()
    except Exception as e:
        print("That subreddit is either private or restricted, try again")
        main()

    subreddit = reddit.subreddit(subr) # get a subreddit
    file = open("C://Users/mille/Documents/CS/Projects/Python/RedditBot/RedditBot2/index.txt", "w", encoding="utf-8")

    # arrays to use later
    titles = []
    posts = []
    comments = []

    # getting the posts
    num = 0
    for submission in subreddit.hot(limit=50): # post in the subreddit
        try:
            if (submission.stickied): 
                continue # dont get the ones that are pinned
            titles.append(submission.title)
            # print(submission.selftext)
            if (comment):
                comments.append(submission.coments[0].body)
            else:
                posts.append(submission.selftext)
            num += 1
            if num == usernum: 
                break # if hit the right amount then break
        except Exception as e:
            print("ERROR IN GETTING POST")
            exit()
    
    # get random tile and post
    rand = random.randint(0,len(titles)-1)
    file.write(titles[rand])

    # print the chosen post to the console
    print("------------------------------------------------------------------------------")
    print(titles[rand])
    print("------------------------------------------------------------------------------")
    print()


    # write the chosed post to the file
    file.write("\r\n")
    file.write("\r\n")
    if comment: # if it's more of a comment post
        file.write(comments[0])
        print(comments[0])
    else: # if its more of a normal rant post
        file.write(posts[rand])
        print(posts[rand])

    print()
    file.close()

# main method
def main():

    # get info user wants
    print("What subreddit would you like to do? ", end="")
    subr = input()
    print("How many posts would you like? ", end="")
    usernum = int(input())
    print("Would you like to print comments? (y/n) ",end="")
    usercom = input()
    comment = False
    if (usercom.lower() == 'y'): comment = True

    # get the post and create the index.txt and voice.mp3 files
    getpost(subr,usernum,comment)

    print()

    # ask if this post is a solid post, if not, runs method again
    ans = input("would you like this post? (y/n) ")
    if ans == 'n': 
        while ans == 'n':
            getpost(subr,usernum,comment)
            ans = input("would you like this post? (y/n) ")

    # create the mp3 file
    file = open("C://Users/mille/Documents/CS/Projects/Python/RedditBot/RedditBot2/index.txt", "r", encoding="utf-8").read()
    language = 'en'
    speech = gTTS(text = str(file), lang = language, slow = False)
    speech.save("Voice.mp3")

    # get all the stock videos
    videos = []
    videopath = "C:\\Users\\mille\\Documents\\CS\\Projects\\Python\\RedditBot\\RedditBot2\\Videos"
    videosnum = 0
    for filenames in os.listdir(videopath):
        videos.append(filenames)
        videosnum += 1

    # add the audio to the video
    rand = random.randint(0,videosnum-1)
    audio = mp.AudioFileClip("Voice.mp3")
    video1 = mp.VideoFileClip(videopath + "\\" + videos[rand])
    final = video1.set_audio(audio)

    # final output file
    final.write_videofile("output.mp4")

    # get current date and time for name of file
    now = datetime.now()
    dt = now.strftime("%m/%d/%Y %H:%M:%S")

    # get rid of slashes and colons
    dnt = ""
    for i in dt:
        if i == ' ': dnt += '_'
        elif i == ':': continue
        elif i == '/': continue
        else: dnt += i

    # get name of file
    finalfile = "video_" + str(dnt) + ".mp4"
    # cut the video to be the same length as the audio
    audio = MP3("Voice.mp3")
    endtime = audio.info.length
    fp("output.mp4", 0, endtime, targetname=finalfile)

    # move the file to a folder
    p = Path.cwd()
    shutil.move(p / finalfile, p / 'FinalVideos')

    print("------------------------------------------------------------------------------")
    print("FILES ARE READY")
    print("------------------------------------------------------------------------------")

# run main method
if __name__ == '__main__':
    main()