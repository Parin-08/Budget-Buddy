#!/bin/bash

echo "======================================"
echo "Budget Buddy Web Application"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

echo "🚀 Starting Budget Buddy Web Server..."
echo ""
echo "📍 Access the application at:"
echo "   http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "======================================"
echo ""

python3 app.py
