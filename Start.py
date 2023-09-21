from Sudoku import get_transaction_history
from Sudoku import create_transaction
import tkinter as tk

def on_button1_click():
    # This will call the create_transaction function when Button 1 is clicked
    create_transaction()

def on_button2_click():
    # This will call the get_transaction_history function when Button 2 is clicked
    get_transaction_history()

# Create the main window
root = tk.Tk()
root.title("Transaction GUI")

# Add a button and link it to the on_button1_click function
button1 = tk.Button(root, text="Create Transaction", command=on_button1_click)
button1.pack(pady=20)

# Add another button and link it to the on_button2_click function
button2 = tk.Button(root, text="Get Transaction History", command=on_button2_click)
button2.pack(pady=20)

# Start the main loop to display the window
root.mainloop()
