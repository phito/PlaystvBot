import requests
import re
import config
import HTMLParser

# user agent used to access playstv
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'

DOWNLOAD_URL = 'http://m0playscdntv-a.akamaihd.net/video/%s/processed/720.mp4'

# regex used to find the id of a playstv video
re_vidid = re.compile('akamaihd\.net\/video\/([a-zA-Z0-9-_]*)\/processed')
# regex used to find the title of a playstv video
re_title = re.compile(ur'data-share-text=\\"(.*?)\\"')

def get_title(url):
    h = HTMLParser.HTMLParser()
    html = h.unescape(requests.get(url, headers={'User-Agent': USER_AGENT}).content.encode('utf-8'))
    match_title = re.search(re_title, html)

    if match_title:
        return match_title.group(1)
    else:
        return False

def get_video_id(url):
    h = HTMLParser.HTMLParser()
    html = h.unescape(requests.get(url, headers={'User-Agent': USER_AGENT}).content.encode('utf-8'))
    match_id = re.search(re_vidid, html)

    if match_id:
        return match_id.group(1)
    else:
        return False

def download(video_id):
    req = requests.get(DOWNLOAD_URL % video_id, stream=True)
    with open(config.DOWNLOAD_FOLDER + video_id + '.mp4', 'wb') as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk: f.write(chunk)
