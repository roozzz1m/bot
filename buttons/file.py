import utils
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import WebAppInfo
from aiogram.filters import CommandObject, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ChatMemberStatus
import json
from openpyxl import load_workbook
from config import qw

from misc import dp, bot
from aiogram import F, types

@dp.callback_query(F.data == "last_file")
async def last_file(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer_document(types.FSInputFile('artists.xlsx'))

@dp.callback_query(F.data == "start")
async def start(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id in qw:
        await callback.answer(text="Вы уже стоите в очереди, ожидайте.", show_alert=True)

    await callback.answer(text="Отправь ссылку в данный чат.", show_alert=True)
    await state.set_state(utils.Start.url)


