# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


API_HASH = getenv("3a96c33357667f5d8a6f6991288d1e3a")
API_ID = int(getenv("API_ID", "27843871"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.2.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "Lunatic0de")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "SharingUserbot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
REPO_URL = getenv("REPO_URL", "https://github.com/mrismanaziz/PyroMan-Userbot")
STRING_SESSION1 = getenv("1BVtsOGwBu5afh1lncBEH0qwdOe2-vx9KUZkvPjwJVwqubyxjZo9LkTUtTZtR1qZCKt3bq8i5cXISW6xcPNE353mNerZrhsLsOJ_FkaiS40CEuq9ZqE4SzJLm6E5CozyJ2aGSZwICfuNypKPNm9RP2IvQCj7N-c2PAnyDQyZECkABpIDDdEzWj7MdIjdpyOQxwYItDa6MoRe1VorTcVwJ1XcubybzIG_INdtY0ueKZ8ZnJyWwiiqKSkRU93EStjSGyNc28MMssd6sUTgGkOl8Wm8YPGV0MVtLyKR0LBu4yUsqA-XYk9cD3C1FyTVeAVPr4_0wQ_lqJSRbvaeAW87nOsGlA_bjtEw=", "")
STRING_SESSION2 = getenv("1BVtsOGwBu5afh1lncBEH0qwdOe2-vx9KUZkvPjwJVwqubyxjZo9LkTUtTZtR1qZCKt3bq8i5cXISW6xcPNE353mNerZrhsLsOJ_FkaiS40CEuq9ZqE4SzJLm6E5CozyJ2aGSZwICfuNypKPNm9RP2IvQCj7N-c2PAnyDQyZECkABpIDDdEzWj7MdIjdpyOQxwYItDa6MoRe1VorTcVwJ1XcubybzIG_INdtY0ueKZ8ZnJyWwiiqKSkRU93EStjSGyNc28MMssd6sUTgGkOl8Wm8YPGV0MVtLyKR0LBu4yUsqA-XYk9cD3C1FyTVeAVPr4_0wQ_lqJSRbvaeAW87nOsGlA_bjtEw=", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
