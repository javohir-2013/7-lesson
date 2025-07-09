from aiogram import Router
from . import start, sherik_kerak, ish_joyi_kerak,hodim_kerak


def setup_message_routers():
    router = Router()
    router.include_router(start.router)
    router.include_router(sherik_kerak.router)
    router.include_router(ish_joyi_kerak.router)
    router.include_router(hodim_kerak.router)
    return router

