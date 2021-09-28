import random, time

from aiogram.utils.markdown import text, bold
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher


from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

fucups = ['блять', 'пиздец']

@dp.message_handler(commands=['pr'])
async def prm(message:types.Message):
    await message.reply('Пиши число дурик')
    time.sleep(5)
    print(message.text)

@dp.message_handler(commands=['ugadai'])
async def process_ugadai_command(message: types.Message):
    print('fuh')
    time.sleep(4)
    a = random.randint(1, 10000)
    fl = True
    await message.reply('У тебя есть 5 секунд чтобы написать первое число')
    while fl:
        time.sleep(5)
        if a > int(message.text):
            await message.reply('Мое число больше')
        elif a < int(message.text):
            await message.reply('Мое число меньше')
        elif a == int(message.text):
            await message.reply('Поздравляю, вы прошли игру')
            f1 = False


@dp.message_handler(commands=['start'])
async def psc(message: types.Message):
    await message.reply('Я могу ответить всем и каждому')


@dp.message_handler(commands=['help'])
async def phc(message: types.Message):
    texti = text(bold('Я могу сыграть одну из игр:',
                     '/ugch - угадай число'))
    await message.reply(texti)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

