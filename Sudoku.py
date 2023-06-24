import sqlite3

def setup_db():
    conn = sqlite3.connect('banking.db')  # creates a file named 'banking.db' in your local directory
    c = conn.cursor()
    c.execute('''
        CREATE TABLE transactions
        (id INTEGER PRIMARY KEY, sender_account_id TEXT, receiver_account_id TEXT, amount REAL)
    ''')
    conn.commit()
    conn.close()

def create_transaction(sender, receiver, amount):
    conn = sqlite3.connect('banking.db')
    c = conn.cursor()
    c.execute("INSERT INTO transactions (sender_account_id, receiver_account_id, amount) VALUES (?, ?, ?)",
              (sender, receiver, amount))
    conn.commit()
    conn.close()

def get_transaction_history():
    conn = sqlite3.connect('banking.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    conn.close()
    return transactions
