import utils
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import WebAppInfo
from aiogram.filters import CommandObject, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ChatMemberStatus
import json
import asyncio
from config import qw

from misc import dp, bot
from aiogram import F, types

queue = asyncio.Queue()

async def worker():
    """Воркер, который обрабатывает задачи из очереди."""
    while True:
        url, user_id, message = await queue.get()
        await message.answer(text=f"Начинаю работу с URL: {url}")
        try:
            with open('settings.json', 'r') as f:
                data = json.load(f)

            filename = await utils.main(url=url, save=data['save'], id=user_id)
            await message.answer_document(types.FSInputFile(filename))
            await message.answer("Готово!")
        except Exception as e:
            await message.answer(f"Ошибка: {e}")
        finally:
            queue.task_done()

async def on_startup(dispatcher):
    asyncio.create_task(worker())

@dp.message(Command('start'))
async def start(message: Message, state: FSMContext) -> None:
    with open('settings.json', 'r') as f:
        data = json.load(f)
    
    if message.from_user.id in data['admins']:
        text = f"Добро пожаловать, укажи своё действие.\nПоследнее обновление данных в файле было: {data['date']}"
        btn = InlineKeyboardBuilder().add(
            types.InlineKeyboardButton(text='🚀 Начать', callback_data='start')
        ).row(
            types.InlineKeyboardButton(text='🪬 Получить последний файл', callback_data="last_file"),
            types.InlineKeyboardButton(text="⚙️ Настройки", callback_data='settings')
        ).as_markup()

        await state.set_state(utils.Start.url)
        await message.answer(text=text, reply_markup=btn)

@dp.message(utils.Start.url)
async def add_to_queue(message: Message, state: FSMContext) -> None:
    if message.from_user.id in qw:
        await message.answer(text="Вы уже стоите в очереди, ожидайте.")
        return
    # print(queue)
    # qw.append(message.from_user.id)
    url = message.text
    await state.clear()
    await message.delete()

    await queue.put((url, message.from_user.id, message))