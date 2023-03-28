import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from gpt_model import gpt_responce
from utils import config_reader

# Логирование на уровне INFO
logging.basicConfig(level=logging.INFO)

token = config_reader('Telegram', 'token')

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.answer('Hello, write me a question and I will try to answer it!')

@dp.message_handler(content_types=['text'])
async def GPt_answer(message: types.Message):
    user_id = message.from_user.id
    await message.answer(gpt_responce(user_id, message.text))

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())