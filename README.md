📖 Overview

The Aqua Ward Water Supply Measurement & Equity Dashboard is a smart water monitoring system developed for SIH 2026. It measures ward-wise water distribution using a sensor simulator and provides real-time insights through an interactive dashboard. The system helps municipal authorities identify supply inequalities and improve water distribution schedules.

📖 Problem Statement

A town supplies water to its wards on a rotating schedule. Residents in some wards complain they receive far less water than others, but the corporation cannot verify these complaints because supply is never measured—only valve operation times are noted manually.

Without accurate measurements, complaints cannot be validated and schedules cannot be adjusted effectively.

Objective: Build a device simulator and dashboard that measures the water actually delivered at each ward supply point and displays ward-wise supply over time so that complaints can be verified using real data.

✨ Features Implemented
SIH Task	Feature	Status
Task 1	SIH-compliant sample data generation with faulty cases (Outliers, Missing Values and Stuck Readings)	✅
Task 2	Server-side validation and SQLite data persistence	✅
Task 3	Listing, Search and Filter functionality with visual fault highlighting	✅
Task 4	Non-blocking Sensor Node using threading.Timer with Moving Average smoothing	✅
Task 5	Graceful network recovery, auto-reconnection and local logging	✅
Task 6	Comprehensive documentation and demonstration-ready implementation	✅

🛠️ Technology Stack
Component	Technology Used
Frontend	HTML5, CSS3, JavaScript, Chart.js
Backend	Python Flask (REST API)
Database	SQLite
Simulator	Python (threading, requests)
Visualization	Real-time Charts using Chart.js
DevOps	start.bat (One-click execution)
⚙️ Key Functionalities
Real-time Ward-wise Water Monitoring.
Water Flow Measurement Simulation.
Fault Detection (Outliers, Missing Values and Stuck Readings).
Moving Average based Sensor Data Smoothing.
Dynamic Search and Filtering.
SQLite Data Storage.
Network Failure Handling and Auto Recovery.
Interactive Dashboard with Graphical Visualization.
📂 Project Structure

> 🔹 Backend Module – Flask-based REST APIs.

> 🔹 Sensor Simulator – Generates ward-wise water flow readings.

> 🔹 Dashboard Module – Displays real-time analytics.

> 🔹 Database Module – Stores water supply measurements.

> 🔹 Validation Module – Detects faulty sensor readings.

> 🔹 Documentation Module – Provides setup and project details.
Modify the folder structure above if your project contains additional files or folders.

🚀 How It Works
The Sensor Simulator generates ward-wise water flow data.
The Flask REST API receives and validates the readings.
The validated data is stored in SQLite.
The dashboard displays real-time ward-wise measurements.
Faulty readings are automatically detected and highlighted.
Authorities can analyse supply inequalities using visual reports.
📊 Output Dashboard

The dashboard provides:

Ward-wise Water Supply Measurements.
Real-time Graphical Visualization.
Search and Filtering Options.
Fault Detection Alerts.
Water Distribution Analytics.

Add screenshots of your dashboard inside a screenshots/ folder and include them here before submission.

🔮 Future Enhancements
IoT Sensor Integration.
AI-based Water Demand Prediction.
SMS and Email Notifications.
Mobile Application Support.
Cloud-based Deployment.
Advanced Water Consumption Analytics.
👨‍💻 Team Information

Project: Aqua Ward Water Supply Measurement & Equity Dashboard

SIH 2026 Project
BE Computer Science and Engineering

✅ Project Status

Completed and Demonstration Ready for SIH 2026 Submission.
