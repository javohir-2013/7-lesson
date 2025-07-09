from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import asyncio
from handler import setup_message_routers

API_TOKEN = "7780165947:AAEJuiZK-zBsiK2Y5zyd5SN-Jl64MhkAhu0"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("help"))
async def start_bot(message: types.Message):
    await message.answer(text="""UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. 

Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. 

E'lon berish: @UstozShogirdBot

Admin @UstozShogirdAdminBot""")


async def on_start_up(dispatcher: Dispatcher):
    await bot.send_message(chat_id="424550064",
                           text="Bot ishga tushdi")


async def main():
    handler_router = setup_message_routers()
    dp.include_router(handler_router)

    dp.startup.register(on_start_up)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
