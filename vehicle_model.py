# vehicle_model.py
import math
from torq_calc import torque_adhesion_limited
# physical constraints
g = 9.81                  # gravitational acceleration (m/s^2)
rho_air = 1.225           # air density at sea level (kg/m^3)
mu = 0.8

# vehicle parameters
mass = 1600.0             # kg (vehicle + driver)
frontal_area = 2.2        # m^2
drag_coefficient = 0.28   # Cd
rolling_resistance_coeff = 0.015  # C_rr
wheel_radius = 0.32       # m
gear_ratio = 9.0          # final drive ratio (EV with single speed)
drivetrain_efficiency = 0.92

# powertrain parameters
max_motor_torque = 280.0  # Nm (at low speeds)
base_speed_rpm = 4000.0   # not used yet
max_power = 120000.0      # W (not used yet)




def acceleration_calculation(veh_speed, grade, throttle, brake):
    

    
    # derived forces
    Max_traction_force = torque_adhesion_limited(mu,mass,g,veh_speed,wheel_radius,gear_ratio)
    #Max_traction_force = max_motor_torque*gear_ratio/wheel_radius
    Max_brake_force = 8000.0  # N (simple assumption)
    
    # Resistive forces
    Force_roll_resistance = rolling_resistance_coeff * mass * g
    Force_drag = 0.5 * rho_air * drag_coefficient * frontal_area * veh_speed * veh_speed
    Force_grade = mass * g * math.sin(grade)

    # Tractive & braking forces
    F_trac = Max_traction_force* throttle
    F_brake = Max_brake_force * brake

    # Net acceleration
    acceleration = (F_trac - (Force_grade + Force_roll_resistance + Force_drag + F_brake)) / mass
    return acceleration 
