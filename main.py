import youtube
import playstv
import config
import time
import re
import praw
import os
import traceback
import sqlite3

# regex used to find a playstv url
re_url = re.compile('(https?:\/\/(?:[a-z0-9-]+\.)*plays\.tv(?:\S*)?)')

################################################################################

print('Opening database...')
db = sqlite3.connect(config.DATABASE_FILE)
print('Logging into Reddit...')
reddit = praw.Reddit(user_agent=config.REDDIT_USER_AGENT)
reddit.login(config.REDDIT_USER, config.REDDIT_PASSWD, disable_warning=True)
print('Logging into YouTube...')
yt = youtube.auth()

def init_db():
    c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS reddit(postid TEXT PRIMARY KEY NOT NULL);')
    c.execute('CREATE TABLE IF NOT EXISTS youtube(playsid TEXT PRIMARY KEY NOT NULL, youtubeid TEXT NOT NULL);')
    db.commit()

def get_cache_video(video_id):
    c = db.cursor()
    c.execute('SELECT youtubeid FROM youtube WHERE playsid=?', [video_id])
    r = c.fetchone()

    if r:
        return r[0]
    return False

def add_cache_video(video_id, youtube_id):
    c = db.cursor()
    c.execute('INSERT INTO youtube VALUES (?, ?)',  [video_id, youtube_id])
    db.commit()

def add_cache_reddit(reddit_id):
    c = db.cursor()
    c.execute('INSERT INTO reddit VALUES (?)',  [reddit_id])
    db.commit()

def is_already_visited(reddit_id):
    c = db.cursor()
    c.execute('SELECT * FROM reddit WHERE postid=?', [reddit_id])
    r = c.fetchone()
    return r is not None

def check_subreddit(subreddit):
    print('Checking /r/' + subreddit)

    # retreiving new submissions
    submissions = reddit.get_subreddit(subreddit).get_new(limit=20)

    for submission in submissions:
        match = re.search(re_url, submission.url)
        # if the post isn't a playstv url, check the selftext
        if not match:
            match = re.search(re_url, submission.selftext)

        if match and not is_already_visited(submission.id):
            url = match.group(1)
            video_id = playstv.get_video_id(url)
            video_title = playstv.get_title(url)

            if not video_id:
                print('Unable to find video id for ' + url)
                add_cache_reddit(submission.id)
                return
            elif not video_title:
                print('Unable to find video title for ' + url)
                add_cache_reddit(submission.id)
                return

            # if the playstv title is the default one, we use the reddit title
            if video_title.startswith('Check out this'):
                video_title = submission.title

            print('PlayTv video found: ' + video_title)
            youtube_id = get_cache_video(video_id)

            if not youtube_id:
                filename = config.DOWNLOAD_FOLDER + video_id + '.mp4'
                print('Downloading...')
                playstv.download(video_id)
                print('Done downloading!')

                print('Uploading to Youtube...')
                youtube_id = youtube.upload(yt, config.DOWNLOAD_FOLDER + video_id + '.mp4', video_title,
                                            config.YOUTUBE_DESCR.format(playstv_url=url, reddit_url=submission.short_link), '')
                add_cache_video(video_id, youtube_id)
                print('Done! Youtube ID: ' + youtube_id)
            else:
                print('Video already downloaded! Youtube ID: ' + youtube_id)

            print('Replying to reddit post...')
            submission.add_comment(config.REDDIT_MSG.format(url = youtube_id))
            submission.upvote()
            print('All done!\n-------------------------')

            add_cache_reddit(submission.id)

# create video folder if doesn't exists
if not os.path.exists(config.DOWNLOAD_FOLDER):
    os.makedirs(config.DOWNLOAD_FOLDER)

init_db()

while True:
    print('Checking subreddits...')

    for sub in config.SUBREDDITS:
    	try:
            check_subreddit(sub)
    	except Exception, err:
            traceback.print_exc()
    	    pass
        time.sleep(10)
