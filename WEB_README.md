# Budget Buddy - Web Application

A beautiful, fully functional web-based personal finance management system built with Flask, HTML, CSS, and JavaScript.

## 🌟 Features

- **Modern UI**: Beautiful gradient design with smooth animations
- **Dual Mode System**: Separate modes for students and professionals
- **Real-time Updates**: Instant feedback and live data updates
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Data Persistence**: All data saved automatically
- **Budget Alerts**: Visual warnings when overspending
- **Category Breakdown**: Visual charts showing spending patterns
- **Transaction Management**: Easy add, view, and delete operations

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Run the Application**
```bash
python app.py
```

3. **Open in Browser**
```
http://localhost:5000
```

The application will start on port 5000 by default.

## 📱 How to Use

### First Time Setup

1. **Select Your Mode**
   - When you first open the app, choose between Student or Professional mode
   - You can change this later by clicking on the mode indicator

2. **Add Income**
   - Go to the "Income" tab
   - Enter your income source and amount
   - Click "Add Income"

3. **Add Expenses**
   - Go to the "Expenses" tab
   - Select a category, add description and amount
   - Click "Add Expense"

4. **View Dashboard**
   - The Dashboard shows your financial summary
   - See total income, expenses, balance, and savings rate
   - View category-wise expense breakdown with visual bars

5. **Manage Transactions**
   - Go to "Transactions" tab to see all your financial activity
   - Delete individual transactions if needed
   - Clear all data with the "Clear All Data" button

## 🎨 Features Breakdown

### Dashboard Tab
- **Summary Cards**: Quick view of income, expenses, balance, and savings rate
- **Budget Alerts**: Automatic warnings when spending exceeds income
- **Category Breakdown**: Visual representation of spending by category

### Income Tab
- Add multiple income sources
- View all income entries
- Delete individual income entries

### Expenses Tab
- Categorized expense tracking
- Add detailed descriptions
- View recent expenses
- Delete individual expenses

### Transactions Tab
- Complete transaction history
- Separate views for income and expenses
- Bulk data clearing option

## 🛠️ Technical Stack

### Backend
- **Flask**: Python web framework
- **JSON**: Data storage format
- **Session Management**: User data isolation

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with animations
- **JavaScript**: Dynamic interactions and API calls
- **Fetch API**: Asynchronous data operations

## 📁 Project Structure

```
budget-buddy-web/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html             # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css          # Styles
│   └── js/
│       └── app.js             # JavaScript logic
└── user_data/                 # User data storage (auto-created)
    └── default_user_data.json # User financial data
```

## 🔒 Data Storage

- All data is stored locally in the `user_data` directory
- Each user session has its own JSON file
- Data persists across browser sessions
- No external database required

## 🎯 API Endpoints

### Mode Management
- `GET /api/mode` - Get current mode
- `POST /api/mode` - Set mode (student/professional)

### Income Management
- `GET /api/income` - Get all income sources
- `POST /api/income` - Add new income
- `DELETE /api/income` - Delete income entry

### Expense Management
- `GET /api/expenses` - Get all expenses
- `POST /api/expenses` - Add new expense
- `DELETE /api/expenses` - Delete expense entry

### Summary & Reports
- `GET /api/summary` - Get financial summary
- `GET /api/categories` - Get categories for current mode

### Data Management
- `POST /api/clear` - Clear all data

## 🎨 Customization

### Change Colors
Edit `static/css/style.css` and modify the CSS variables:
```css
:root {
    --primary-color: #4CAF50;
    --secondary-color: #2196F3;
    --danger-color: #f44336;
    --warning-color: #ff9800;
}
```

### Add New Categories
Edit `app.py` and modify the category lists:
```python
STUDENT_CATEGORIES = [...]
PROFESSIONAL_CATEGORIES = [...]
```

### Change Port
Edit `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use a different port
python app.py
# Then edit app.py to change the port number
```

### Dependencies Not Installing
```bash
# Upgrade pip first
pip install --upgrade pip
# Then install requirements
pip install -r requirements.txt
```

### Data Not Saving
- Check that the `user_data` directory exists
- Ensure you have write permissions in the project directory

## 🚀 Deployment

### Local Network Access
The app runs on `0.0.0.0` by default, making it accessible on your local network:
```
http://YOUR_LOCAL_IP:5000
```

### Production Deployment
For production, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up proper authentication
- Using a real database (PostgreSQL, MySQL)
- Implementing HTTPS
- Changing the secret key

## 📊 Browser Compatibility

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers

## 🎓 Learning Outcomes

This project demonstrates:
- Flask web application development
- RESTful API design
- Frontend-backend integration
- Responsive web design
- JavaScript async/await patterns
- CSS animations and transitions
- Session management
- File-based data persistence

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and enhance this project!

---

**Built with ❤️ for better financial management**
