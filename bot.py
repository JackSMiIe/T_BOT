from aiogram import Dispatcher,Bot
from aiogram.types import Message
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()
dp = Dispatcher()
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))

@dp.message()
async def echo(message: Message) -> None:
    await message.answer(text=f'{message.chat.full_name}')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())