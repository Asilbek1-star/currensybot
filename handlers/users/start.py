
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp,user_db,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        telegram_id=message.from_user.id
        username=message.from_user.username
        if not user_db.add_user(telegram_id=telegram_id):
            user_db.add_user(telegram_id=telegram_id,username=username)


            count=user_db.count_users()
            text="Yana yangi foydalanuvchi qo`shildi\n"
            text+=f"bazada {count} ta foydalanuvchi bor\n"
            await bot.send_message(ADMINS[0],text)

        await message.answer("Xush kelibsan")
    except Exception as err:
        print(err)

