import asyncio
from aiogram import Dispatcher, Bot

import bot_commands


with open('.env', 'r') as f:
    TOKEN = f.readline()


async def main() -> None:
    bot = Bot(token=TOKEN, parse_mode='HTML')

    dp = Dispatcher()

    dp.include_router(bot_commands.router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())