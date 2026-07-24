from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database setup (Task 2: Store readings in SQLite)
os.makedirs('data', exist_ok=True)  # Ensure data folder exists
DB_PATH = os.path.join('data', 'water_data.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reading_id TEXT NOT NULL,
            ward TEXT NOT NULL,
            flow_litres REAL,
            valve_state TEXT NOT NULL,
            recorded_at TEXT NOT NULL,
            device_id TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()
print("✅ Database initialized at data/water_data.db")

# Valid values for validation
VALID_WARDS = ['Ward-A', 'Ward-B', 'Ward-C', 'Ward-D', 'Ward-E']
VALID_VALVE = ['OPEN', 'CLOSED']

# 1. POST /api/update - Simulator sends data, Backend validates & stores (Task 2)
@app.route('/api/update', methods=['POST'])
def update_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    # Validate all required fields exist
    required_fields = ['reading_id', 'ward', 'flow_litres', 'valve_state', 'recorded_at', 'device_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Validate ward
    if data['ward'] not in VALID_WARDS:
        return jsonify({"error": "Invalid ward name"}), 400

    # Validate valve state
    if data['valve_state'] not in VALID_VALVE:
        return jsonify({"error": "Invalid valve state"}), 400

    # Validate flow (allow None for missing values)
    flow = data['flow_litres']
    if flow is not None:
        try:
            flow = float(flow)
            if flow < 0:
                return jsonify({"error": "Flow cannot be negative"}), 400
        except (TypeError, ValueError):
            return jsonify({"error": "Flow must be a number"}), 400

    # Save to SQLite database
    conn = get_db()
    conn.execute(
        'INSERT INTO readings (reading_id, ward, flow_litres, valve_state, recorded_at, device_id) VALUES (?, ?, ?, ?, ?, ?)',
        (data['reading_id'], data['ward'], flow, data['valve_state'], data['recorded_at'], data['device_id'])
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Reading saved!"}), 200

# 2. GET /api/data - For Frontend Dashboard (Chart compatibility)
@app.route('/api/data')
def get_latest():
    conn = get_db()
    row = conn.execute('SELECT * FROM readings ORDER BY id DESC LIMIT 1').fetchone()
    conn.close()
    
    if row:
        # Convert to dict and map to frontend fields
        data = dict(row)
        # Frontend expects 'flow', 'pressure', 'level'
        return jsonify({
            'flow': data['flow_litres'] if data['flow_litres'] is not None else 0,
            'pressure': round(random.uniform(2, 8), 2),  # Dummy for now
            'level': round(random.uniform(30, 90), 2),  # Dummy for now
            'ward': data['ward'],
            'valve_state': data['valve_state']
        })
    return jsonify({'flow': 0, 'pressure': 0, 'level': 0, 'ward': 'None'})

# 3. GET /api/readings - For Task 3 (Listing, Search, Filter)
@app.route('/api/readings')
def get_readings():
    ward = request.args.get('ward')
    valve = request.args.get('valve')
    query = 'SELECT * FROM readings WHERE 1=1'
    params = []
    if ward:
        query += ' AND ward = ?'
        params.append(ward)
    if valve:
        query += ' AND valve_state = ?'
        params.append(valve)
    query += ' ORDER BY id DESC'
    
    conn = get_db()
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

if __name__ == '__main__':
    app.run(debug=True, port=5000)