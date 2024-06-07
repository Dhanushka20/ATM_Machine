import tkinter as tk
from tkinter import messagebox
import os

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM")
        self.root.geometry("400x300")
        
        self.accounts = []
        self.account = None
        self.account_position = None
        self.num_of_tries = 5

        self.load_accounts()
        self.create_login_frame()
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def load_accounts(self):
        if os.path.exists("account.txt"):
            with open("account.txt", "r") as f:
                for line in f:
                    pin, balance, name = line.strip().split(', ')
                    account = {
                        "pin": int(pin),
                        "balance": float(balance),
                        "name": name
                    }
                    self.accounts.append(account)
        else:
            messagebox.showinfo("No Accounts Found", "No accounts found. Please create an account.")
            self.create_account()
    
    def save_accounts(self):
        with open("account.txt", "w") as f:
            for account in self.accounts:
                f.write(f"{account['pin']}, {account['balance']}, {account['name']}\n")
    
    def create_login_frame(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        label = tk.Label(frame, text="Please log in using your 4-digit PIN")
        label.pack(pady=10)
        
        self.pin_entry = tk.Entry(frame, show="*")
        self.pin_entry.pack(pady=10)
        
        login_button = tk.Button(frame, text="Login", command=self.login)
        login_button.pack(pady=10)
    
    def login(self):
        input_pin = self.pin_entry.get()
        
        if input_pin.isdigit():
            input_pin = int(input_pin)
        else:
            messagebox.showerror("Invalid Input", "Please enter a 4-digit PIN.")
            return
        
        self.account = None
        
        for i, a in enumerate(self.accounts):
            if a["pin"] == input_pin:
                self.account = a
                self.account_position = i
                break
        
        if self.account:
            self.create_main_menu_frame()
        else:
            self.num_of_tries -= 1
            if self.num_of_tries == 0:
                messagebox.showerror("Too Many Attempts", "You have exceeded the maximum number of tries.")
                self.root.quit()
            else:
                messagebox.showerror("Login Failed", f"Incorrect PIN. You have {self.num_of_tries} attempts remaining.")
                self.pin_entry.delete(0, tk.END)
    
    def create_main_menu_frame(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        label = tk.Label(frame, text=f"Welcome, {self.account['name']}")
        label.pack(pady=10)
        
        balance_button = tk.Button(frame, text="Balance Inquiry", command=self.balance_inquiry)
        balance_button.pack(pady=5)
        
        withdraw_button = tk.Button(frame, text="Withdrawal", command=self.withdraw)
        withdraw_button.pack(pady=5)
        
        deposit_button = tk.Button(frame, text="Deposit", command=self.deposit)
        deposit_button.pack(pady=5)
        
        change_pin_button = tk.Button(frame, text="Change PIN", command=self.change_pin)
        change_pin_button.pack(pady=5)
        
        logout_button = tk.Button(frame, text="Logout", command=self.create_login_frame)
        logout_button.pack(pady=5)
    
    def balance_inquiry(self):
        messagebox.showinfo("Balance Inquiry", f"Your current balance is: {self.account['balance']}")
    
    def withdraw(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        label = tk.Label(frame, text="Enter the amount you wish to withdraw")
        label.pack(pady=10)
        
        self.withdraw_entry = tk.Entry(frame)
        self.withdraw_entry.pack(pady=10)
        
        withdraw_button = tk.Button(frame, text="Withdraw", command=self.process_withdraw)
        withdraw_button.pack(pady=10)
        
        back_button = tk.Button(frame, text="Back", command=self.create_main_menu_frame)
        back_button.pack(pady=10)
    
    def process_withdraw(self):
        withdraw_amount = self.withdraw_entry.get()
        
        if withdraw_amount.isdigit():
            withdraw_amount = float(withdraw_amount)
            if withdraw_amount <= self.account['balance']:
                self.account['balance'] -= withdraw_amount
                self.accounts[self.account_position] = self.account
                self.save_accounts()
                messagebox.showinfo("Transaction Successful", f"Withdrawn: {withdraw_amount}\nRemaining balance: {self.account['balance']}")
                self.create_main_menu_frame()
            else:
                messagebox.showerror("Transaction Failed", "Insufficient funds.")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")
    
    def deposit(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        label = tk.Label(frame, text="Enter the amount you wish to deposit")
        label.pack(pady=10)
        
        self.deposit_entry = tk.Entry(frame)
        self.deposit_entry.pack(pady=10)
        
        deposit_button = tk.Button(frame, text="Deposit", command=self.process_deposit)
        deposit_button.pack(pady=10)
        
        back_button = tk.Button(frame, text="Back", command=self.create_main_menu_frame)
        back_button.pack(pady=10)
    
    def process_deposit(self):
        deposit_amount = self.deposit_entry.get()
        
        if deposit_amount.isdigit():
            deposit_amount = float(deposit_amount)
            self.account['balance'] += deposit_amount
            self.accounts[self.account_position] = self.account
            self.save_accounts()
            messagebox.showinfo("Transaction Successful", f"Deposited: {deposit_amount}\nUpdated balance: {self.account['balance']}")
            self.create_main_menu_frame()
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")
    
    def change_pin(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        label = tk.Label(frame, text="Enter your new 4-digit PIN")
        label.pack(pady=10)
        
        self.new_pin_entry = tk.Entry(frame, show="*")
        self.new_pin_entry.pack(pady=10)
        
        change_pin_button = tk.Button(frame, text="Change PIN", command=self.process_change_pin)
        change_pin_button.pack(pady=10)
        
        back_button = tk.Button(frame, text="Back", command=self.create_main_menu_frame)
        back_button.pack(pady=10)
    
    def process_change_pin(self):
        new_pin = self.new_pin_entry.get()
        
        if new_pin.isdigit() and len(new_pin) == 4:
            self.account['pin'] = int(new_pin)
            self.accounts[self.account_position] = self.account
            self.save_accounts()
            messagebox.showinfo("PIN Change Successful", f"Your new PIN is: {self.account['pin']}")
            self.create_main_menu_frame()
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid 4-digit PIN.")
    
    def create_account(self):
        self.clear_frame()
        
        frame = tk.Frame(self.root)
        frame.pack(pady=20)
        
        label = tk.Label(frame, text="Create a New Account")
        label.pack(pady=10)
        
        pin_label = tk.Label(frame, text="Enter a 4-digit PIN:")
        pin_label.pack(pady=5)
        
        self.new_pin_entry = tk.Entry(frame)
        self.new_pin_entry.pack(pady=5)
        
        balance_label = tk.Label(frame, text="Enter initial balance:")
        balance_label.pack(pady=5)
        
        self.new_balance_entry = tk.Entry(frame)
        self.new_balance_entry.pack(pady=5)
        
        name_label = tk.Label(frame, text="Enter your name:")
        name_label.pack(pady=5)
        
        self.new_name_entry = tk.Entry(frame)
        self.new_name_entry.pack(pady=5)
        
        create_button = tk.Button(frame, text="Create Account", command=self.process_create_account)
        create_button.pack(pady=10)
        
        back_button = tk.Button(frame, text="Back", command=self.create_login_frame)
        back_button.pack(pady=10)
    
    def process_create_account(self):
        pin = self.new_pin_entry.get()
        balance = self.new_balance_entry.get()
        name = self.new_name_entry.get()
        
        if pin.isdigit() and len(pin) == 4 and balance.replace('.', '', 1).isdigit() and name:
            account = {
                "pin": int(pin),
                "balance": float(balance),
                "name": name
            }
            self.accounts.append(account)
            self.save_accounts()
            messagebox.showinfo("Account Created", "Account created successfully!")
            self.create_login_frame()
        else:
            messagebox.showerror("Invalid Input", "Please enter valid account details.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
