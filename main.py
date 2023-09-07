import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import m, mr

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("Assalomu alaykum. Botimizga xush kelibsiz! 🙋\nKerakli bolimni tanlang 👇", reply_markup=m)

@dp.message_handler(text="Darsliklar 📙")
async def textbooks(msg: types.Message):
    await msg.answer("🏫 Sinfni tanlang 👇", reply_markup=mr)

@dp.message_handler(text="🔙 Asosiy menyuga")
async def textbooks(msg: types.Message):
    await msg.answer("Assalomu alaykum. Botimizga xush kelibsiz!", reply_markup=m)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)