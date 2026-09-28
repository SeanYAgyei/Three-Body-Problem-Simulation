import numpy as np

###############################################
SOFTENING = 0.05


#Calculates the displacement between body a and b
def displacement(body_a, body_b):

    #Displacement formula
    dx = body_b.position[0] - body_a.position[0]
    dy = body_b.position[1] - body_a.position[1]

    return [dx, dy]


def distance(displacement):
    dx = displacement[0]
    dy = displacement[1]

    #Distance formula
    return np.sqrt(dx ** 2 + dy ** 2)


def direction(displacement):
    distance_value = distance(displacement)

    if distance_value == 0:
        return [0.0, 0.0]

    dx = displacement[0]
    dy = displacement[1]

    direction_x = dx / distance_value
    direction_y = dy / distance_value

    return [direction_x, direction_y]


def gravitational_force(body_a, body_b, gravity):
    displacement_vector = displacement(body_a, body_b)
    distance_value = distance(displacement_vector)

    if distance_value == 0:
        return [0.0, 0.0]

    direction_vector = direction(displacement_vector)

    #Force magnitude equation
    force_magnitude = (
        gravity * body_a.mass * body_b.mass
    ) / (distance_value ** 2 + SOFTENING ** 2)

    fx = force_magnitude * direction_vector[0]
    fy = force_magnitude * direction_vector[1]

    return [fx, fy]


def calculate_acceleration(body, bodies, gravity):
    total_force = [0.0, 0.0]

    for other_body in bodies:
        if other_body == body:
            continue

        force = gravitational_force(body, other_body, gravity)

        total_force[0] += force[0]
        total_force[1] += force[1]

    #We calculate F = m * a
    #Solving for a (a = F / m)
    ax = total_force[0] / body.mass
    ay = total_force[1] / body.mass

    return [ax, ay]