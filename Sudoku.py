import mysql.connector
import os

def create_connection():
    conn = mysql.connector.connect(
      host=os.getenv("DB_HOST"), # Environmental variables hold the keys
      user=os.getenv("DB_USER"),
      password=os.getenv("DB_PASSWORD"),
      database=os.getenv("DB_DATABASE")
    )
    return conn

def setup_db():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE transactions
        (id INT AUTO_INCREMENT PRIMARY KEY, sender_account_id VARCHAR(255), receiver_account_id VARCHAR(255), amount FLOAT)
    ''')
    conn.commit()
    conn.close()

def create_transaction(sender: str, receiver: str, amount: int):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO transactions (sender_account_id, receiver_account_id, amount) VALUES (%s, %s, %s)",
              (sender, receiver, amount))
    conn.commit()
    conn.close()

def get_transaction_history():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    conn.close()
    return transactions


