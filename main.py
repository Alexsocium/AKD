import random

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def psc(message: types.Message):
    await message.reply('Я могу ответить всем и каждому')

@dp.message_handler()
async def pec(message: types.Message):
    if message.text == 'Рандомное число':

        await message.reply(random.randint(1, 9999))

@dp.message_handler(commands=['help'])
async def phc(message: types.Message):
    await message.reply('gg ne budet /photo')

