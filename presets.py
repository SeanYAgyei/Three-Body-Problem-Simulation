from body import Body
import random

def create_figure_eight():
    body1 = Body(
        mass = 1.0,
        position = [-0.97000436, 0.24308753],
        velocity = [0.466203685, 0.43236573]
    )

    body2 = Body(
        mass = 1.0,
        position=[0.97000436, -0.24308753],
        velocity=[0.466203685, 0.43236573]

    )

    body3 = Body(
        mass = 1.0,
        position=[0.0, 0.0],
        velocity=[-0.93240737, -0.86473146]
    )

    return[body1, body2, body3]


def create_random_system(
    body_count = 3,
    position_range = 2.0,
    velocity_range = 0.5,
    min_mass = 0.5,
    max_mass = 3.5
):
    bodies = []

    for _ in range(body_count):
        mass = random.uniform(min_mass, max_mass)

        position = [
            random.uniform(-position_range, position_range),
            random.uniform(-position_range, position_range)
        ]

        velocity = [
            random.uniform(-velocity_range, velocity_range),
            random.uniform(-velocity_range, velocity_range)
        ]

        body = Body(
            mass = mass,
            position = position,
            velocity = velocity
        ) 

        bodies.append(body)

    return bodies