import os

# List of bot accounts


class Credentials(object):
    # load credentials from your environment variables
    ig_accounts = [
        {
            'id': 1,
            'name': 'xxxx',
            'username': 'xxxx',
            'password': 'xxxx'
        },
        {
            'id': 2,
            'name': 'xxxx',
            'username': 'xxxx',
            'password': 'xxxx'
        },
        {
            'id': 3,
            'name': 'xxxx',
            'username': 'xxxx',
            'password': 'xxxx'
        },
    ]


# BOT SETTINGS
class Configurations():

    IG_HANDLE = ['ausi_bree']  # A LIST OF NSTAGRAM HANDLES
    LIKES_PP = 0  # NUMBER OF POSTS TO LIKE
    COMMENTS_PP = 0  # NUMBER OF POST TO COMMENT ON

    COMM_LIST = [
        'Interesting feed, I love it!',
        'The best post I have seen today',
        'wonderful',
        'see why you are my favourite instagramer??',
        'This is beautiful. I am looking forward to seeing more posts from you. '
    ]
