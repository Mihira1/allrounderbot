
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime

TOKEN="8379382592:AAG4q-Dgi_TTElTmhKjc9mVtMMypp1QifGI"

bot = telebot.TeleBot(TOKEN)

# Premium Start Menu
def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton("⚡ Status", callback_data="status")
    btn2 = InlineKeyboardButton("🕒 Time", callback_data="time")
    btn3 = InlineKeyboardButton("👤 Profile", callback_data="profile")
    btn4 = InlineKeyboardButton("💎 Premium", callback_data="premium")
    btn5 = InlineKeyboardButton("📢 Updates", url="https://t.me/yourchannel")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)

    return markup

# Start Command
@bot.message_handler(commands=['start'])
def start(message):

    text = f"""
✨ Welcome {message.from_user.first_name}

🚀 Modern Telegram Bot System
⚡ Fast & Advanced
💎 Premium Styled UI

Choose an option below.
"""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=main_menu()
    )

# Help Command
@bot.message_handler(commands=['help'])
def help_command(message):

    help_text = """
📚 Available Commands

/start - Open main menu
/help - Show commands
/ping - Bot speed
/id - Your Telegram ID
/time - Current time
"""

    bot.reply_to(message, help_text)

# Ping Command
@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "🏓 Pong! Bot is online.")

# User ID
@bot.message_handler(commands=['id'])
def user_id(message):
    bot.reply_to(
        message,
        f"🆔 Your ID: {message.from_user.id}"
    )

# Time Command
@bot.message_handler(commands=['time'])
def time_cmd(message):

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bot.reply_to(
        message,
        f"🕒 Current Time:\n{now}"
    )

# Button Actions
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    if call.data == "status":
        bot.answer_callback_query(call.id, "✅ Bot is Online")

    elif call.data == "time":

        now = datetime.datetime.now().strftime("%H:%M:%S")

        bot.edit_message_text(
            f"🕒 Current Time:\n{now}",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )

    elif call.data == "profile":

        user = call.from_user

        text = f"""
👤 Profile Info

🆔 ID: {user.id}
👤 Name: {user.first_name}
📛 Username: @{user.username}
"""

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )

    elif call.data == "premium":

        text = """
💎 Premium Features

⚡ Fast Response
🎨 Modern UI
🔒 Secure System
🚀 Advanced Commands
"""

        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )

# Auto Reply
@bot.message_handler(func=lambda message: True)
def auto_reply(message):

    bot.reply_to(
        message,
        "✨ I received your message."
    )

print("Bot Running...")
bot.infinity_polling()