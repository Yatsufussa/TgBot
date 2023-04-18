import sqlite3

# Create/login to database
connection = sqlite3.connect("dostavka.db")

# Creating translator
sql = connection.cursor()


# Creating table
# sql.execute("CREATE TABLE users (id INTEGER, name TEXT, phone_number TEXT,loc_lat REAL,loc_long REAL, gender TEXT);")

def add_user(user_id, name, phone_number, latitude, longitude, gender):
    # Create/login to database
    connection = sqlite3.connect("dostavka.db")
    # Creating translator
    sql = connection.cursor()
    # Adding user into database
    sql.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?);",
                (user_id, name, phone_number, latitude, longitude, gender))

    # fixiruem obnovleniye
    connection.commit()


# Getting user
def get_users():
    # Create/login to database
    connection = sqlite3.connect("dostavka.db")
    # Creating translator
    sql = connection.cursor()
    users = sql.execute("SELECT name,id FROM users;")
    return users.fetchall()


# Request for deleting from database
def delete_user():
    # Create/login to database
    connection = sqlite3.connect("dostavka.db")
    # Creating translator
    sql = connection.cursor()

    # Sending request for deleting
    sql.execute("DELETE FROM users;")
    # Fixing update
    connection.commit()


# sql.execute("CREATE TABLE products (product_name TEXT, product_cost REAL, product_info TEXT,product_picture TEXT);")

def add_product(product_name, product_cost, product_info, product_picture):
    # Create/login to database
    connection = sqlite3.connect("dostavka.db")
    # Creating translator
    sql = connection.cursor()
    # Adding user into database
    sql.execute("INSERT INTO products VALUES (?,?,?,?);", (product_name, product_cost, product_info, product_picture))

    # fixiruem obnovleniye
    connection.commit()


def get_product_name():
    connection = sqlite3.connect("dostavka.db")
    sql = connection.cursor()
    product_name = sql.execute("SELECT product_name FROM products;")
    return product_name.fetchall()


def get_all_products(current_product):
    connection = sqlite3.connect("dostavka.db")
    sql = connection.cursor()
    all_products = sql.execute("SELECT * FROM products WHERE product_name = ?;", (current_product,))
    return all_products.fetchall()


# Func for checking user in consistency into database
def check_user(user_id):
    connection = sqlite3.connect("dostavka.db")
    sql = connection.cursor()
    checker = sql.execute("SELECT id FROM users WHERE id = ?;", (user_id,))

    if checker.fetchone():
        return True
    else:
        return False


# Create table of cart columns (USER ID, PRODUCT NAME, PRODUCT COUNT )
# Create a function of adding into cart
# Create a function of cart of an user WHERE USER ID =? into cart

# sql.execute("CREATE TABLE carts (user_id INTEGER, product_name TEXT, product_count INTEGER);")
def cart_add(user_id, product_name, product_count):
    connection = sqlite3.connect("dostavka.db")
    sql = connection.cursor()
    cart = sql.execute("INSERT INTO carts VALUES (?,?,?)", (user_id, product_name, product_count))
    connection.commit()


def get_cart(user_id):
    connection = sqlite3.connect("dostavka.db")
    sql = connection.cursor()
    cart_get = sql.execute("SELECT * FROM carts WHERE user_id=?", (user_id,))
    return cart_get.fetchall()


def delete_cart(user_id):
    connection = sqlite3.connect("dostavka.db")
    sql = connection.cursor()
    cart_delete = sql.execute("DELETE FROM carts WHERE user_id = ?", (user_id,))
    connection.commit()

