from skyfield.api import load, EarthSatellite
from collision_check import check_collision_for_candidate, generate_collision_free_tle
from logger import log_event
import os

ts = load.timescale()
satellites = {}

# Load existing constellation from TLE data file
def load_constellation(tle_file):
    with open(tle_file, 'r') as f:
        lines = f.readlines()

    for i in range(0, len(lines), 3):
        if i + 2 >= len(lines):
            print(f"Incomplete TLE at line {i}, skipping.")
            continue
        name = lines[i].strip()
        tle1 = lines[i + 1].strip()
        tle2 = lines[i + 2].strip()
        satellite = EarthSatellite(tle1, tle2, name, ts)
        satellites[name] = satellite

    print(f"🛰️ Loaded {len(satellites)} satellites into constellation.")

# Add new satellite with collision check and adjustment if needed
def add_new_satellite(tle1, tle2, name):
    print("\n🔍 Checking candidate orbit for collision risks...")
    new_sat = EarthSatellite(tle1, tle2, name, ts)
    risk, step, t = check_collision_for_candidate(new_sat, satellites)

    if risk:
        print("❌ Candidate orbit risks collision. Attempting to adjust orbit...\n")
        tle1_adj, tle2_adj = generate_collision_free_tle(tle1, tle2, satellites)
        if tle1_adj is None:
            print("🚫 Could not find collision-free orbit after multiple attempts.")
            return
        new_sat = EarthSatellite(tle1_adj, tle2_adj, name, ts)
        print("✅ Successfully adjusted orbit to avoid collisions.")
        log_event(name, t.utc_iso() if t is not None else "N/A", "Adjusted orbit to avoid collision", tle1, tle2)

    else:
        log_event(name, "N/A", "No collision detected. Added successfully.")

    satellites[name] = new_sat

    # Append new satellite to TLE file
    with open("tle_data.txt", "a") as f:
        f.write(f"{name}\n{tle1}\n{tle2}\n")
    print(f"✅ {name} added to constellation and saved.")

# ---------- Main Execution ----------
if __name__ == "__main__":
    print("🚀 Satellite Collision Avoidance Simulation Starting...\n")

    load_constellation("tle_data.txt")

    # New satellite TLE that may collide
    new_name = "NEW-SAT-NO-COLLIDE"
    new_tle1 = "1 99998U 25001D   25200.00000000  .00000100  00000-0  10000-4 0  0004"
    new_tle2 = "2 99998  54.0000  124.0000 0001000  0.0000 180.0000 15.00000000"

    add_new_satellite(new_tle1, new_tle2, new_name)

    print("\n📦 Final Constellation:")
    for sat_name in satellites:
        print(f"  - {sat_name}")
