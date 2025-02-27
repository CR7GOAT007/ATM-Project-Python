import tkinter as tk
from tkinter import messagebox

# Sample user data (Card Number, PIN, and Balance)
users = {
    "123456": {"pin": "7890", "balance": 5000, "history": []},
    "654321": {"pin": "1234", "balance": 3000, "history": []}
}

class ATMSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern ATM System")
        self.root.configure(bg="#f0f0f0")

        self.current_user = None
        
        self.login_screen()
    
    def login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Card Number:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=10)

        self.card_entry = tk.Entry(self.root)
        self.card_entry.pack()
        
        tk.Label(self.root, text="PIN:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=10)

        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack()
        
        tk.Button(self.root, text="Login", command=self.authenticate, bg="#4CAF50", fg="white", font=("Helvetica", 12)).pack(pady=20)

    
    def authenticate(self):
        card = self.card_entry.get()
        pin = self.pin_entry.get()
        
        if card in users and users[card]["pin"] == pin:
            self.current_user = card
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid Card Number or PIN")
    
    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Welcome to Modern ATM", bg="#f0f0f0", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self.root, text="Check Balance", command=self.check_balance, bg="#2196F3", fg="white", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(self.root, text="Deposit", command=self.deposit, bg="#2196F3", fg="white", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(self.root, text="Withdraw", command=self.withdraw, bg="#2196F3", fg="white", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(self.root, text="Transaction History", command=self.transaction_history, bg="#2196F3", fg="white", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(self.root, text="Logout", command=self.login_screen, bg="#f44336", fg="white", font=("Helvetica", 12)).pack(pady=20)

    
    def check_balance(self):
        balance = users[self.current_user]["balance"]
        messagebox.showinfo("Balance", f"Your balance is: ${balance}")
    
    def deposit(self):
        self.transaction_screen("Deposit")
    
    def withdraw(self):
        self.transaction_screen("Withdraw")
    
    def transaction_screen(self, transaction_type):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text=f"Enter amount to {transaction_type.lower()}:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=10)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        
        tk.Button(self.root, text=transaction_type, command=lambda: self.process_transaction(transaction_type), bg="#4CAF50", fg="white", font=("Helvetica", 12)).pack(pady=10)

        tk.Button(self.root, text="Back", command=self.main_menu).pack()
    
    def process_transaction(self, transaction_type):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return
        
        if transaction_type == "Withdraw" and amount > users[self.current_user]["balance"]:
            messagebox.showerror("Error", "Insufficient funds")
            return
        
        if transaction_type == "Deposit":
            users[self.current_user]["balance"] += amount
            users[self.current_user]["history"].append(f"Deposited ${amount}")
        else:
            users[self.current_user]["balance"] -= amount
            users[self.current_user]["history"].append(f"Withdrew ${amount}")
        
        messagebox.showinfo("Success", f"{transaction_type} Successful")
        self.main_menu()
    
    def transaction_history(self):
        history = "\n".join(users[self.current_user]["history"] or ["No transactions yet"])
        messagebox.showinfo("Transaction History", history)

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMSystem(root)
    root.mainloop()
