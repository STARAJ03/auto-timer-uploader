#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "27765349")
API_HASH  = os.environ.get("API_HASH", "9df1f705c8047ac0d723b29069a1332b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
LOG = True  
auth_user = os.environ.get('auth_users', '1116405290').split(',')
auth_users = [int(user_id) for user_id in auth_user]

#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
