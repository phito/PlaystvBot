# reddit configuration
REDDIT_USER_AGENT='playstv'
# leave empty to be prompted for credentials at start
REDDIT_USER=''
REDDIT_PASSWD=''
SUBREDDITS= [ 'GlobalOffensive', 'Overwatch', 'leagueoflegends',
              'TeamSolomid', 'bladeandsoul', 'dayz',
              'Rivenmains', 'fizzmains', 'YasuoMains',
              'EliteDangerous', 'jaycemains', 'gaming',
              'StreetFighter', 'GnarMains', 'KassadinMains',
              'Warframe', 'RocketLeague', 'h1z1',
              'bardmains', 'Rainbow6', 'playrust',
              'fo4', 'counterstrike', 'Rengarmains',
              'ThreshMains', 'Doom', 'JustCause',
              'hearthstone', 'heroesofthestorm', 'DotA2',
              'Draven', 'Xcom', 'LeagueOfMemes',
              'TeemoTalk', 'Velkoz', 'ekkomains',
    	      'starcraft', 'RivalsOfAether', 'csclips'
    	      'funny', 'LeagueOfVideo', 'duckgame',
              'LeBlancMains', 'warthunder', 'tf2',
              'Doom']

REDDIT_MSG = ('[YouTube Mirror](https://youtu.be/{url})\n'
             '****\n'
             '[^contact](https://www.reddit.com/message/compose?to=Phito41) ^- '
             '[^source](https://github.com/phito41/PlaystvBot)')

YOUTUBE_DESCR = ('PlaysTv URL: {playstv_url}\nReddit thread: {reddit_url}\n'
                'I am a bot, and not affiliated with plays.tv, all copyrights reserved to their respective owners.\n'
                'Source code: https://github.com/phito41/PlaystvBot')

VIDEO_CACHE_FILE = 'videos.txt'
REDDIT_CACHE_FILE = 'reddit.txt'
DOWNLOAD_FOLDER = 'videos/'
