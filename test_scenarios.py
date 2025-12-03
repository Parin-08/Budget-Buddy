#!/usr/bin/env python3
"""
Test Scenarios for Budget Buddy
Demonstrates various use cases and edge cases
"""

import json
import os

def create_test_data_student():
    """Create test data for student mode"""
    test_data = {
        'mode': 'student',
        'income_sources': [
            {
                'source': 'Monthly Allowance',
                'amount': 500.0,
                'date': '2024-01-01 10:00:00'
            },
            {
                'source': 'Part-time Job',
                'amount': 800.0,
                'date': '2024-01-05 14:30:00'
            }
        ],
        'expenses': [
            {
                'category': 'Books & Supplies',
                'description': 'Textbooks for semester',
                'amount': 250.0,
                'date': '2024-01-02 11:00:00'
            },
            {
                'category': 'Food & Dining',
                'description': 'Groceries',
                'amount': 150.0,
                'date': '2024-01-03 16:00:00'
            },
            {
                'category': 'Transportation',
                'description': 'Bus pass',
                'amount': 80.0,
                'date': '2024-01-04 09:00:00'
            },
            {
                'category': 'Entertainment',
                'description': 'Movie tickets',
                'amount': 30.0,
                'date': '2024-01-06 20:00:00'
            }
        ]
    }
    
    with open('budget_data.json', 'w') as f:
        json.dump(test_data, f, indent=2)
    
    print("✓ Student test data created!")
    print(f"  Total Income: ₹{sum(i['amount'] for i in test_data['income_sources']):.2f}")
    print(f"  Total Expenses: ₹{sum(e['amount'] for e in test_data['expenses']):.2f}")
    print(f"  Balance: ₹{sum(i['amount'] for i in test_data['income_sources']) - sum(e['amount'] for e in test_data['expenses']):.2f}")

def create_test_data_professional():
    """Create test data for professional mode"""
    test_data = {
        'mode': 'professional',
        'income_sources': [
            {
                'source': 'Monthly Salary',
                'amount': 4500.0,
                'date': '2024-01-01 00:00:00'
            },
            {
                'source': 'Freelance Project',
                'amount': 800.0,
                'date': '2024-01-15 10:00:00'
            }
        ],
        'expenses': [
            {
                'category': 'Housing & Rent',
                'description': 'Monthly rent',
                'amount': 1500.0,
                'date': '2024-01-01 12:00:00'
            },
            {
                'category': 'Utilities',
                'description': 'Electricity and water',
                'amount': 150.0,
                'date': '2024-01-05 14:00:00'
            },
            {
                'category': 'Groceries',
                'description': 'Weekly groceries',
                'amount': 400.0,
                'date': '2024-01-07 10:00:00'
            },
            {
                'category': 'Transportation',
                'description': 'Gas and parking',
                'amount': 200.0,
                'date': '2024-01-10 08:00:00'
            },
            {
                'category': 'Healthcare',
                'description': 'Doctor visit',
                'amount': 100.0,
                'date': '2024-01-12 15:00:00'
            },
            {
                'category': 'Savings & Investment',
                'description': 'Monthly savings',
                'amount': 1000.0,
                'date': '2024-01-01 23:00:00'
            }
        ]
    }
    
    with open('budget_data.json', 'w') as f:
        json.dump(test_data, f, indent=2)
    
    print("✓ Professional test data created!")
    print(f"  Total Income: ₹{sum(i['amount'] for i in test_data['income_sources']):.2f}")
    print(f"  Total Expenses: ₹{sum(e['amount'] for e in test_data['expenses']):.2f}")
    print(f"  Balance: ₹{sum(i['amount'] for i in test_data['income_sources']) - sum(e['amount'] for e in test_data['expenses']):.2f}")

def create_overspending_scenario():
    """Create test data demonstrating overspending alert"""
    test_data = {
        'mode': 'student',
        'income_sources': [
            {
                'source': 'Monthly Allowance',
                'amount': 500.0,
                'date': '2024-01-01 10:00:00'
            }
        ],
        'expenses': [
            {
                'category': 'Entertainment',
                'description': 'Concert tickets',
                'amount': 300.0,
                'date': '2024-01-02 11:00:00'
            },
            {
                'category': 'Shopping',
                'description': 'New clothes',
                'amount': 250.0,
                'date': '2024-01-03 16:00:00'
            }
        ]
    }
    
    with open('budget_data.json', 'w') as f:
        json.dump(test_data, f, indent=2)
    
    print("✓ Overspending scenario created!")
    print(f"  Total Income: ₹{sum(i['amount'] for i in test_data['income_sources']):.2f}")
    print(f"  Total Expenses: ₹{sum(e['amount'] for e in test_data['expenses']):.2f}")
    print(f"  ⚠ Overspending: ₹{sum(e['amount'] for e in test_data['expenses']) - sum(i['amount'] for i in test_data['income_sources']):.2f}")

def clear_test_data():
    """Remove test data file"""
    if os.path.exists('budget_data.json'):
        os.remove('budget_data.json')
        print("✓ Test data cleared!")
    else:
        print("No test data file found.")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("BUDGET BUDDY - TEST SCENARIOS")
    print("="*50)
    print("\n1. Create Student Test Data")
    print("2. Create Professional Test Data")
    print("3. Create Overspending Scenario")
    print("4. Clear Test Data")
    print("5. Exit")
    
    choice = input("\nSelect scenario (1-5): ")
    
    if choice == '1':
        create_test_data_student()
    elif choice == '2':
        create_test_data_professional()
    elif choice == '3':
        create_overspending_scenario()
    elif choice == '4':
        clear_test_data()
    elif choice == '5':
        print("Exiting...")
    else:
        print("Invalid choice!")
    
    print("\nRun 'python budget_buddy.py' to test with this data.\n")
