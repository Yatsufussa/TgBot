from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import database


# Button for sending phone number
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Share number", request_contact=True)
    kb.add(button)
    return kb


# Button for sending location
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Location", request_location=True)
    kb.add(button)
    return kb


# Buttons for sending gender
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Male")
    button2 = KeyboardButton("Female")
    kb.add(button, button2)
    return kb


# Proccess for products counting
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [KeyboardButton(str(i)) for i in range(1, 10)]
    back = KeyboardButton("Back")
    kb.add(*buttons, back)
    return kb


# Buttons with product names
def products_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    cart = KeyboardButton("Cart")
    order = KeyboardButton("Make an order")

    all_products = database.get_product_name()

    # Making list of buttons with product names
    buttons = [KeyboardButton(i[0]) for i in all_products]
    kb.add(*buttons)
    kb.add(cart, order)
    return kb


# Button for cart
def cart():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Clear")
    button2 = KeyboardButton("Make an orded")
    button3 = KeyboardButton("Change")
    button4 = KeyboardButton("Back")
    kb.add(button, button2, button3, button4)
    return kb


# Buttons for payment type
def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Cash")
    button2 = KeyboardButton("Credit Card")
    button3 = KeyboardButton("Back")
    kb.add(button, button2, button3)
    return kb


# Buttons for Accepting an order
def confirmation():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Confirm")
    button2 = KeyboardButton("Cancel")
    button3 = KeyboardButton("Back")
    kb.add(button, button2, button3)
    return kb
