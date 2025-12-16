# drive_cycle.py

MPH_TO_MPS = 0.44704


# ===============================
#  DRIVE CYCLE DATABASE
# ===============================
# All cycles stored here in mph
# (shortened representative versions)
# ===============================

DRIVE_CYCLES_MPH = {
    "UDDS": [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        6, 10, 15, 20, 23, 25, 26, 27, 28, 28,
        29, 30, 30, 31, 31, 31, 31, 30, 29, 29,
        28, 28, 29, 30, 30, 31, 32, 33, 34, 35,
        35, 35, 35, 34, 33, 32, 30, 28, 26, 25,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        15, 20, 25, 30, 35, 36, 36, 37, 38, 38,
        39, 40, 40, 41, 41, 41, 40, 40, 39, 38,
        37, 36, 34, 32, 30, 28, 26, 24, 22, 20,
        18, 16, 14, 12, 10, 8, 6, 4, 2, 0,
    ],

    "HWFET": (
        [0] * 20 +
        [0 + (60.0 - 0.0) * (i / 60.0) for i in range(60)] +
        sum([[55, 56, 57, 58, 59, 60, 59, 58, 57, 56]] * 12, []) +
        [60.0 - (60.0 - 45.0) * (i / 30.0) for i in range(30)] +
        [45.0] * 30 +
        [45.0 * (1.0 - i / 40.0) for i in range(40)]
    ),

    "US06": (
        [0] * 10 +
        [0 + (50.0 - 0.0) * (i / 20.0) for i in range(20)] +
        [50.0] * 20 +
        [50.0 + (70.0 - 50.0) * (i / 20.0) for i in range(20)] +
        [70.0] * 20 +
        [70.0 - (70.0 - 20.0) * (i / 20.0) for i in range(20)] +
        [20.0] * 20 +
        [20.0 + (80.0 - 20.0) * (i / 20.0) for i in range(20)] +
        [80.0] * 20 +
        sum([[60, 70, 80, 70, 60, 70, 80, 70]] * 3, []) +
        [60.0 * (1.0 - i / 20.0) for i in range(20)]
    )
}


# ===============================
#  GENERAL LOAD FUNCTION
# ===============================

def load_drive_cycle(cycle_name):
    """
    Loads any drive cycle by name.
    Returns:
       time  -> list of time stamps [s]
       speed -> list of speeds [m/s]
    """
    cycle_name = cycle_name.upper()

    if cycle_name not in DRIVE_CYCLES_MPH:
        raise ValueError(f"Unknown drive cycle '{cycle_name}'. Available: {list(DRIVE_CYCLES_MPH.keys())}")

    mph_list = DRIVE_CYCLES_MPH[cycle_name]

    # convert to m/s
    speed_mps = [v * MPH_TO_MPS for v in mph_list]

    # time vector in 1 sec increments
    time = list(range(len(speed_mps)))

    return time, speed_mps


# ===============================
#  INTERPOLATION (COMMON)
# ===============================
def get_vref_interpolated(t, speed_list):
    """
    Linear interpolation of a discrete speed profile.
    """
    t_int = int(t)
    t_frac = t - t_int

    if t_int >= len(speed_list) - 1:
        return speed_list[-1]

    v1 = speed_list[t_int]
    v2 = speed_list[t_int + 1]

    return v1 + t_frac * (v2 - v1)
