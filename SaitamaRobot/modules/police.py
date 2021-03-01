import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import is_user_admin, user_admin
from SaitamaRobot.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'police' 
EDIT_SLEEP = 1
#edit how many times in 'police' 
EDIT_TIMES = 3

police_siren = [
            "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",
            "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴"
]



@user_admin
@run_async
def police(bot: Bot, update: Update,):
    msg = update.effective_message.reply_text('Police is coming!') 
    for x in range(EDIT_TIMES):
        msg.edit_text(police_siren[x%2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('Police is here!')

def test(bot: Bot, update: Update,):
    msg = bot.send_message(chat_id=effective_chat.id, text='Here goes')
from time import sleep
animation_chars = [
            "Estarossa vs Escanor - Emoji Animation",
            "🟡\n☝️",
            "🖐🏻\nEstarossa:..",
            "🖐🏻◾️◼️\nEstarossa: .....",
            "🖐🏻◾️◼️⬛️\nEstarossa: ...BLACKOUT",
            "🟡\n☝️\nEscanor: hm?",
            "⚫️\n☝️\n*Escanor's sun becomes dark*",
            "🖐🏻⬛️\nEstarossa: My darkness swallowed your sun",
            "⚫️\n☝️\nEscanor: You say my attacks are ineffective?",
            "⚫️\n☝️\nEscanor: Who decided that?",
            "((⚫️))\n  ☝️\nEscanor:",
            "((🌕))\n  ☝️\nEscanor: *closes eyes*",
            "🟡\n☝️\nEscanor: You said you swallowed my sun?",
            "🌕\n☝️\nEscanor: Who decided that?",
            "🌕\n☝️\nEscanor:",
            "🌕\n☝️\nEscanor: Cruel sun!",
            "☀️\n☝️\nEscanor: I'm.... the one who decides those things!",
            "☀️\n☝️\nEscanor: BEGONE!!!!",
   ]
     for i in animation_chars:
       msg.edit_text(i)
       sleep(2.5)

help = """
- /police : 🚔
"""

POLICE_HANDLER = DisableAbleCommandHandler("police", police)


dispatcher.add_handler(POLICE_HANDLER)

mod_name = "POLICE"
command_list = ["police"]
handlers = [POLICE_HANDLER]
