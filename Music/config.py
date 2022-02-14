##Config

from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'Session')
BOT_TOKEN = getenv('BOT_TOKEN', '')
API_ID = int(getenv('API_ID', '13716091'))
API_HASH = getenv('API_HASH','')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '54000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '5053757688').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-100'))
ASS_ID = int(getenv("ASS_ID", '5028635008'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '5053757688').split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "scripthelper360")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "scripthelperbots")
GROUP = getenv("GROUP", "scripthelper360")
CHANNEL = getenv("CHANNEL", "scripthelperbots")
