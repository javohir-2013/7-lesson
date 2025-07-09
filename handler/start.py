from aiogram import types, Router
from aiogram.filters import Command
from keyboard.default import main_menu

router = Router()


@router.message(Command("start"))
async def start_bot(message: types.Message):
    await message.answer(text="""Assalom alaykum Zilola
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!
/help so'zini yozing""",
                         reply_markup=main_menu())

