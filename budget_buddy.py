#!/usr/bin/env python3
"""
Budget Buddy - Personal Finance Management System
A console-based application for tracking income, expenses, and savings
"""

import os
import json
from datetime import datetime

class BudgetBuddy:
    def __init__(self):
        self.mode = None
        self.income_sources = []
        self.expenses = []
        self.data_file = "budget_data.json"
        
        # Mode-specific expense categories
        self.student_categories = [
            "Tuition & Fees",
            "Books & Supplies",
            "Food & Dining",
            "Transportation",
            "Accommodation",
            "Entertainment",
            "Personal Care",
            "Other"
        ]
        
        self.professional_categories = [
            "Housing & Rent",
            "Utilities",
            "Groceries",
            "Transportation",
            "Healthcare",
            "Insurance",
            "Entertainment",
            "Dining Out",
            "Shopping",
            "Savings & Investment",
            "Other"
        ]
        
        self.load_data()
    
    def load_data(self):
        """Load data from file if exists"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.mode = data.get('mode')
                    self.income_sources = data.get('income_sources', [])
                    self.expenses = data.get('expenses', [])
                print("✓ Previous session data loaded successfully!\n")
            except Exception as e:
                print(f"⚠ Error loading data: {e}\n")
    
    def save_data(self):
        """Save data to file"""
        try:
            data = {
                'mode': self.mode,
                'income_sources': self.income_sources,
                'expenses': self.expenses
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            print("✓ Data saved successfully!")
        except Exception as e:
            print(f"⚠ Error saving data: {e}")
    
    def get_positive_float(self, prompt):
        """Validate and get positive float input"""
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("⚠ Please enter a positive value!")
                    continue
                return value
            except ValueError:
                print("⚠ Invalid input! Please enter a valid number.")
    
    def select_mode(self):
        """Select user mode"""
        if self.mode:
            print(f"Current mode: {'Student' if self.mode == 'student' else 'Professional'}")
            change = input("Do you want to change mode? (y/n): ").lower()
            if change != 'y':
                return
        
        print("\n" + "="*50)
        print("SELECT YOUR MODE")
        print("="*50)
        print("1. Student Mode")
        print("2. Professional Mode")
        
        while True:
            choice = input("\nEnter your choice (1-2): ")
            if choice == '1':
                self.mode = 'student'
                print("\n✓ Student mode activated!")
                break
            elif choice == '2':
                self.mode = 'professional'
                print("\n✓ Professional mode activated!")
                break
            else:
                print("⚠ Invalid choice! Please select 1 or 2.")
    
    def add_income(self):
        """Add income source"""
        if not self.mode:
            print("⚠ Please select a mode first!")
            return
        
        print("\n" + "="*50)
        print("ADD INCOME")
        print("="*50)
        
        source_label = "Income Source" if self.mode == "professional" else "Income Source (e.g., Allowance, Part-time job)"
        source = input(f"{source_label}: ").strip()
        
        if not source:
            print("⚠ Source cannot be empty!")
            return
        
        amount = self.get_positive_float("Amount: ₹")
        
        income_entry = {
            'source': source,
            'amount': amount,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.income_sources.append(income_entry)
        print(f"\n✓ Income of ₹{amount:.2f} from '{source}' added successfully!")
        self.save_data()
    
    def add_expense(self):
        """Add expense"""
        if not self.mode:
            print("⚠ Please select a mode first!")
            return
        
        print("\n" + "="*50)
        print("ADD EXPENSE")
        print("="*50)
        
        categories = self.student_categories if self.mode == 'student' else self.professional_categories
        
        print("\nExpense Categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        while True:
            try:
                choice = int(input(f"\nSelect category (1-{len(categories)}): "))
                if 1 <= choice <= len(categories):
                    category = categories[choice - 1]
                    break
                else:
                    print(f"⚠ Please select a number between 1 and {len(categories)}!")
            except ValueError:
                print("⚠ Invalid input! Please enter a number.")
        
        description = input("Description: ").strip()
        if not description:
            description = category
        
        amount = self.get_positive_float("Amount: ₹")
        
        expense_entry = {
            'category': category,
            'description': description,
            'amount': amount,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.expenses.append(expense_entry)
        print(f"\n✓ Expense of ₹{amount:.2f} for '{description}' added successfully!")
        
        # Check budget status
        self.check_budget_alert()
        self.save_data()
    
    def calculate_total_income(self):
        """Calculate total income"""
        return sum(income['amount'] for income in self.income_sources)
    
    def calculate_total_expenses(self):
        """Calculate total expenses"""
        return sum(expense['amount'] for expense in self.expenses)
    
    def calculate_balance(self):
        """Calculate current balance"""
        return self.calculate_total_income() - self.calculate_total_expenses()
    
    def check_budget_alert(self):
        """Check if expenses exceed income"""
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        
        if total_expenses > total_income:
            print("\n" + "!"*50)
            print("⚠ BUDGET ALERT: Your expenses exceed your income!")
            print(f"Overspending: ₹{total_expenses - total_income:.2f}")
            print("!"*50)
        elif total_expenses > total_income * 0.9:
            print("\n⚠ Warning: You've used 90% or more of your income!")
    
    def view_summary(self):
        """Display financial summary"""
        if not self.mode:
            print("⚠ Please select a mode first!")
            return
        
        print("\n" + "="*50)
        print("FINANCIAL SUMMARY")
        print("="*50)
        
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        balance = self.calculate_balance()
        
        # Income Summary
        print(f"\n{'INCOME SOURCES':-^50}")
        if self.income_sources:
            for income in self.income_sources:
                print(f"  {income['source']:<30} ₹{income['amount']:>10.2f}")
            print(f"  {'Total Income:':<30} ₹{total_income:>10.2f}")
        else:
            print("  No income recorded yet.")
        
        # Expense Summary
        print(f"\n{'EXPENSES':-^50}")
        if self.expenses:
            # Category-wise breakdown
            categories = self.student_categories if self.mode == 'student' else self.professional_categories
            category_totals = {cat: 0 for cat in categories}
            
            for expense in self.expenses:
                category_totals[expense['category']] += expense['amount']
            
            print("\nCategory-wise Breakdown:")
            for category, amount in category_totals.items():
                if amount > 0:
                    percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
                    print(f"  {category:<30} ₹{amount:>10.2f} ({percentage:>5.1f}%)")
            
            print(f"\n  {'Total Expenses:':<30} ₹{total_expenses:>10.2f}")
        else:
            print("  No expenses recorded yet.")
        
        # Balance and Savings
        print(f"\n{'BALANCE & SAVINGS':-^50}")
        print(f"  {'Current Balance:':<30} ₹{balance:>10.2f}")
        
        if balance > 0:
            savings_rate = (balance / total_income * 100) if total_income > 0 else 0
            print(f"  {'Savings Rate:':<30} {savings_rate:>10.1f}%")
            print(f"\n  ✓ Great job! You're saving money!")
        elif balance < 0:
            print(f"\n  ⚠ You're overspending by ₹{abs(balance):.2f}!")
        else:
            print(f"\n  ⚠ You've spent all your income!")
        
        print("="*50)
    
    def view_transactions(self):
        """View all transactions"""
        if not self.mode:
            print("⚠ Please select a mode first!")
            return
        
        print("\n" + "="*50)
        print("TRANSACTION HISTORY")
        print("="*50)
        
        if self.income_sources:
            print(f"\n{'INCOME TRANSACTIONS':-^50}")
            for i, income in enumerate(self.income_sources, 1):
                print(f"\n{i}. {income['source']}")
                print(f"   Amount: ₹{income['amount']:.2f}")
                print(f"   Date: {income['date']}")
        
        if self.expenses:
            print(f"\n{'EXPENSE TRANSACTIONS':-^50}")
            for i, expense in enumerate(self.expenses, 1):
                print(f"\n{i}. {expense['description']}")
                print(f"   Category: {expense['category']}")
                print(f"   Amount: ₹{expense['amount']:.2f}")
                print(f"   Date: {expense['date']}")
        
        if not self.income_sources and not self.expenses:
            print("\nNo transactions recorded yet.")
        
        print("="*50)
    
    def clear_data(self):
        """Clear all data"""
        confirm = input("\n⚠ Are you sure you want to clear all data? (yes/no): ").lower()
        if confirm == 'yes':
            self.income_sources = []
            self.expenses = []
            self.save_data()
            print("✓ All data cleared successfully!")
        else:
            print("Operation cancelled.")
    
    def display_menu(self):
        """Display main menu"""
        mode_text = f" ({self.mode.upper()} MODE)" if self.mode else ""
        
        print("\n" + "="*50)
        print(f"BUDGET BUDDY{mode_text}")
        print("="*50)
        print("1. Select/Change Mode")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. View Financial Summary")
        print("5. View Transaction History")
        print("6. Clear All Data")
        print("7. Exit")
        print("="*50)
    
    def run(self):
        """Main application loop"""
        print("\n" + "="*50)
        print("WELCOME TO BUDGET BUDDY")
        print("Your Personal Finance Management System")
        print("="*50)
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-7): ")
            
            if choice == '1':
                self.select_mode()
            elif choice == '2':
                self.add_income()
            elif choice == '3':
                self.add_expense()
            elif choice == '4':
                self.view_summary()
            elif choice == '5':
                self.view_transactions()
            elif choice == '6':
                self.clear_data()
            elif choice == '7':
                self.save_data()
                print("\n" + "="*50)
                print("Thank you for using Budget Buddy!")
                print("Stay financially smart! 💰")
                print("="*50 + "\n")
                break
            else:
                print("⚠ Invalid choice! Please select 1-7.")


if __name__ == "__main__":
    app = BudgetBuddy()
    app.run()
