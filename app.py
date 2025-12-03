#!/usr/bin/env python3
"""
Budget Buddy Web Application
Flask-based personal finance management system
"""

from flask import Flask, render_template, request, jsonify, session
import json
import os
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'budget_buddy_secret_key_2024'  # Change in production

DATA_DIR = 'user_data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Mode-specific expense categories
STUDENT_CATEGORIES = [
    "Tuition & Fees", "Books & Supplies", "Food & Dining",
    "Transportation", "Accommodation", "Entertainment",
    "Personal Care", "Other"
]

PROFESSIONAL_CATEGORIES = [
    "Housing & Rent", "Utilities", "Groceries", "Transportation",
    "Healthcare", "Insurance", "Entertainment", "Dining Out",
    "Shopping", "Savings & Investment", "Other"
]

def get_user_file():
    """Get user data file path"""
    user_id = session.get('user_id', 'default_user')
    return os.path.join(DATA_DIR, f'{user_id}_data.json')

def load_user_data():
    """Load user data from file"""
    file_path = get_user_file()
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except:
            pass
    return {
        'mode': None,
        'income_sources': [],
        'expenses': []
    }

def save_user_data(data):
    """Save user data to file"""
    file_path = get_user_file()
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def calculate_totals(data):
    """Calculate financial totals"""
    total_income = sum(item['amount'] for item in data['income_sources'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    balance = total_income - total_expenses
    
    return {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance,
        'savings_rate': (balance / total_income * 100) if total_income > 0 else 0
    }

def get_category_breakdown(data):
    """Get expense breakdown by category"""
    categories = STUDENT_CATEGORIES if data['mode'] == 'student' else PROFESSIONAL_CATEGORIES
    breakdown = {cat: 0 for cat in categories}
    
    for expense in data['expenses']:
        if expense['category'] in breakdown:
            breakdown[expense['category']] += expense['amount']
    
    total_expenses = sum(breakdown.values())
    
    result = []
    for category, amount in breakdown.items():
        if amount > 0:
            percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
            result.append({
                'category': category,
                'amount': amount,
                'percentage': percentage
            })
    
    return sorted(result, key=lambda x: x['amount'], reverse=True)

@app.route('/')
def index():
    """Home page"""
    if 'user_id' not in session:
        session['user_id'] = 'default_user'
    
    data = load_user_data()
    return render_template('index.html', mode=data['mode'])

@app.route('/api/mode', methods=['GET', 'POST'])
def mode():
    """Get or set user mode"""
    data = load_user_data()
    
    if request.method == 'POST':
        new_mode = request.json.get('mode')
        if new_mode in ['student', 'professional']:
            data['mode'] = new_mode
            save_user_data(data)
            return jsonify({'success': True, 'mode': new_mode})
        return jsonify({'success': False, 'error': 'Invalid mode'}), 400
    
    return jsonify({'mode': data['mode']})

@app.route('/api/categories')
def categories():
    """Get categories for current mode"""
    data = load_user_data()
    if data['mode'] == 'student':
        return jsonify({'categories': STUDENT_CATEGORIES})
    elif data['mode'] == 'professional':
        return jsonify({'categories': PROFESSIONAL_CATEGORIES})
    return jsonify({'categories': []}), 400

@app.route('/api/income', methods=['GET', 'POST', 'DELETE'])
def income():
    """Manage income sources"""
    data = load_user_data()
    
    if request.method == 'POST':
        income_data = request.json
        source = income_data.get('source', '').strip()
        amount = income_data.get('amount')
        
        if not source or not amount or amount <= 0:
            return jsonify({'success': False, 'error': 'Invalid input'}), 400
        
        entry = {
            'source': source,
            'amount': float(amount),
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        data['income_sources'].append(entry)
        save_user_data(data)
        
        return jsonify({'success': True, 'entry': entry})
    
    elif request.method == 'DELETE':
        index = request.json.get('index')
        if 0 <= index < len(data['income_sources']):
            deleted = data['income_sources'].pop(index)
            save_user_data(data)
            return jsonify({'success': True, 'deleted': deleted})
        return jsonify({'success': False, 'error': 'Invalid index'}), 400
    
    return jsonify({'income_sources': data['income_sources']})

@app.route('/api/expenses', methods=['GET', 'POST', 'DELETE'])
def expenses():
    """Manage expenses"""
    data = load_user_data()
    
    if request.method == 'POST':
        expense_data = request.json
        category = expense_data.get('category', '').strip()
        description = expense_data.get('description', '').strip()
        amount = expense_data.get('amount')
        
        if not category or not amount or amount <= 0:
            return jsonify({'success': False, 'error': 'Invalid input'}), 400
        
        entry = {
            'category': category,
            'description': description or category,
            'amount': float(amount),
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        data['expenses'].append(entry)
        save_user_data(data)
        
        return jsonify({'success': True, 'entry': entry})
    
    elif request.method == 'DELETE':
        index = request.json.get('index')
        if 0 <= index < len(data['expenses']):
            deleted = data['expenses'].pop(index)
            save_user_data(data)
            return jsonify({'success': True, 'deleted': deleted})
        return jsonify({'success': False, 'error': 'Invalid index'}), 400
    
    return jsonify({'expenses': data['expenses']})

@app.route('/api/summary')
def summary():
    """Get financial summary"""
    data = load_user_data()
    
    if not data['mode']:
        return jsonify({'error': 'Please select a mode first'}), 400
    
    totals = calculate_totals(data)
    breakdown = get_category_breakdown(data)
    
    return jsonify({
        'totals': totals,
        'breakdown': breakdown,
        'income_sources': data['income_sources'],
        'expenses': data['expenses']
    })

@app.route('/api/clear', methods=['POST'])
def clear_data():
    """Clear all data"""
    data = {
        'mode': load_user_data()['mode'],
        'income_sources': [],
        'expenses': []
    }
    save_user_data(data)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
