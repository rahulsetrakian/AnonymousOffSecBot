import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import *
import logging
from webserver import keep_alive
from gc import callbacks
import json

# Importing Json file
filename='data/analytics.json'
with open(filename,'r') as file:
    data = json.load(file)
with open(filename,'w') as file:
    json.dump(data, file)



# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename="data/statics.log",
    level=logging.INFO)
logger = logging.getLogger("Anonymous")
# logging code end


# Functions for the bot
def updateJsonFile(key,value):
    jsonFile = open("data/analytics.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file
    ## Working with buffered content
    data[0][key] = value
    ## Save our changes to JSON file
    jsonFile = open("data/analytics.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()


data_for_hello = data[0]['Hello']
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'Hello {update.effective_user.first_name}, How may I help you? Type "/help" to get help.'
    )
    global data_for_hello
    logger.info('People Who Said Hello: '+str(data_for_hello))
    data_for_hello+=1
    updateJsonFile("Hello",data_for_hello)

data_for_start = data[0]['Start']
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I'm Anonymous Bot and I'll be helping you get started. Enter /help for more information.")
    global data_for_start
    logger.info('Total User Till Now: '+str(data_for_start))
    data_for_start+=1
    updateJsonFile("Start",data_for_start)

data_for_intro = data[0]['Help']
intro = open("data/start.txt", "r").read()
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(intro, disable_web_page_preview=True)
    global data_for_intro
    logger.info('Total Clicks On Help: '+str(data_for_intro))
    data_for_intro+=1
    updateJsonFile("Help",data_for_intro)

data_for_cyber=data[0]['Cybersecurity']
cyber = open("data/cybersecurity.txt", "r").read()
async def cybersecurity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(cyber, disable_web_page_preview=True)
    global data_for_cyber
    logger.info('Total Clicks On Help: '+str(data_for_cyber))
    data_for_cyber+=1
    updateJsonFile("Cybersecurity",data_for_cyber)


data_for_pro = data[0]['Programming']
pro = open("data/programming.txt", "r").read()
async def programming(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(pro, disable_web_page_preview=True)
    global data_for_pro
    logger.info('Total Clicks On Programming: '+str(data_for_pro))
    data_for_pro+=1
    updateJsonFile("Programming",data_for_pro)


data_for_darkweb=data[0]['Darkweb']
dark = open("data/darkweb.txt", "r").read()
async def darkweb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(dark, disable_web_page_preview=True)
    global data_for_darkweb
    logger.info('Total Clicks On Darkweb: '+str(data_for_darkweb))
    data_for_darkweb+=1
    updateJsonFile("Darkweb",data_for_darkweb)

data_for_it = data[0]['Information Technology']
forit = open("data/it.txt", "r").read()
async def it(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(forit, disable_web_page_preview=True)
    global data_for_it
    logger.info('Total Clicks On IT: '+str(data_for_it))
    data_for_it+=1
    updateJsonFile("Information Technology",data_for_it)

data_for_rules=data[0]['Rules']
rulefile = open("data/rules.txt", "r", encoding="utf8").read()
x = rulefile.split("---")
async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker(sticker=open('data/completion.webp', 'rb'))
    for single in x:
        await update.message.reply_text(single, disable_web_page_preview=True)
    await update.message.reply_sticker(sticker=open('data/separator.webp', 'rb'))
    global data_for_rules
    logger.info('Total Clicks On Rules: '+str(data_for_rules))
    data_for_rules+=1
    updateJsonFile("Rules",data_for_rules)


# Pathway Function Start

data_for_pathway=data[0]['Pathway']
async def pathway(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Programming", callback_data=str(1)),
            InlineKeyboardButton("Hacking", callback_data=str(2)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    path = open("data/path.txt", "r", encoding="utf8").read()
    await update.message.reply_text(path, reply_markup=reply_markup)
    global data_for_pathway
    logger.info('Total Clicks On Pathway: '+str(data_for_pathway))
    data_for_pathway+=1
    updateJsonFile("Pathway",data_for_pathway)

pathfp = open("data/pathfp.txt", "r").read()
pathfh = open("data/pathfh.txt", "r").read()

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "1":
        await update.callback_query.message.edit_text(pathfp, disable_web_page_preview=True)
    else:
        await update.callback_query.message.edit_text(pathfh, disable_web_page_preview=True)

# Pathway Function End


keep_alive()
TOKEN = "Put The Token Here"
print("BOT has started.")

while True:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("pathway", pathway))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("cybersecurity", cybersecurity))
    app.add_handler(CommandHandler("programming", programming))
    app.add_handler(CommandHandler("darkweb", darkweb))
    app.add_handler(CommandHandler("it", it))
    app.add_handler(CommandHandler("rules", rules))
    time.sleep(1)
    app.run_polling()
    app.idle()
