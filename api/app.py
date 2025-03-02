# app.py - Main application file for Vercel
from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime, timedelta

# Initialize Flask app with correct static and template folder paths
app = Flask(__name__,
            static_folder='../static',  # Static files in 'static' folder one level up
            template_folder='../templates')  # Templates in 'templates' folder one level up

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_time_left', methods=['POST'])
def get_time_left():
    data = request.json
    target_date = datetime.fromisoformat(data['target_date'].replace('Z', '+00:00'))
    now = datetime.utcnow()
    time_left = target_date - now
    
    if time_left.total_seconds() <= 0:
        return jsonify({
            'days': 0,
            'hours': 0,
            'minutes': 0,
            'seconds': 0,
            'expired': True
        })
    
    # Extract time components
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60
    
    return jsonify({
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'expired': False
    })

# For local development
if __name__ == '__main__':
    app.run(debug=True)