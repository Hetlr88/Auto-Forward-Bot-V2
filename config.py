from os import environ 

class Config:
    API_ID = environ.get("API_ID", "7324525")
    API_HASH = environ.get("API_HASH", "d28604398dc13af15dd108bb34a27a54")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7461358634:AAHqk9o56O33T6uy8h4rWFFs_GmNwlhzZXc") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6169288210').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
