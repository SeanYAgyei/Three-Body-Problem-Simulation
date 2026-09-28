from presets import create_random_system
from simulation import Simulation
from visualization import animate_graph


bodies = create_random_system(
    body_count = 3,
    position_range = 3.0,
    velocity_range = 1,
    min_mass = 10,
    max_mass = 50
)

simulation = Simulation(
    bodies, 
    gravity = 2.0)

animate_graph(
    simulation,
    frames = 10000,
    dt = 0.01,
    interval = 5
)