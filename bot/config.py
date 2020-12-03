import os

#CREDENTIALS
class Credentials(object):
    
    BOT_EMAIL = os.environ.get('BOT_EMAIL')
    BOT_PASSWORD = os.environ.get('DB_PASSWORD')

#BOT SETTINGS
class Settings(Credentials):

    USER = 'Kolumbusbeats'
    LIKES_PP = 3 
    COMMENTS_PP = 0

    COMM_LIST = [
                    'Interesting feed, I love it!',
                    'The best post I have seen today',
                    'wonderful',
                    'see why you are my favourite instagramer??',
                    'This is beautiful. I am looking forward to seeing more posts from you. '
                ]
