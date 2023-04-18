import state
from aiogram import Dispatcher, Bot, executor
import buttons
from aiogram.types import ReplyKeyboardRemove
from state import Registration, Order, GetProduct, Cart
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import database

bot = Bot("5801401239:AAH0A4dIoentafuDYpd7FlMNdzRE7lcrxyk")
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_command(message):
    start_text = f"Hello {message.from_user.first_name}\nIm delivery Bot!"
    await message.answer(start_text)
    user_id = message.from_user.id
    checker = database.check_user(user_id)

    # If user already registered in database so we send menu

    if checker:
        await message.answer("Choose product", reply_markup=buttons.products_kb())
    else:
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
    user_number = message.contact.phone_number
    await state.update_data(phone_number=user_number)
    await message.answer('Share location now', reply_markup=buttons.location_kb())
    await Registration.get_location_state.set()


@dp.message_handler(state=Registration.get_location_state, content_types=['location'])
async def user_location(message, state=Registration.get_location_state):
    user_location = (message.location.latitude, message.location.longitude)
    await state.update_data(coordinates=user_location)
    await message.answer("Location accepted!", reply_markup=buttons.gender_kb())
    await Registration.get_gender_state.set()


@dp.message_handler(state=Registration.get_gender_state, content_types=['text'])
async def user_gender(message, state=Registration.get_gender_state):
    user_gender = message.text
    await state.update_data(gender=user_gender)
    await message.answer("Registration completed!", reply_markup=buttons.gender_kb())
    # Saving user into database
    all_info = await state.get_data()
    name = all_info.get('name')
    phone_number = all_info.get('number')
    latitude = all_info.get('latitude')
    longitude = all_info.get('longitude')
    gender = user_gender
    user_id = message.from_user.id

    database.add_user(user_id, name, phone_number, latitude, longitude, gender)
    print(database.get_users())
    await state.finish()


# Independent handler for main menu text
@dp.message_handler(content_types=['text'])
async def text_messages(message):
    user_answer = message.text
    # Actual list of products
    actual_product = [i[0] for i in database.get_product_name()]
    if user_answer == "Cart":
        await message.answer("Your Cart")

    elif user_answer == "Make an order":
        await message.answer("Make an order")  # оформить заказ

    # If sent message = is product
    elif user_answer in actual_product:
        await message.answer("Choose the amount", reply_markup=buttons.product_count())
        await dp.current_state(user=message.from_user.id).update_data(user_product=message.text)
        await GetProduct.get_pr_count.set()
    else:
        await message.text("Choose the product from the menu!", reply_markup=buttons.products_kb())


# SAVing users product amount input
@dp.message_handler(state=GetProduct.get_pr_count, content_types=['text'])
async def pr_count(message):
    user_prnumber = message.text
    await message.answer('Smth else?', reply_markup=buttons.products_kb())

    print(user_prnumber)


executor.start_polling(dp)
