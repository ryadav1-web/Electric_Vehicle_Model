# 🚗 Electric Vehicle Longitudinal Simulation (Python)

## Overview
This project is a **Python-based Electric Vehicle (EV) longitudinal simulation framework** designed to model vehicle dynamics, driver behavior, electric powertrain response, and battery energy consumption over standard drive cycles.

The model is intentionally **modular and readable**, making it suitable for:
- Control algorithm development
- Energy consumption analysis
- Rapid prototyping of EV supervisory and vehicle-level logic
- Educational and research purposes

The simulation follows a **Level 1 / Level 2 vehicle modeling philosophy**, commonly used in early-stage automotive control development.

---

## 🎯 Objectives
The primary objectives of this project are:

- Simulate **longitudinal vehicle dynamics** of an electric vehicle
- Track **vehicle speed vs. drive cycle reference**
- Model **driver behavior** using a PI controller
- Compute **motor speed, torque, and power**
- Estimate **battery SOC, current, and terminal voltage**
- Evaluate **energy consumption (kWh/100 miles)**
- Provide a clean foundation to **build higher-level vehicle algorithms**

---

## 🧩 Project Architecture
The model is organized into **independent functional modules**, closely resembling real automotive software architecture.

```
Electric_Vehicle_Simulation/
│
├── simulation.py          # Main simulation loop
├── vehicle_model.py       # Vehicle longitudinal dynamics
├── driver_controller.py   # Driver PI controller
├── drive_cycle.py         # Drive cycle loader & interpolation
├── motor_curve.py         # Motor torque-speed characteristic
├── Battery_model.py       # Battery SOC & electrical model
├── torq_calc.py           # Adhesion-limited torque calculation
├── *.xlsx                 # Drive cycle files (UDDS, HWFET, US06, etc.)
```

---

## 📁 File-by-File Description

### simulation.py
**Main entry point of the simulation**

Responsibilities:
- Loads the selected drive cycle
- Executes the time-based simulation loop
- Calls driver, vehicle, motor, and battery models
- Logs signals for post-processing
- Computes:
  - Total energy consumption
  - Distance traveled
  - kWh / 100 miles
- Generates plots for vehicle, motor, and battery behavior

---

### vehicle_model.py
**Longitudinal vehicle dynamics model**

Includes:
- Aerodynamic drag
- Rolling resistance
- Grade resistance
- Adhesion-limited traction force
- Brake force model

Outputs:
- Vehicle longitudinal acceleration

---

### driver_controller.py
**Driver PI controller**

Responsibilities:
- Tracks drive cycle speed reference
- Generates throttle and brake commands
- Anti-windup and standstill protection logic

---

### drive_cycle.py
**Drive cycle handling module**

Capabilities:
- Loads standard drive cycles (UDDS, HWFET, US06, ECE)
- Converts speed from MPH to m/s
- Time-based linear interpolation

---

### motor_curve.py
**Electric motor torque-speed characteristic**

Contains:
- Motor speed vs torque lookup
- Linear interpolation

---

### Battery_model.py
**Battery electrical & SOC model**

Features:
- OCV vs SOC lookup
- Internal resistance model
- Current and terminal voltage calculation
- SOC update

---

### torq_calc.py
**Traction and adhesion limits**

Computes:
- Road friction-limited traction
- Motor torque-limited wheel force

---

## ▶️ How to Run the Simulation

### 1. Install Dependencies
```
pip install numpy matplotlib openpyxl
```

### 2. Ensure Drive Cycle Files Are Present
Ensure .xlsx drive cycle files are in the same directory as drive_cycle.py.

### 3. Run
```
python simulation.py
```

---

## 🧠 Using This Model for Algorithm Development

You can build on this framework to implement:
- SOC-based supervisory control
- Regenerative braking strategies
- Adaptive cruise control
- MPC or AI-based drivers
- Energy optimization algorithms

The modular structure mirrors **industry-standard MBD workflows**.

---

## 🚀 Future Extensions
- Thermal modeling
- Efficiency map integration
- Hybrid powertrain support

---

## 👤 Author
Developed by an Rajeshwar Yadav, Automotive Controls Engineer focusing on Model-Based Development, EV powertrain systems, and Python-based simulation.
Email ID : ryadav1@mtu.edu
LinkedIn: www.linkedin.com/in/rajeshwar-yadav-53710143
