import numpy as np
motor_speed_rpm = [
      0,  500, 1000, 1500, 2000, 2500, 3000, 3500,
   4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500,
   8000, 8500, 9000, 9500, 10000
]
motor_torque_Nm = [
    280, 280, 280, 280, 280, 280, 280, 280,
    280, 260, 240, 220, 200, 185, 170, 155,
    140, 120, 100, 70, 40
]

def get_motor_torque(speed_rpm):
    return float(np.interp(speed_rpm, motor_speed_rpm, motor_torque_Nm))

