# 🛰️ Safe Constellation: Smart TLE Simulation for Satellite Deployment

This project simulates a real-time collision-aware satellite deployment system using Python and [Skyfield](https://rhodesmill.org/skyfield/). It validates and adjusts the TLE (Two-Line Element) data of a new satellite before adding it to an existing constellation.

## 🚀 Features

- Load existing constellation from `tle_data.txt`
- Simulate a new satellite's trajectory using TLE
- Detect potential collisions with existing satellites
- Automatically adjust orbit (inclination) to avoid collisions
- Log all events in `events_log.csv`
- Append collision-free TLEs to the constellation

---

## 📁 Folder Structure

```
safe-constellation-smart-tle-simulation/
 └──project
      ├── main.py                # Main simulation logic
      ├── collision_check.py     # Collision detection and TLE adjustment
      ├── logger.py              # Logging events to CSV
      ├── tle_data.txt           # Existing constellation TLEs
      ├── events_log.csv         # Output log file (auto-generated)
      ├── README.md              # Documentation
      └── requirements.txt       # Python dependencies
```

---

## 🧪 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:

```
skyfield
numpy
```

---

## 🧠 How It Works

### 1. Load the existing constellation:

```python
load_constellation("tle_data.txt")
```

### 2. Add a new satellite and check for collision:

```python
add_new_satellite(tle1, tle2, "NEW-SAT")
```

- If a potential collision is detected, the system attempts to adjust the inclination angle (`delta_deg`) iteratively.
- If successful, the adjusted TLE is added to the constellation.

---

## 🗂️ Sample TLE Format in `tle_data.txt`

```
SAT-1
1 25544U 98067A   25200.00000000  .00000200  00000-0  10000-4 0  0002
2 25544  51.6400  124.0000 0001000  0.0000 180.0000 15.00000000
```

---

## 📊 Output

- ✅ Updated constellation in `tle_data.txt`
- 📝 Event log in `events_log.csv`
- 🚨 Console alerts for any detected collision risks

```
Satellite Collision Avoidance Simulation Starting ...
Loaded 3 satellites into constellation.
Checking candidate orbit for collision risks ...
NEW-SAT-NO-COLLIDE added to constellation and saved.
Final Constellation:
- SAT-1
SAT-2
- NEW-SAT
NEW-SAT-NO-COLLIDE
```
---

## 📌 Future Improvements

- GUI or Web Interface for satellite deployment
- ML-based orbit prediction and optimization
- 3D orbital visualization using `plotly` or `matplotlib`

---

## 📜 License

MIT License (add `LICENSE` file for clarity)

---
