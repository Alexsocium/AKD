import random, time

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import markaps

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

fucups = ['блять', 'пиздец']


@dp.message_handler(commands=['start'])
async def psc(message: types.Message):
    await bot.send_message(message.from_user.id, 'Я могу ответить всем и каждому',
                           reply_markup = markaps.mainmenu)

@dp.message_handler()
async def pec(message: types.Message):
    if message.text == 'Рандомное число - 🏹':

        await message.reply(random.randint(1, 9999))

    for i in fucups:
        if i in message.text:
            await message.reply('Так не красиво')
            time.sleep(2)
            await message.delete()

@dp.message_handler(commands=['help'])
async def phc(message: types.Message):
    await message.reply('gg ne budet /photo')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

