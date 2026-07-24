\# 🚰 Ward Water Supply Measurement \& Equity Dashboard



\[!\[SIH 2026](https://img.shields.io/badge/SIH-2026-blue)](https://www.sih.gov.in/)

\[!\[Python](https://img.shields.io/badge/Python-3.9+-green)](https://www.python.org/)

\[!\[Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)](https://flask.palletsprojects.com/)

\[!\[SQLite](https://img.shields.io/badge/Database-SQLite-blue)](https://www.sqlite.org/)

\[!\[Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()



\## 📖 Problem Statement



A town supplies water to its wards on a rotating schedule. Residents in some wards complain they receive far less than others, but the corporation cannot verify this because supply is never measured—only valve operation times are noted manually. Without measurement, complaints cannot be verified, and schedules cannot be corrected.



\*\*Objective:\*\* Build a device simulator and dashboard that measures the water actually delivered at each ward supply point and displays ward-wise supply over time, so complaints can be checked against measurement and the schedule adjusted.



\## ✨ Features Implemented



| SIH Task | Feature | Status |

| :---: | :--- | :---: |

| \*\*Task 1\*\* | \*\*Sample Data:\*\* SIH-compliant schema (`reading\_id`, `ward`, `flow\_litres`, `valve\_state`, `recorded\_at`, `device\_id`) with deliberate faulty cases (Outliers, Missing values, Stuck readings). | ✅ |

| \*\*Task 2\*\* | \*\*Register End-to-End:\*\* Server-side validation, derived figure calculation, and SQLite persistence. | ✅ |

| \*\*Task 3\*\* | \*\*Listing, Search \& Filter:\*\* Dynamic table with Ward/Valve filters, instant search, record count, and visual highlighting for faulty data. | ✅ |

| \*\*Task 4\*\* | \*\*Non-blocking Sensor Node:\*\* `threading.Timer` based scheduling, Plausibility checks (>100 L/s rejected), and Moving Average smoothing (last 5 values). | ✅ |

| \*\*Task 5\*\* | \*\*Integration \& Resilience:\*\* Graceful degradation during network loss, auto-reconnection, and local logging. | ✅ |

| \*\*Task 6\*\* | \*\*Documentation:\*\* Comprehensive README, field definitions, and demonstration ready. | ✅ |



\## 🛠️ Technology Stack



\- \*\*Frontend:\*\* HTML5, CSS3, Vanilla JavaScript, Chart.js (Real-time graphing)

\- \*\*Backend:\*\* Python Flask (REST API)

\- \*\*Database:\*\* SQLite (Lightweight, file-based)

\- \*\*Simulator:\*\* Python (`threading` for non-blocking I/O, `requests` for API calls)

\- \*\*DevOps:\*\* `start.bat` (One-click orchestration)



\## 📂 Project Structure



