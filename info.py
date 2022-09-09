# Modified By @DARK-Devil
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = 'Film_search'
API_ID = 15197646
API_HASH = '12ad370a8455c02701649e1d7b322dc2'
BOT_TOKEN = '5429635253:AAFKP3jzAXaQmByU5TSZfAuudBKC7tq6PQc'

# Bot settings
CACHE_TIME =300
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = 'https://telegra.ph/file/ca7db8cf548be0f7e429c.jpg https://telegra.ph/file/ee515fc9df1286c0a3a0d.jpg https://telegra.ph/file/a1d1a6c52771c817ad824.jpg https://telegra.ph/file/df33395c05aad5b341224.jpg https://telegra.ph/file/e9fbad2773626e39adfe1.jpg https://telegra.ph/file/c0b7cde6396908c9c492d.jpg https://telegra.ph/file/70b40295f9db3fa203afc.jpg https://telegra.ph/file/b8462930758fd92e56887.jpg https://telegra.ph/file/979a9187a722e514c95c0.jpg https://telegra.ph/file/b515e1f7a94556caf233f.jpg'.split()

# Admins, Channels & Users
ADMINS = [5512382938, 2071644540]
CHANNELS = [-1001621272794, -1001673187322, -1001607692169]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = [-1001616221826]
AUTH_CHANNEL = [-1001616221826]
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = 'mongodb+srv://film-detective:darkdevil@darkdevil.lcfllos.mongodb.net/?retryWrites=true&w=majority'
DATABASE_NAME = 'darkdevil'
COLLECTION_NAME = 'Devil_Films'

# Others
LOG_CHANNEL = [-1001787331054]
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'DarkDevilBotz')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), True)
CUSTOM_FILE_CAPTION = "🤩<b>ᴊᴏɪɴ [ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ](https://t.me/DarkNetflixPublic)</b>😍\n📂𝙵𝙸𝙻𝙴 : <code>{file_name}</code>\n📼𝚂𝙸𝚉𝙴 : <i>{file_size}<i>\n😈𝙾𝚆𝙽𝙴𝚁 : <a href=https://t.me/DARKDevilV2>ᴅᴀʀᴋ ᴅᴇᴠɪʟ</a>"
BATCH_FILE_CAPTION = "🤩<b>ᴊᴏɪɴ [ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ](https://t.me/DarkNetflixPublic)</b>😍\n📂𝙵𝙸𝙻𝙴 : <code>{file_name}</code>\n📼𝚂𝙸𝚉𝙴 : <i>{file_size}<i>\n😈𝙾𝚆𝙽𝙴𝚁 : <a href=https://t.me/DARKDevilV2>ᴅᴀʀᴋ ᴅᴇᴠɪʟ</a>"
IMDB_TEMPLATE = "🤩𝙷𝙴𝚈, {message.from_user.mention} 𝙱𝚁𝙾\n ᴀʀᴇ ʏᴏᴜ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ ᴛʜɪꜱ ᴍᴏᴠɪᴇ?\n 👉 {query} 👈\n\n<b>♥️𝚃𝙸𝚃𝙻𝙴</b>: <a href={url}>{title}</a>\n🎭 𝙶𝙴𝙽𝚁𝙴𝚂: {genres}\n📆 𝚈𝙴𝙰𝚁: <a href={url}/releaseinfo>{year}</a>\n🌟 𝚁𝙰𝚃𝙸𝙽𝙶: <a href={url}/ratings>{rating}</a> / 10 (𝙱𝙰𝚂𝙴𝙳 𝙾𝙽 {votes} 𝚄𝚂𝙴𝚁 𝚁𝙰𝚃𝙸𝙽𝙶𝚂.)\n💽 𝚁𝚄𝙽𝚃𝙸𝙼𝙴: {runtime} Minutes\n📆 𝚁𝙴𝙻𝙴𝙰𝚂𝙴𝙳 : {release_date}\n🌍 𝙲𝙾𝚄𝙽𝚃𝚁𝙸𝙴𝚂 : <code>{countries}</code>\n\n☕𝙿𝙾𝚆𝙴𝚁𝙳 𝙱𝚈☕\n <a href=https://t.me/DarkDevilBotz>©️ᴅᴀʀᴋ ᴅᴇᴠɪʟ ʙᴏᴛᴢ</a>\n <a href=https://t.me/TeamDarkDevil>©️ᴛᴇᴀᴍ ᴅᴀʀᴋ ᴅᴇᴠɪʟ</a>"
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = [-1001787331054]
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
