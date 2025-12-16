from motor_curve import get_motor_torque 

def torque_adhesion_limited(mu,mass,g,veh_speed,wheel_radius,gear_ratio):
    ## Torque limited due to adhesion 
    Traction_adhesion_max = mu*mass*g
    speed = veh_speed*gear_ratio*60/(2*3.14*wheel_radius)
    Max_motor_torque = get_motor_torque(speed)
    Motor_torque_limited = Max_motor_torque*gear_ratio/wheel_radius
   

    return min(Traction_adhesion_max,Motor_torque_limited)








