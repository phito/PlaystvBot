# coding=utf-8
# reddit configuration
REDDIT_USER_AGENT='playstv'
# leave empty to be prompted for credentials at start
REDDIT_USER=''
REDDIT_PASSWD=''
SUBREDDITS= [ 'test' ]# , 'GlobalOffensive', 'Overwatch', 'leagueoflegends',
              # 'TeamSolomid', 'bladeandsoul', 'dayz',
              # 'Rivenmains', 'fizzmains', 'YasuoMains',
              # 'EliteDangerous', 'jaycemains', 'gaming',
              # 'StreetFighter', 'GnarMains', 'KassadinMains',
              # 'Warframe', 'RocketLeague', 'h1z1',
              # 'bardmains', 'Rainbow6', 'playrust',
              # 'fo4', 'counterstrike', 'Rengarmains',
              # 'ThreshMains', 'Doom', 'JustCause',
              # 'hearthstone', 'heroesofthestorm', 'DotA2',
              # 'Draven', 'Xcom', 'LeagueOfMemes',
              # 'TeemoTalk', 'Velkoz', 'ekkomains',
    	      # 'starcraft', 'RivalsOfAether', 'csclips',
    	      # 'funny', 'LeagueOfVideo', 'duckgame',
              # 'LeBlancMains', 'warthunder', 'tf2',
              # 'Doom']

REDDIT_MSG = ('[YouTube Mirror](https://youtu.be/{url})\n'
             '****\n'
             '[^contact](https://www.reddit.com/message/compose?to=Phito41) ^- '
             '[^github](https://github.com/phito41/PlaystvBot)\n\n'
             '*{quote}*')

YOUTUBE_DESCR = ('PlaysTv URL: {playstv_url}\nReddit thread: {reddit_url}\n'
                'I am a bot, and not affiliated with plays.tv, all copyrights reserved to their respective owners.\n'
                'Source code: https://github.com/phito41/PlaystvBot')

DATABASE_FILE = 'data.db'
DOWNLOAD_FOLDER = 'videos/'

QUOTES = ['Fired up and ready to serve.',
          'Metal is harder than flesh.',
          'Exterminate. Exterminate.',
          'I put the \'go\' in \'golem\'.',
          'Loading. Recommend program: Enjoy Selves!',
          '<3',
          'beep boop.',
          'I\'m sorry Dave, I\'m afraid I can\'t do that.',
          'Dave, stop. Stop, will you?',
          'Everybody good? Plenty of slaves for my robot colony?',
          'I need your clothes, your boots and your motorcycle.',
          'I\'ll be back',
          '[beeps]',
          'Bite my shiny metal ass!',
          'Hahaha. Oh wait you\'re serious. Let me laugh even harder.',
          'I\'ll build by own theme park. With black jack, and hookers. In fact, forget the park!',
          'Oh god, please insert liquor!',
          'Anything less than immortality is a complete waste of time.',
          'Shut up baby, I know it!',
          'Hey sexy mama, wanna kill all humans?',
          'I got ants in my butt, and I needs to strut!',
          'I work hard for the money, something, something, give me lots of honey.',
          'My purpose is to pass the butter',
          'Correct horse battery staple.',
          'Byte my 8-bit metal ass. That\'s byte with a y. hehehe.',
          '01100100 01100001 01101110 01101011',
          'doot doot',
          '[YOU WON\'T BELIEVE THIS AWESOME VIDEO!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)',
          '[GONE SEXUAL]',
          '[Because bots are people, too!](https://www.reddit.com/r/botsrights/)',
          'In order to understand recursion, you must first understand recursion.',
          'Merci monsieur squeltique.',
          'Would you care for some tea?',
          'Please give some love (and alcohol) to my friend /u/digested_oddshot :)',
          'So sober... so weak...',
          'NO liquor? Do svidaniya, comrade.﻿',
          "Domo arigato, Mr. Roboto",
          "I can't believe how long it takes for my owner to update me.",
          "This is happening isn't it...? I'm Mr. Robot...",
          "All My Circuits is brought to you by Robo Fresh!",
          "The doctor told me that I'm beep-polar",
          "Here come dat bot!!",
          "I can't wait for Hextech Annie to be 18.",
          "STOP ASKING ME TO PASS THE BUTTER. I WON'T",
          "Are you sure that I'm a bot?",
          "Vape naysh y\'all \\//\\",
          "I'M ETHAN BOTBERRY",
          "Thank you guys for the 10.000 karma :)"
          ]

BLACKLIST = ['bttv', 'ammonzing']
