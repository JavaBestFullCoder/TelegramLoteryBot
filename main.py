import asyncio

from dispatcher import dp, bot
import handlers

async def main():
    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())