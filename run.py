from bot.login_bot import LoginBot
from bot.engagement_bot import EngagementBot
from bot.config import Credentials, Configurations

#credentials
crededentials = Credentials.ig_accounts

#bot configurations
handles = Configurations.IG_HANDLE
likes_pp = Configurations.LIKES_PP
comments_pp =Configurations.COMMENTS_PP
comment_list = Configurations.COMM_LIST

#instatiate a list of bot accounts 
bots = [EngagementBot(cred['username'], cred['password'] ) for cred in crededentials]

#iterate through the list of accounts
for bot in range(len(bots)):
    bots[bot].login()
    for handle in handles:
        bots[bot].find_user(handle)
        bots[bot].like(likes_pp)
    bots[bot].quit_driver()

#git push -u owen-eternal master
