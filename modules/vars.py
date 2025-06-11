#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "23274330")
API_HASH  = os.environ.get("API_HASH", "970e2e79779707c56d2b453b3a6eea48")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7886849876:AAHCnpO8zR7cqGS5Y3jgE5U95O0jgut3nSM")
LOG = True  
auth_user = os.environ.get('auth_users', '5680454765').split(',')
auth_users = [int(user_id) for user_id in auth_user]

#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
