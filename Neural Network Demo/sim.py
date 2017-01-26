from my_math import *

def simulate_drop(mass,  pos_self_current,  speed_current,  drag,  wind,  pos_goal,  step = 0.001):

    time = 0
    force = [0, 0, 0]
    g = -9.806  # in Ottawa (g differs in different locations on earth)
    acceleration = [0, 0, 0]
    pos_self = pos_self_current
    speed = speed_current
    while pos_self[2] > 0:
        time += step

        # in 3 dimensions
        for counter in range(3):
            force[counter] = drag[counter] * (speed[counter] - wind[counter])**2
            if counter == 2:
                force[counter] += g
            acceleration[counter] = force[counter] / mass
            pos_self[counter] += speed[counter] * step + 0.5*acceleration[counter] * step**2
            speed[counter] += acceleration[counter] * step

    # angle from moving direction to the direction to aim in the clockwiseness of unit circle in degrees
    angle = calc_angle_diff_between(speed_current,   vector_add(pos_goal,pos_self_current,"-") )
    return [time, pos_self, angleToDirect(angle), vector_add(pos_goal,pos_self,"-")]
    # output: [
    #
    #            supposed length of time from dropping moment(now) to landing moment if it is dropped at current moment,
    #            [x,y,z](supposed landing position if it is dropped at current moment ),
    #            [direction from current velocity to aim direction, degree]  human readable
    #            [x,y,z] distance from supposed landing position to aim if it is dropped at current moment
    #
    #          ]



