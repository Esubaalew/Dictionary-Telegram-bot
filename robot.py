# robot.py

"""Simple robot for a simple dictionary.
This robot uses an online dictionry website to extract meaningd for english words- 
and phrases."""

from cgitb import text
from fileinput import close
from turtle import update
from unittest.main import main
from warnings import filters
from telegram import Update
from telegram.ext import *
from telegram.ext.updater import Updater
from telegram.ext.callbackcontext import CallbackContext
import requests
from bs4 import BeautifulSoup
from pprint import pp, pprint


def start(update: Update, context: CallbackContext):
    """Starts conversation after /start command from user.
    This method and/or command tried to identify some of my school clasmates
    and these users will have their true name with their father's name First letter.
    If for example, the pre-iddentified user is Selam Debebe, the bot will say 'hey Selam D' instead
    of using the default way --'hey, user.first_name'
    I used this technique to show that telegram bots can do specific jobs to specific users.
    """

    user = update.message.from_user
    userName = user.first_name
    if user.id == 1742717838:
        Name = "Azeb M"
        update.message.reply_text(
            "Hey, " + Name+"! I admire you very much!")
        update.message.reply_text(
            "Send any word, you want meaning for. I will define it.")
    elif user.id == 1648265210:
        Name = "Esubalew Chekol"
        update.message.reply_text("Hey,",Name+"!")
        update.message.reply_text(
            "Send any word, you want meaning for. I will define it")
    elif user.id == 1877835630:
        Name = 'Lidiya F'
        update.message.reply_text(
            f'Hey, {Name}!'
        )
    elif user.id == 842766828:
        Name = 'Bereket G'
        update.message.reply_text(
            "Hey,{}".format(Name)
        )
    elif user.id == 1615509187:
        Name = 'Hayat E'
        update.message.reply_text(
            "Hey,", Name

        )
    else:
        update.message.reply_text("Hey, " + userName+"!")
        update.message.reply_text(
            "Send any word, you want meaning for. I will define it.")


def bad_command(update: Update, context: CallbackContext):
    """Detects unknown commands"""

    update.message.reply_text(
        "Sorry,  '%s' is not a valid command!\nUse /start to restart  me or /list to find other bots " % update.message.text
    )


def list(update: Update, context: CallbackContext):
    """Returns the list of bot usernames after /list command"""

    update.message.reply_text(
        """
        other bots
        @TheBELAHbot
        @AAU_Robot
        @AllFunctionsbot
        @Informing_Robot
        Join @esubalewbots for more

        """
    )


def search(update: Update, context: CallbackContext):
    """Scraps the online web source and extracts the needed HTML content.
    Returns the following:
    Meaning of a text
    Etymology of a text if found
    Examples if found
    """
    text = update.message.text
    text = text.strip()
    if len(text) > 27:
        update.message.reply_text(
            "Sorry! I can't find meanings for words having letters greater than 27\n The longest word i can define is electroencephalographically[27 letters]"
        )
        return

    url = 'https://www.merriam-webster.com/dictionary/' + text
    headers = {'User-Agent': 'Generic user agent'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    pprint(soup)
    try:
        update.message.reply_text(
            f'I am searching for {text}, Please wait....',
            quote=True
        )

        try:
            meaning = soup.find('div', {'class': 'vg'}).text
            update.message.reply_text('Meaning for ' + text+'\n' + meaning)
        except:
            update.message.reply_text('Meaning not found for '+text+'!')

        try:
            etymology = soup.find('p', {'class': 'et'}).text
            update.message.reply_text('Etymology\n' + etymology)
        except:
            update.message.reply_text('Etymology not found for '+text+'!')
        try:
            examples = soup.find(
                'div', {'class': "in-sentences read-more-content-hint-container"}).text
            total_length = len(examples)
            see_pos = total_length-9
            deleted = examples[see_pos:]
            examples = examples.replace(deleted, "")
            #print(examples)
            update.message.reply_text('Examples for '+text+"\n" + examples)
        except:
            update.message.reply_text(f'No examples found for {text}')

    except:
        update.message.reply_text('Something went wrong...')


def filter_photos(update: Update, context: CallbackContext):
    """Detects photos from user and tells to user that robot can not search
    for photos"""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't search for Photos/Images!", quote=True
    )


def filter_videos(update: Update, context: CallbackContext):
    """Detects videos received from user and tells to user that robot can not search
    for videos"""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't search for Videos", quote=True
    )


def filter_contacts(update: Update, context: CallbackContext):
    """Detects contacts received from user and tells to user that robot can not search
    for contats"""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't search for Contacts or Contacts are useless for me",
        quote=True
    )


def filter_polls(update: Update, context: CallbackContext):
    """Detects polls received from user and tells to user that robot can not search
    for polls"""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't need polls or i don't search for them!",
        quote=True
    )


def filter_captions(update: Update, context: CallbackContext):
    """Detects captions received from user and tells to user that robot can not search
    for captions."""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't need captions for my work or i don't search for them!",
        quote=True
    )


def filter_stickers(update: Update, context: CallbackContext):
    """Detects stickers received from user and tells to user that robot can not search
    for stickers."""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't search for Stickers!",
        quote=True
    )


def filter_animations(update: Update, context: CallbackContext):
    """Detects animations received from user and tells to user that robot can not search
    for animations."""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't search for animations!",
        quote=True
    )


def filter_attachments(update: Update, context: CallbackContext):
    """Detects attachiments received from user and tells to user that robot can not search
    for attachments."""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't search for attachments!",
        quote=True
    )


def filter_audios(update: Update, context: CallbackContext):
    """Detects audios received from user and tells to user that robot can not search
    for audios."""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently, I don't search for Audios!",
        quote=True
    )


def filter_dice(update: Update, context: CallbackContext):
    """Detects dice received from user and tells to user that robot can not search
    for dice."""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Dice is beyound my knowlege!",
        quote=True
    )


def filter_documents(update: Update, context: CallbackContext):
    """Detects documents received from user and tells to user that robot can not search
    for doucuments."""

    user = update.message.from_user.first_name
    update.message.reply_text(
        f"Dear {user}, Currently I am incapable of searching documents!",
        quote=True
    )


# def main():
TOKEN = '5497017439:AAHkmvbmBIwLaH8J2j3FKjGFgCCDJ8s07O0'
updater = Updater(TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('list', list))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text & (~Filters.command), search))
updater.dispatcher.add_handler(
    MessageHandler(Filters.contact, filter_contacts))
updater.dispatcher.add_handler(MessageHandler(Filters.video, filter_videos))
updater.dispatcher.add_handler(MessageHandler(Filters.poll, filter_polls))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, filter_photos))
updater.dispatcher.add_handler(MessageHandler(Filters.dice, filter_dice))
updater.dispatcher.add_handler(
    MessageHandler(Filters.document, filter_documents))
updater.dispatcher.add_handler(
    MessageHandler(Filters.caption, filter_captions))
updater.dispatcher.add_handler(
    MessageHandler(Filters.sticker, filter_stickers))
updater.dispatcher.add_handler(MessageHandler(
    Filters.animation, filter_animations))
updater.dispatcher.add_handler(MessageHandler(
    Filters.attachment, filter_attachments))
updater.dispatcher.add_handler(MessageHandler(Filters.audio, filter_audios))
updater.dispatcher.add_handler(MessageHandler(Filters.command, bad_command))
updater.start_polling()
