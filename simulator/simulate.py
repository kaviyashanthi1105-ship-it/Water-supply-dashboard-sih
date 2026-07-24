import random
import requests
import uuid
from datetime import datetime
import threading
import time

wards = ['Ward-A', 'Ward-B', 'Ward-C', 'Ward-D', 'Ward-E']
devices = ['FLOW-SENSOR-01', 'FLOW-SENSOR-02', 'FLOW-SENSOR-03']
valve_states = ['OPEN', 'CLOSED']

# For Smoothing (Task 4)
flow_history = []  # Last 5 valid flows
MAX_ALLOWED_FLOW = 100  # Plausibility limit

# For stuck simulation
previous_valid_flow = None

def generate_reading():
    global previous_valid_flow
    
    # 1. Generate raw value (with 10% fault chance - Task 1)
    is_faulty = random.random() < 0.1
    raw_flow = random.randint(10, 50)
    
    if is_faulty:
        fault_type = random.choice(['outlier', 'missing', 'stuck'])
        if fault_type == 'outlier':
            raw_flow = random.randint(500, 1000)
            print(f"⚠️ FAULT: Outlier generated ({raw_flow})")
        elif fault_type == 'missing':
            raw_flow = None
            print(f"⚠️ FAULT: Missing value generated")
        elif fault_type == 'stuck':
            raw_flow = previous_valid_flow
            print(f"⚠️ FAULT: Stuck value ({raw_flow})")
    
    # 2. Plausibility Check (Task 4)
    valid = True
    if raw_flow is not None and (raw_flow < 0 or raw_flow > MAX_ALLOWED_FLOW):
        print(f"❌ REJECTED (Plausibility): {raw_flow} is out of range (> {MAX_ALLOWED_FLOW})")
        valid = False
        raw_flow = None  # Reject it
    
    # 3. Smoothing - Moving Average of last 5 valid readings (Task 4)
    if valid and raw_flow is not None:
        flow_history.append(raw_flow)
        if len(flow_history) > 5:
            flow_history.pop(0)
        smoothed_flow = sum(flow_history) / len(flow_history)
        previous_valid_flow = raw_flow  # Store for stuck fault
        print(f"📊 Smoothing: History={flow_history} → Avg={round(smoothed_flow,2)}")
    else:
        # If invalid, use last known average
        if flow_history:
            smoothed_flow = sum(flow_history) / len(flow_history)
            print(f"ℹ️ Using last smoothed value: {round(smoothed_flow,2)}")
        else:
            smoothed_flow = None
            print(f"ℹ️ No history available, sending None")

    # 4. Prepare SIH format data
    data = {
        'reading_id': str(uuid.uuid4())[:8],
        'ward': random.choice(wards),
        'flow_litres': round(smoothed_flow, 2) if smoothed_flow is not None else None,
        'valve_state': random.choice(valve_states),
        'recorded_at': datetime.now().isoformat(),
        'device_id': random.choice(devices)
    }
    
    # 5. Send to backend
    try:
        response = requests.post('http://localhost:5000/api/update', json=data)
        print(f"✅ Sent (Smoothed): {data} - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending: {e}")
    
    # 6. Schedule next run (NON-BLOCKING - Task 4)
    threading.Timer(5.0, generate_reading).start()
    print("⏳ Next reading scheduled in 5 seconds (Non-blocking)...")

# Start the first reading
print("🚀 Starting NON-BLOCKING Simulator (Task 4: Plausibility + Smoothing)...")
generate_reading()

# Keep the program running (Main thread is free, Timer runs in background)
while True:
    time.sleep(1)