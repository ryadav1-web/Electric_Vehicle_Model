# driver_controller.py

# Driver Controller (PI)
Kp = 0.6
Ki = 0.2
integral_error = 0.0
delta_time = 0.01   # should match sim_time


def driver_command(veh_speed, v_ref):
    
    global integral_error

    error = v_ref - veh_speed

    # PI Controller with Anti windup to remove standstill controller output
    if abs(veh_speed) < 0.05 and abs(v_ref) < 0.05:
        integral_error = 0.0
        controller_output = 0.0
    else:
        integral_error += error * delta_time
        controller_output = Kp * error + Ki * integral_error



    if controller_output >= 0:
        throttle = min(controller_output, 1.0)
        brake = 0.0
    else:
        throttle = 0.0
        brake = min(-controller_output, 1.0)
    
    

    return throttle, brake
