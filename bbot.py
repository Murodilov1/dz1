from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from  but import keydord_main, MENU, genrate_menu
import asyncio, random
bot = Bot(token = "7909819952:AAGO4HWwBkJ1ziGbFbRb3R9exDxxzkSbjFI")
dp = Dispatcher()
chose = ["камень", "ножницы", "бумага"]
botchoice = random.choice(chose)
@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Начинается игра", reply_markup=keydord_main)
@dp.message(F.text == "выбрать вариант")
async def choice(message:types.Message):
    keyboard = genrate_menu()
    await message.answer("выберите вариант", reply_markup=keyboard)
@dp.message(F.text == "ножницы")
async def cc(message:types.Message):
    if botchoice == "бумага":
        await message.answer("вы выиграли")
    if botchoice == "камень":
        await message.answer("вы проиграли")
    if botchoice == "ножницы":
        await message.answer("ничья")
@dp.message(F.text == "бумага")
async def c(message:types.Message):
    if botchoice == "бумага":
        await message.answer("ничья")
    if botchoice == "ножницы":
        await message.answer("вы проиграли")
    if botchoice == "камень":
        await message.answer("Вы выиграли")

@dp.message(F.text == "камень")
async def c(message:types.Message):
    if botchoice == "бумага":
        await message.answer("вы проиграли")
    if botchoice == "ножницы":
        await message.answer("вы выиграли")
    if botchoice == "камень":
        await message.answer("ничья")
async def main():
    print("Запукс Бота")
    await dp.start_polling(bot)

asyncio.run(main())
