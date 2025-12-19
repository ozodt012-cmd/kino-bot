from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = "8379812587:AAGMO8Q1jBX7iipwC4lYExvcnzf8LWR9V4E"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Salom! 🎬\nKino kodini yoz (masalan: 101)")

@dp.message_handler()
async def send_movie(message: types.Message):
    if message.text == "101":
        await message.answer_video("1003345975608")
    else:
        await message.answer("❌ Bunday kod yo‘q")

if name == "main":
    executor.start_polling(dp)