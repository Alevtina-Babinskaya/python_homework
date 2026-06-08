import sqlite3

try:
    with sqlite3.connect('../db/magazines.db') as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Publishers (
                        publisher_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL UNIQUE 
                        )
                        """)
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Magazines (
                       magazine_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL UNIQUE,
                       publisher_id INTEGER,
                       FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id) 
                       )
                       """)
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Subscribers (
                       subscriber_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       address TEXT
                       )
                       """)
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Subscriptions (
                       subscription_id INTEGER PRIMARY KEY,
                       magazine_id INTEGER,
                       subscriber_id INTEGER,
                       FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
                       FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id)
                       )
                       """)

        print('Tables created')



except sqlite3.Error as e:
    print(f"Something went wrong: {e}")

def add_publisher (cursor, name):   
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazine(cursor, name, publisher):
    try:
        cursor.execute("SELECT * FROM Publishers WHERE name = ?", (publisher,))
        results = cursor.fetchall()
        if len(results) > 0:
            publisher_id = results[0][0]
        else:
            print(f"There was no publisher named {publisher}.")
            return
        cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscriber (cursor, name, address):
    try:
       cursor.execute("SELECT * FROM Subscribers WHERE name = ?", (name,))
       results = cursor.fetchall()
       if len(results) > 0:
           for row in results:
               if row[2] == address:
                    print('This record already exists')
                    return
       cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscription (cursor, subscriber, magazine):
    try:
        cursor.execute("SELECT * FROM Subscribers WHERE name = ?", (subscriber,))
        results = cursor.fetchall()
        if len(results) > 0:
            subscriber_id = results[0][0]
        else:
            print(f"There is no subscriber named {subscriber}")
            return
        cursor.execute("SELECT * FROM Magazines WHERE name = ?", (magazine,))
        results = cursor.fetchall()
        if len(results) > 0:
            magazine_id = results[0][0]
        else:
            print(f"There is no magazine named {magazine}")
            return
        cursor.execute("INSERT INTO Subscriptions (magazine_id, subscriber_id) VALUES (?, ?)", (magazine_id, subscriber_id))
    except sqlite3.IntegrityError:
        print("subscription is already in the database.")

add_publisher(cursor, "Tech Media")
add_publisher(cursor, "Nature Press")
add_publisher(cursor, "Global Science")
add_publisher(cursor, "Travel World")

add_magazine(cursor, "Python Monthly", "Tech Media")
add_magazine(cursor, "AI Today", "Tech Media")
add_magazine(cursor, "Nature Weekly", "Nature Press")
add_magazine(cursor, "Science Digest", "Global Science")
add_magazine(cursor, "Traveler", "Travel World")

add_subscriber(cursor, "Alice Johnson", "123 Main St")
add_subscriber(cursor, "Bob Smith", "456 Oak Ave")
add_subscriber(cursor, "Carol Davis", "789 Pine Rd")
add_subscriber(cursor, "David Wilson", "101 Maple Dr")

add_subscription(cursor, "Alice Johnson", "Python Monthly")
add_subscription(cursor, "Alice Johnson", "AI Today")
add_subscription(cursor, "Bob Smith", "Nature Weekly")
add_subscription(cursor, "Carol Davis", "Science Digest")
add_subscription(cursor, "Carol Davis", "Traveler")
add_subscription(cursor, "David Wilson", "Python Monthly")

conn.commit() 
try:      
    cursor.execute("SELECT * FROM Subscribers")
    result = cursor.fetchall()
    for row in result:
        print(row) 

    cursor.execute("SELECT * FROM Magazines ORDER BY name")
    result = cursor.fetchall()
    for row in result:
        print(row) 

    cursor.execute("""SELECT Magazines.name FROM Magazines JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id WHERE Publishers.name = ?""", ("Tech Media",))
    result = cursor.fetchall()
    for row in result:
        print(row) 
        
except sqlite3.IntegrityError as e:
    print(e)