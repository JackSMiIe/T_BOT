from aiogram import Dispatcher,Bot
from aiogram.types import Message
import asyncio
import os
from dotenv import load_dotenv
from aiogram import F


load_dotenv()
dp = Dispatcher()
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))

@dp.message(F.text == '/start')
async def start(message: Message) -> None:
    await message.answer(f'Привет, {message.chat.username}!\n'
                         f'Давай хуярить' )

@dp.message(F.text & F.text.startswith('a') & F.chat.username == 'ManyJackSMile')
async def answer_a(message: Message) -> None:
    await message.answer('Ты написал букву А')

@dp.message(F.photo)
async def photo(message: Message) -> None:
    await message.answer("Ты отправил фото")






async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())