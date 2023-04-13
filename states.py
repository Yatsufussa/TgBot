from aiogram.dispatcher.filters.state import State, StatesGroup


# Registration Proccess
class Registration(StatesGroup):
    get_name_state = State()
    get_phone_number_state = State()
    get_location_state = State()
    get_gender = State()


# Choosing Products proccess pr = product
class GetProduct(StatesGroup):
    get_pr_name = State()
    get_pr_count = State()


# Products basket
class Cart(StatesGroup):
    more_pr = State()
    more_pr_num = State()


# Registration of products
class Order(StatesGroup):
    wait_location = State()
    wait_pay_type = State()
    wait_accept = State()
