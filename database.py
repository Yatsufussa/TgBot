import sqlite3

# Create/login to database
connection = sqlite3.connect("dostavka.db")

# Creating translator
sql = connection.cursor()

# Creating table
#sql.execute("CREATE TABLE users (id INTEGER, name TEXT, phone_number TEXT,loc_lat REAL,loc_long REAL, gender TEXT);")

def add_user(user_id, name, phone_number, latitude, longitude, gender):
   # Create/login to database
   connection = sqlite3.connect("dostavka.db")
   # Creating translator
   sql = connection.cursor()
   # Adding user into database
   sql.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?);", (user_id, name, phone_number, latitude, longitude, gender))

   #fixiruem obnovleniye
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

delete_user()