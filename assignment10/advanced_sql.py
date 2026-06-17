import sqlite3
import os

path = "../db/lesson.db"
#task 1
conn = sqlite3.connect(path)
cursor = conn.cursor()

query = """SELECT l.order_id, SUM(p.price * l.quantity) AS total_price 
FROM orders AS o JOIN line_items AS l ON o.order_id = l.order_id JOIN products as p ON l.product_id = p.product_id 
GROUP BY l.order_id ORDER BY l.order_id LIMIT 5;"""
cursor.execute(query)
result = cursor.fetchall()
print(result)
conn.close()


# task 2 
conn = sqlite3.connect(path)
cursor = conn.cursor()
query = """SELECT c.customer_name, AVG(total_price) AS average_total_price 
FROM customers AS c LEFT JOIN 
(SELECT o.customer_id AS customer_id_b, SUM(p.price * l.quantity) AS total_price FROM products AS p 
JOIN line_items AS l ON l.product_id = p.product_id 
JOIN orders AS o ON l.order_id = o.order_id GROUP BY l.order_id) AS order_totals ON c.customer_id = order_totals.customer_id_b
GROUP BY c.customer_id; 
"""
cursor.execute(query)
result = cursor.fetchall()
print(result)
conn.close()

# task 3
conn = sqlite3.connect(path)
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.execute("SELECT customer_id FROM customers WHERE customers.customer_name = ?;", ('Perez and Sons',))
customer_id = cursor.fetchone()[0]
cursor = conn.execute("SELECT employee_id FROM employees WHERE employees.first_name = ? AND employees.last_name = ?;", ('Miranda', 'Harris'))
employee_id = cursor.fetchone()[0]
cursor = conn.execute("SELECT product_id FROM products ORDER BY products.price ASC LIMIT 5") 
product_ids = cursor.fetchall()

try:
    cursor.execute("INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id;", (customer_id, employee_id) )
    order_id = cursor.fetchone()[0]
    for product_id in product_ids:
        cursor.execute("INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?);", (order_id, product_id[0], 10))
    conn.commit()  
except Exception as e:
    conn.rollback()  
    print("Error:", e)
conn.close()

conn = sqlite3.connect(path)
cursor = conn.cursor()
query = """SELECT l.line_item_id, l.quantity, p.product_name FROM line_items AS l JOIN products AS p ON l.product_id = p.product_id WHERE l.order_id = ?"""
cursor = conn.execute(query, (order_id,)) 
print(cursor.fetchall())
conn.close()

# task 4
conn = sqlite3.connect(path)
cursor = conn.cursor()
query = """SELECT (e.first_name || ' ' || e.last_name) AS employee_name, COUNT(o.order_id) AS orders_count FROM Employees AS e 
JOIN orders AS o ON e.employee_id = o.employee_id GROUP BY e.employee_id HAVING COUNT(o.order_id) > 5;"""
cursor = conn.execute(query)
print(cursor.fetchall())
conn.close()