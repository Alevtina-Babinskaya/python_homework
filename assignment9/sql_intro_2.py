import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    #sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    #JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    sql_statement = """SELECT line_items.line_item_id, line_items.quantity, line_items.product_id, products.product_name, products.price FROM line_items JOIN products ON line_items.product_id = products.product_id"""

    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())
    df['total'] = df['quantity'] * df['price']
    print(df.head())
    df = df.groupby('product_id').agg({'line_item_id': 'count', 'total': 'sum', 'product_name': 'first'})
    print(df.head())
    df.sort_values(by='product_name', ascending=True, inplace=True)
    print(df.head())
    df.to_csv('order_summary.csv')

