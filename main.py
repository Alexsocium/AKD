import random, time

from aiogram.utils.markdown import text, bold
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher


from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

fucups = ['блять', 'пиздец']


@dp.message_handler(commands=['start'])
async def psc(message: types.Message):
    await message.reply('Я могу ответить всем и каждому')

@dp.message_handler()
async def pec(message: types.Message):
    if message.text == 'Рандомное число':

        await message.reply(str(random.randint(1, 9999)))

    for i in fucups:
        if i in message.text:
            await message.reply('Так не красиво')
            time.sleep(2)
            await message.delete()

@dp.message_handler(commands=['help'])
async def phc(message: types.Message):
    texti = text(bold('Я могу сыграть одну из игр:',
                     '/ugch - угадай число'))
    await message.reply(texti)

@dp.message_handler(commands=['ugadai'])
async def process_ugch_command(message: types.Message):
    await message.reply('Выберите сложность')
    await message.reply('Легкая, Сложная')
    if message.text == 'Легкая':
        a = random.randint(1, 500)
        fl = True
        while fl:
            if a > int(message.text):
                await message.reply('Мое число больше')
            elif a < int(message.text):
                await message.reply('Мое число меньше')
            elif a == int(message.text):
                await message.reply('Поздравляю, вы прошли игру')
    elif message.text == 'Сложная':
        a = random.randint(1, 10000)
        fl = True
        while fl:
            if a > int(message.text):
                await message.reply('Мое число больше')
            elif a < int(message.text):
                await message.reply('Мое число меньше')
            elif a == int(message.text):
                await message.reply('Поздравляю, вы прошли игру')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

