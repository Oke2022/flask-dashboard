# app.py
from flask import Flask, render_template, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Sample data for dashboard
dashboard_data = {
    'users': 1250,
    'sales': 45780,
    'orders': 892,
    'revenue': 123456.78
}

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/data')
def get_data():
    return jsonify({
        'data': dashboard_data,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
