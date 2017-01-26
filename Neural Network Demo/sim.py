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
    landing_diff = vector_add(pos_goal,pos_self,"-")
    result = {"time ": time, "landing pos: ": pos_self, "angle: ":angleToDirect(angle), "landing diff: ":[landing_diff]}
    if abs(landing_diff[0])< 0.03 and abs(landing_diff[1])<0.03:
        result["landing diff: "].insert(0,"would land at aim")
    else:
        result["landing diff: "].insert(0,"would not land at aim")
    return result
    # output: [
    #
    #            "time ": supposed length of time from dropping moment(now) to landing moment if it is dropped at current moment,
    #
    #            "landing pos: ": [x,y,z]
    #            #(supposed landing position if it is dropped at current moment ),
    #
    #            "angle ":[direction from current velocity to aim direction, degree]
    #            # rounded to human readable
    #
    #            "landing diff ": ["if would land at aim", [x,y,z]]
    #            # distance from supposed landing position to aim if it is dropped at current moment
    #
    #          ]



