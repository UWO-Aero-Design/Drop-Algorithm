from cmath import *


def calc_angle_diff_between(a,b):
    a_phase = phase(complex(a[0],a[1]))
    b_phase = phase(complex(b[0],b[1]))
    return (b_phase-a_phase) * 180 / pi


def dot(a,b):
    if min(len(a),len(b)) == 2:
        return  a(0)*b(0) + a(1)*b(1)
    elif len(a) == len(b) == 3:
        return a(0)*b(0) + a(1)*b(1)+ a(2)*b(2)


def cross(a,b):
    return [a(1)*b(2)-a(2)*b(1),a(2)*b(0)-a(0)*b(2),a(0)*b(1)-a(1)*b(0)]


def vector_add(a,b,symbol = "+"):
    import operator
    ops = { "+": operator.add, "-": operator.sub }
    result = []
    if len(a) != len(b):
        raise ArithmeticError("Vectors in different dimensions: R" + str(len(a)) + " != R" + str(len(b)))
    else:
        for i in range(len(a)):
            result.append(ops[symbol](a[i],b[i]))
    return result

def angleToDirect(angle_in_direction_of_unit_circle):
    if angle_in_direction_of_unit_circle > 180:
        return ["turn right" , 360-round(angle_in_direction_of_unit_circle,2)]
    elif 0 < angle_in_direction_of_unit_circle < 180:
        return [ "turn left" , round(angle_in_direction_of_unit_circle,2) ]
    elif -180 < angle_in_direction_of_unit_circle < 0:
        return ["turn right" , round(-angle_in_direction_of_unit_circle,2) ]
    elif angle_in_direction_of_unit_circle < -180:
        return ["turn left" , round(angle_in_direction_of_unit_circle + 360,2) ]
    elif angle_in_direction_of_unit_circle in [180,-180]:
        return ["turn around" ,180]
    elif angle_in_direction_of_unit_circle == 0:
        return  ["go straight",0]


#def coordinate_converter(longitude, latitude, altitude):
