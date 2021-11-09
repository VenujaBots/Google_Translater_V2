from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "2111962326:AAERb1Xma1GlV4yKEb3iRNwmFxhKO2MqbiI")

API_ID = int(os.environ.get("API_ID",7395896))

API_HASH = os.environ.get("API_HASH", "cd3998ddf318dad74d7c506731bc0abc")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()
