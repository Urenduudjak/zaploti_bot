from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from data.config import ADMINS
import logging
admin = ADMINS

# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
        except Exception as err:
            logging.exception(err)
