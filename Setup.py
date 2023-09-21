import mysql.connector

def setup_db():
    conn = mysql.connector.connect()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE transactions
        (id INT AUTO_INCREMENT PRIMARY KEY, sender_account_id VARCHAR(255), receiver_account_id VARCHAR(255), amount FLOAT)
    ''')
    conn.commit()
    conn.close()




setup_db()
