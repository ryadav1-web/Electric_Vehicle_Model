import numpy as np
# Battery pack configuration
battery_nominal_voltage = 360.0      # V (typical 96s–108s EV pack)
battery_capacity_Ah = 75.0            # Ah
battery_capacity_kWh = 27.0           # kWh (360 V * 75 Ah ≈ 27 kWh)
#battery_max_power = 120000           # W (matches motor max power)
battery_max_current = 350.0           # A (continuous)


# State of Charge (SOC)
soc_init = 0.8          # 80% initial SOC
soc_min = 0.1           # minimum usable SOC
soc_max = 0.9           # maximum usable SOC
# Battery internal resistance (lumped)
battery_internal_resistance = 0.08    # ohms (pack-level)
TPIM_efficieny = 0.94 # Traction power inverter module efficiency


# OCV vs SOC lookup table
soc_table = np.array([0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ocv_table = np.array([300, 320, 335, 350, 360, 370, 380, 390, 400, 410, 418, 420])

def battery_ocv(soc):
    soc = np.clip(soc, 0.0, 1.0)
    return float(np.interp(soc, soc_table, ocv_table))


def battery_soc_calculation(Motor_torque,Motor_Speed,SOC):
    ## Motor Power calculation
    Motor_power = Motor_torque*Motor_Speed
    # Calculating Battery Power from Motor Power
    Battery_Power =  Motor_power/TPIM_efficieny
    OCV = battery_ocv(SOC)
    #Initial current depends on OCV
    Battery_Current = Battery_Power/OCV

    Terminal_Voltage = OCV - Battery_Current * battery_internal_resistance

    Battery_Current = Battery_Power/Terminal_Voltage
    if Battery_Current > battery_max_current:   # checking max battery current
        Battery_Current = battery_max_current
    
    SOC = SOC - Battery_Current*0.01/(battery_capacity_Ah*3600)
    return SOC,Battery_Current,Terminal_Voltage






