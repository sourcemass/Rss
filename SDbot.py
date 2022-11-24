#        @PPF22 (https://github.com/Sadew451/SDTelegraphBot).
#    Copyright (c) 2022 RsExs

import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery, InlineQuery)

SDBots = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

@SDBots.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("` ...`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text(" ...`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`  `") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@SDBots.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("` ...`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("` ...`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("   ...") 
  else:
    await message.reply_text("      5  ")

@SDBots.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("` ...`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("` ...")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("   ...") 
  else:
    await message.reply_text("        5Mb")

STICKER = "CAACAgUAAxkBAAEBT4Bhih3lL3FSMYx1pFvEwwwplJfqhQACJgQAAgjSKFSQdidotfevrCIE"
      
@SDBots.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('‹  ›', callback_data='help'),
        InlineKeyboardButton('•  •', callback_data='close')
    ],
    [
        InlineKeyboardButton('‹   ›', url='http://telegram.me/vvvznn'),
        InlineKeyboardButton('‹   ›', url=https://t.me/TwS_RsExS'')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await SDBots.send_message(
        chat_id=message.chat.id,
        text=""" 
        
        
        
          
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@SDBots.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('‹   › ', callback_data='home'),
        InlineKeyboardButton('•  •', callback_data='close')
    ],
    [
        InlineKeyboardButton('‹   ›', url='http://telegram.me/SDBOTs_Inifinity')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await SDBots.send_message(
        chat_id=message.chat.id,
        text="""    ,
        
    
     """,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@SDBots.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)

SDBots.run()
