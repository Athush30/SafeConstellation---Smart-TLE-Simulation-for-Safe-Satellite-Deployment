from skyfield.api import load
from skyfield.api import load, EarthSatellite
from datetime import timedelta
import numpy as np

ts = load.timescale()

def check_collision(pos1, pos2, threshold_km):
    distance = np.linalg.norm(pos1 - pos2)
    return distance <= threshold_km, distance

def check_collision_for_candidate(candidate, constellation, steps=144, interval_sec=15, threshold_km=5.0):
    for step in range(steps):
        t = ts.utc(ts.now().utc_datetime() + timedelta(seconds=step * interval_sec))
        pos_new = candidate.at(t).position.km
        for name, sat in constellation.items():
            pos_old = sat.at(t).position.km
            risk, dist = check_collision(np.array(pos_new), np.array(pos_old), threshold_km)
            if risk:
                print(f"⚠️ Collision Risk at step {step + 1} ({t.utc_iso()}):")
                print(f"   {candidate.name} vs {name}: Distance = {dist:.3f} km")
                return True, step, t
    return False, -1, None

def generate_collision_free_tle(tle1, tle2, constellation, delta_deg=0.1, attempts=50):
    line_parts = tle2.split()
    inc_index, raan_index = 2, 3  # Inclination and RAAN
    inc = float(line_parts[inc_index])
    raan = float(line_parts[raan_index])

    for i in range(attempts):
        test_inc = inc + delta_deg * (i + 1)
        line_parts[inc_index] = f"{test_inc:.4f}"
        new_tle2 = " ".join(line_parts)
        test_sat = EarthSatellite(tle1, new_tle2, "NEW-SAT", ts)
        risk, _, _ = check_collision_for_candidate(test_sat, constellation)
        if not risk:
            return tle1, new_tle2
    return None, None
