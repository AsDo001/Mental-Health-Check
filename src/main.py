import asyncio
import logging
import sys


from loader import dp, bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

@dp.message(Command('help'))
async def cmd_start_2(message: Message):
    await message.answer('test')

async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # import uvloop
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())