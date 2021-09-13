import os
import requests
import aiohttp
import youtube_dl

from pyrogram import filters, Client
from youtube_search import YoutubeSearch



@Client.on_message(filters.command('song') & ~filters.private & ~filters.channel)
def song(client, message):

  
        
        
       
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵 i [AleXa OweNs](https://t.me/asanga_bot) Project..
I can play music in your group's voice call. Developed by [Asanga Udara](https://t.me/Ausanga_Udara).
Add me to your group and play music freely!**
        """,

     disable_web_page_preview=True
    )


   
