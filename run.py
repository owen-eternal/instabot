from bot.login_bot import LoginBot
from bot.engagement_bot import EngagementBot
from bot.config import Credentials, Settings

#configure
username = Credentials.BOT_EMAIL
password = Credentials.BOT_PASSWORD
user = Settings.USER
likes_pp = Settings.LIKES_PP

#engagement bot in action
bot = EngagementBot(username, password)
bot.login()
bot.find_user(user)
bot.like(likes_pp)