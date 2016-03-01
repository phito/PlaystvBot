import youtube
import playstv
import config
import time
import re
import praw

# regex used to find a playstv url
re_url = re.compile('(https?:\/\/(?:[a-z0-9-]+\.)*plays\.tv(?:\S*)?)')
already_done = []

################################################################################

print('Logging into Reddit...')
reddit = praw.Reddit(user_agent=config.REDDIT_USER_AGENT)
reddit.login(config.REDDIT_USER, config.REDDIT_PASSWD, disable_warning=True)
print('Logging into YouTube...')
yt = youtube.auth()

def get_cache_video(video_id):
    with open(config.VIDEO_CACHE_FILE, 'r') as f:
        content = f.readlines()

        for line in content:
            data = line.strip().split(',')
            if data[0] == video_id:
                return data[1]
    return False

def add_cache_video(video_id, youtube_id):
    with open(config.VIDEO_CACHE_FILE, 'a') as f:
        f.write(video_id + ',' + youtube_id + '\n')

def load_reddit_cache():
    with open(config.REDDIT_CACHE_FILE, 'r') as f:
        content = f.readlines()
        for line in content:
            already_done.append(line.strip())


def save_reddit_cache():
    with open(config.REDDIT_CACHE_FILE, 'w+') as f:
        for post in already_done:
            f.write(post + '\n')

def check_subreddit(subreddit):
    print('Checking /r/' + subreddit)

    # retreiving new submissions
    submissions = reddit.get_subreddit(subreddit).get_new(limit=20)

    for submission in submissions:
        match = re.search(re_url, submission.url)
        # if the post isn't a playstv url, check the selftext
        if not match:
            match = re.search(re_url, submission.selftext)

        if match and submission.id not in already_done:
            url = match.group(1)
            video_id = playstv.get_video_id(url)
            video_title = playstv.get_title(url)

            if not video_id:
                print('Unable to find video id for ' + url)
                already_done.append(submission.id)
                return
            elif not video_title:
                print('Unable to find video title for ' + url)
                already_done.append(submission.id)
                return

            print('PlayTv video found: ' + video_title)
            youtube_id = get_cache_video(video_id)

            if not youtube_id:
                filename = config.DOWNLOAD_FOLDER + video_id + '.mp4'
                print('Downloading...')
                playstv.download(video_id)
                print('Done downloading!')

                print('Uploading to Youtube...')
                youtube_id = youtube.upload(yt, config.DOWNLOAD_FOLDER + video_id + '.mp4', video_title,
                                            YOUTUBE_DESCR.format(playstv_url=url, reddit_url=submission.short_link), '')
                add_cache_video(video_id, youtube_id)
                print('Done! Youtube ID: ' + youtube_id)
            else:
                print('Video already downloaded! Youtube ID: ' + youtube_id)

            print('Replying to reddit post...')
            submission.add_comment(REDDIT_MSG.format(url = youtube_id))
            submission.upvote()
            print('All done!\n-------------------------')

            already_done.append(submission.id)
            save_reddit_cache()

load_reddit_cache()

while True:
    print('Checking subreddits...')

    for sub in config.SUBREDDITS:
	try:
            check_subreddit(sub)
            time.sleep(10)
	except Exception:
	    pass
