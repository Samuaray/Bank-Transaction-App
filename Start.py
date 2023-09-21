from Sudoku import get_transaction_history
from Sudoku import create_transaction
from Sudoku import create_connection
import tkinter as tk


def on_button1_click():
    # This will call the create_transaction function when Button 1 is clicked
    create_connection()
    create_transaction("bob", "gary", 5000)

def on_button2_click():
    # This will call the get_transaction_history function when Button 2 is clicked
    transactions = get_transaction_history()
    for transaction in transactions:
        text_widget.insert(tk.END, str(transaction) + "\n")

# Create the main window
root = tk.Tk()
root.title("Transaction GUI")

# Add a button and link it to the on_button1_click function
button1 = tk.Button(root, text="Create Transaction", command=on_button1_click)
button1.pack(pady=20)

# Add another button and link it to the on_button2_click function
button2 = tk.Button(root, text="Get Transaction History", command=on_button2_click)
button2.pack(pady=20)

# Create a text widget to display the transaction history
text_widget = tk.Text(root, height=10, width=50)
text_widget.pack(pady=20)

# Start the main loop to display the window
root.mainloop()
