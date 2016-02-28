import httplib2
import sys
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import argparser, run_flow
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient.errors import HttpError

YOUTUBE_SECRETS_FILE = "client_secrets.json"
YOUTUBE_CATEGORY = '22'
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
args = argparser.parse_args()

def auth():
    flow = flow_from_clientsecrets(YOUTUBE_SECRETS_FILE, scope=YOUTUBE_UPLOAD_SCOPE)
    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, args)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))

def upload(yt, file, title, description, tags):
    body=dict(
        snippet=dict(
            title=title[:100],
            description=description,
            categoryId=YOUTUBE_CATEGORY,
            tags=tags
            ),
        status=dict(
            privacyStatus='public'
            )
        )
    # Call the API's videos.insert method to create and upload the video.
    insert_request = yt.videos().insert(part=",".join(body.keys()), body=body,
                     media_body=MediaFileUpload(file, chunksize=-1, resumable=True))
    return resumable_upload(insert_request)

def resumable_upload(insert_request):
    response = None
    error = None
    retry = 0
    yt_id = None
    while response is None:
        try:
            status, response = insert_request.next_chunk()
            if response is not None:
                if 'id' in response:
                    yt_id = response['id']
                else:
                    exit('The upload failed with an unexpected response: %s' % response)
        except HttpError, e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                    error = 'A retriable HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
            else:
                raise
        except RETRIABLE_EXCEPTIONS, e:
            error = 'A retriable error occurred: %s' % e

        if error is not None:
            print error
            retry += 1
            if retry > MAX_RETRIES:
                exit('No longer attempting to retry.')

            max_sleep = 2 ** retry
            sleep_seconds = random.random() * max_sleep
            print 'Sleeping %f seconds and then retrying...' % sleep_seconds
            time.sleep(sleep_seconds)
    return yt_id
