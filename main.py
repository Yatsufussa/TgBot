import state
from aiogram import Dispatcher, Bot, executor
import buttons
from aiogram.types import ReplyKeyboardRemove
from state import Registration, Order, GetProduct, Cart
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot("5801401239:AAH0A4dIoentafuDYpd7FlMNdzRE7lcrxyk")
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_command(message):
    start_text = f"Hello {message.from_user.first_name}\nIm delivery Bot!"
    user_id = (message.from_user.id)
    print(user_id)
    await message.answer(start_text)
    await message.answer("Registration\nWrite your name please:", reply_markup=ReplyKeyboardRemove())
    await Registration.get_name_state.set()


@dp.message_handler(state=Registration.get_name_state, content_types=['text'])
async def user_name(message, state=Registration.get_name_state):
    name = message.text
    await state.update_data(user_name=name)
    await message.answer("Send now phone number", reply_markup=buttons.phone_number_kb())
    await Registration.get_phone_number_state.set()


@dp.message_handler(state=Registration.get_phone_number_state, content_types=['contact'])
async def user_number(message, state=Registration.get_phone_number_state):
    await state.update_data(phone_number=user_number)
    await message.answer('Share location now', reply_markup=buttons.location_kb())
    await Registration.get_location_state.set()


@dp.message_handler(state=Registration.get_location_state, content_types=['location'])
async def user_location(message, state=Registration.get_location_state):
    user_location = (message.location.latitude, message.location.longitude)
    await  state.update_data(coordinates=user_location)
    await message.answer("Location accepted!", reply_markup=buttons.gender_kb())
    await Registration.get_gender_state.set()


@dp.message_handler(state=Registration.get_gender_state, content_types=['text'])
async def user_gender(message, state=Registration.get_gender_state):
    await state.up


executor.start_polling(dp)
