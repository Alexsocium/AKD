from aiogram import Bot, types
from aiogram.utils import executor

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Hello')