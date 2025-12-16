# simulation.py
import matplotlib.pyplot as plt
import math

from vehicle_model import acceleration_calculation, gear_ratio, wheel_radius
from drive_cycle import load_drive_cycle, get_vref_interpolated
from driver_controller import driver_command, delta_time
from motor_curve import get_motor_torque
from Battery_model import battery_soc_calculation


# SIM parameters
sim_time = delta_time      # keep them consistent
vehicle_speed_init = 0.0
grade = 0.0                # flat road
SOC_init = 0.8


def speed_calculation():
    time_start = 0.0
    veh_speed = vehicle_speed_init
    SOC = SOC_init
    data_time = []
    data_vehicle_speed = []
    data_vref = []
    data_throttle = []
    data_brake = []
    data_motor_speed = []
    data_motor_torque = []
    data_SOC = []
    data_Terminal_Voltage = []
    data_motor_power = []
    data_battery_power = []
   

 

    # get drive cycle once (UDDS / HWFET / US06)
    cycle_time, cycle_speed = load_drive_cycle("UDDS")
    time_end = cycle_time[-1]    # simulate full cycle

    while time_start < time_end:
        # interpolated reference speed from drive cycle
        v_ref = get_vref_interpolated(time_start, cycle_speed)

        # driver PI controller
        throttle, brake = driver_command(veh_speed, v_ref)

        # vehicle dynamics
        a = acceleration_calculation(veh_speed, grade, throttle, brake)
        veh_speed = veh_speed + a * sim_time
        if veh_speed < 0:
            veh_speed = 0.0

        ## -------------Motor data capturing for simulation output-------------------##
        motor_speed_rpm = veh_speed * gear_ratio * 60 / (2 * math.pi * wheel_radius)
        data_motor_speed.append(motor_speed_rpm)
        motor_torque = get_motor_torque(motor_speed_rpm) * throttle
        data_motor_torque.append(motor_torque)  
        ##--------------------------------------------------------------------------##

        ## -------------Battery SOC Calculation ------------------------------------##

        motor_speed_rps = motor_speed_rpm*2*3.14/60
        motor_power = motor_speed_rps*motor_torque
        SOC,Battery_Current,Terminal_Voltage = battery_soc_calculation(motor_torque,motor_speed_rps,SOC)
        battery_power = Battery_Current*Terminal_Voltage
        data_SOC.append(SOC)
        data_Terminal_Voltage.append(Terminal_Voltage)
        data_motor_power.append(motor_power)
        data_battery_power .append(battery_power)

        ###------------------------------------------------------------------------###

        time_start += sim_time

        # log data
        data_time.append(time_start)
        data_vehicle_speed.append(veh_speed)
        data_vref.append(v_ref)
        data_throttle.append(throttle)
        data_brake.append(brake)
        


    return data_time, data_vehicle_speed, data_vref, data_throttle, data_brake,data_motor_speed,data_motor_torque,data_SOC,data_Terminal_Voltage,data_motor_power,data_battery_power


if __name__ == "__main__":
    time_list, speed_list, vref_list, throttle_list, brake_list,motor_speed_list, motor_torque_list,SOC_list,Terminal_Voltage_list,motor_power_list,battery_power_list = speed_calculation()

    # ===== plots =====
    plt.figure()
    plt.plot(time_list, speed_list, label="Actual speed")
    plt.plot(time_list, vref_list, "--", label="UDDS reference")
    plt.xlabel("Time (s)")
    plt.ylabel("Vehicle Speed (m/s)")
    plt.title("Speed vs Time (Longitudinal Dynamics - Level 2, UDDS)")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.plot(time_list, throttle_list, label="Throttle")
    plt.plot(time_list, brake_list, label="Brake")
    plt.xlabel("Time (s)")
    plt.ylabel("Command (0–1)")
    plt.title("Driver Commands")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.plot(time_list, motor_speed_list, label="Motor speed (RPM)")
    plt.xlabel("Time (s)")
    plt.ylabel("Motor Speed (RPM)")
    plt.title("Motor Speed vs Time")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.plot(time_list, motor_torque_list, label="Motor torque (Nm)")
    plt.xlabel("Time (s)")
    plt.ylabel("Motor Torque (Nm)")
    plt.title("Motor Torque vs Time")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.plot(time_list, SOC_list, label="SOC (%)")
    plt.xlabel("Time (s)")
    plt.ylabel("SOC (%)")
    plt.title("SOC vs Time")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.plot(time_list, Terminal_Voltage_list, label="Terminal Voltage (V)")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.title("Voltage vs Time")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.plot(time_list, motor_power_list, label="Motor Power")
    plt.plot(time_list, battery_power_list, label="Battery Power")
    plt.xlabel("Time (s)")
    plt.ylabel("Power (W)")
    plt.title("Power Comparison")
    plt.grid(True)
    plt.legend()

    plt.show()
