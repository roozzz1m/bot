from aiogram import Bot, Dispatcher
from aiogram import Bot, Dispatcher, Router
from config import TOKEN
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder

dp = Dispatcher()
form_router = Router()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


