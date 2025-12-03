# Budget Buddy - Quick Start Guide

## Installation & First Run

### Step 1: Verify Python Installation
```bash
python --version
# or
python3 --version
```
You need Python 3.6 or higher.

### Step 2: Run Budget Buddy
```bash
python budget_buddy.py
# or
python3 budget_buddy.py
```

## First Time Setup

### 1. Select Your Mode
When you first launch Budget Buddy, select your mode:
- Press `1` for Student Mode
- Press `2` for Professional Mode

You can change this later from the main menu.

### 2. Add Your Income
- Select option `2` from the main menu
- Enter your income source (e.g., "Monthly Salary", "Allowance")
- Enter the amount (must be positive)
- Repeat for all income sources

### 3. Add Your Expenses
- Select option `3` from the main menu
- Choose a category from the list
- Enter a description
- Enter the amount
- Repeat for all expenses

### 4. View Your Summary
- Select option `4` to see:
  - Total income
  - Total expenses by category
  - Current balance
  - Savings rate

## Example Session

```
WELCOME TO BUDGET BUDDY
Your Personal Finance Management System
==================================================

BUDGET BUDDY
==================================================
1. Select/Change Mode
2. Add Income
3. Add Expense
4. View Financial Summary
5. View Transaction History
6. Clear All Data
7. Exit
==================================================

Enter your choice (1-7): 1

==================================================
SELECT YOUR MODE
==================================================
1. Student Mode
2. Professional Mode

Enter your choice (1-2): 2

✓ Professional mode activated!

Enter your choice (1-7): 2

==================================================
ADD INCOME
==================================================
Income Source: Monthly Salary
Amount: $4500

✓ Income of $4500.00 from 'Monthly Salary' added successfully!

Enter your choice (1-7): 3

==================================================
ADD EXPENSE
==================================================

Expense Categories:
1. Housing & Rent
2. Utilities
3. Groceries
4. Transportation
5. Healthcare
6. Insurance
7. Entertainment
8. Dining Out
9. Shopping
10. Savings & Investment
11. Other

Select category (1-11): 1
Description: Monthly rent
Amount: $1500

✓ Expense of $1500.00 for 'Monthly rent' added successfully!

Enter your choice (1-7): 4

==================================================
FINANCIAL SUMMARY
==================================================

------------------INCOME SOURCES------------------
  Monthly Salary                  $   4500.00
  Total Income:                   $   4500.00

----------------------EXPENSES---------------------

Category-wise Breakdown:
  Housing & Rent                  $   1500.00 ( 100.0%)

  Total Expenses:                 $   1500.00

--------------BALANCE & SAVINGS-------------------
  Current Balance:                $   3000.00
  Savings Rate:                        66.7%

  ✓ Great job! You're saving money!
==================================================
```

## Testing with Sample Data

Want to test with pre-populated data? Use the test scenarios:

```bash
python test_scenarios.py
```

Choose from:
1. Student test data (balanced budget)
2. Professional test data (with savings)
3. Overspending scenario (triggers alerts)

Then run Budget Buddy to see the data in action.

## Tips for Best Results

### For Students:
- Add your allowance or scholarship at the start of each month
- Track part-time job income separately
- Monitor entertainment and dining expenses closely
- Set aside money for textbooks before the semester

### For Professionals:
- Record your salary on payday
- Include all income sources (freelance, bonuses, etc.)
- Prioritize savings as an "expense" category
- Review your summary weekly to stay on track

## Understanding Alerts

### Budget Alert (Critical)
```
⚠ BUDGET ALERT: Your expenses exceed your income!
Overspending: $150.00
```
**Action**: Review your expenses and reduce spending immediately.

### Warning Alert
```
⚠ Warning: You've used 90% or more of your income!
```
**Action**: Be cautious with remaining spending for the period.

## Common Tasks

### Switching Modes
1. Select option `1` from main menu
2. Confirm you want to change mode
3. Select new mode

### Viewing Transaction History
- Select option `5` to see all income and expense entries with dates

### Starting Fresh
1. Select option `6` from main menu
2. Type `yes` to confirm
3. All data will be cleared

### Exiting Safely
- Always use option `7` to exit
- This ensures your data is saved properly

## Data File Location

Your financial data is saved in `budget_data.json` in the same folder as the application.

**Important**: 
- Don't delete this file unless you want to lose your data
- You can back it up by copying it to another location
- The file is human-readable JSON format

## Troubleshooting

### "Invalid input" errors
- Make sure you're entering numbers for amounts
- Don't use currency symbols ($) when entering amounts
- Use positive numbers only

### Data not saving
- Check you have write permissions in the folder
- Make sure you exit using option 7 (not Ctrl+C)

### Previous data not loading
- Ensure `budget_data.json` is in the same folder
- Check the file isn't corrupted (should be valid JSON)

## Next Steps

1. Use Budget Buddy daily to track all transactions
2. Review your summary weekly
3. Adjust spending based on insights
4. Set savings goals and track progress
5. Build better financial habits over time

---

**Ready to take control of your finances? Start tracking now! 💰**
