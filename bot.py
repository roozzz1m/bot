import asyncio
import logging
import sys
import aiogram
from misc import dp, form_router, bot

import admins
import commands
import buttons

async def main(bot, dp) -> None:
    await commands.on_startup(dispatcher=dp)
    await bot(aiogram.methods.DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)
 
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(bot=bot, dp=dp))
    
