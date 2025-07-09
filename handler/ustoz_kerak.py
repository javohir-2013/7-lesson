
from aiogram import types, Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from keyboard.default import main_menu
from states.user import UserState


router = Router()


@router.message(Command("ustoz kerak"))
async def start_bot(message: types.Message):
    await message.answer(text="""Ustoz topish uchun ariza berish

Hozir sizga birnecha savollar beriladi.
Har biriga javob bering.
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""",
                         reply_markup=main_menu())


@router.message(F.text == "User")
async def start_bot(message: types.Message, state: FSMContext):
    await message.answer(text="Ismingizni kiriting",
                         reply_markup=main_menu())
    await state.set_state(UserState.name)


@router.message(StateFilter(UserState.name))
async def start_bot(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="Yoshingizni kiriting",
                         reply_markup=main_menu())
    await state.set_state(UserState.age)


@router.message(StateFilter(UserState.age))
async def start_bot(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)

    await message.answer(text="email kiriting",
                         reply_markup=main_menu())
    await state.set_state(UserState.email)


@router.message(StateFilter(UserState.email))
async def start_bot(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    email = message.text

    await message.answer(text=f"Foydalanuvchining ismi {name}\n"
                              f"Yoshi {age}, uning emailli {email}",
                         reply_markup=main_menu())
    await state.clear()


