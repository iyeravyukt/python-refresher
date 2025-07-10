import numpy as np


class phsyics:
    import numpy as np
    
    #1---
    def calculate_buoyancy(V, density_fluid):
        return V * density_fluid * 9.81

    #2---
    def will_it_float(V, mass):
        if(V * mass >= 1000):
            return True
        return False
    
    #3---
    def calculate_pressure(depth):
        return depth * 9.81 * 1000

    #4---
    def calculate_acceleration(F, m):
        return F / m
    
    #5---
    def calculate_angular_acceleration(tau, I):
        return tau / I  
    
    #6---
    def calculate_torque(F_magnitude, F_direction, r):
        t = F_magnitude * r * np.sin(F_direction)
        return t
    
    #7---
    def calculate_moment_of_inertia(m, r):
        return m * r * r
    
    #8---
    def calculate_auv_acceleration(F_magnitude, F_angle, m):
        #angle should be from -30 to 30
        Fx = F_magnitude * np.cos(F_angle)
        Fy = F_magnitude * np.sin(F_angle)
        ax = Fx/m
        ay = Fy/m
        return np.sqrt(ax*ax + ay*ay)
    #check
    
    def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia, thruster_distance):
        return F_magnitude * thruster_distance * np.sin(F_angle) / inertia
        #CHECK

    #9---
    def calculate_auv2_acceleration(T, alpha, theta, mass):
        return 0
        




    


