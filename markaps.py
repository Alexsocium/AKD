from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Main menu ---

btnRandom = KeyboardButton('Рандомное число - 🏹')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom)