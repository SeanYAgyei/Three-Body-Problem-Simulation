# N-Body Gravitational Simulation
  This is an interactive gravitational simulation built using Python that models the motion of multiple bodies under mutual gravitational attraction.
  
  This project originally started off as a three-body simulation but has gradually turned into a N-body simulation that includes real-time visualization, different initial conditions, adjustable physics parameters, and interactive controls.

> **Project Status:** Work in progress. More features, controls, and visualization improvements are coming soon.

## Overview
The simulation calculates the gravitational interaction between each body and updates their positions and velocities over time.

The project currently uses the **Velocity Verlet integration method** for the main simulation, which provides better numerical stability than the original Euler implementation that was used.

This simulation also includes gravitational softening to reduce numerical problems when bodies pass extremely close to eachother.

## Current Features
- N-body gravitational simulation
- Velocity Verlet integration
- Euler integration implementation
- Gravitational softening
- Real-time Matplotlib animation
- Body trajectory/trail visualization
- Randomized initial systems
- Three-body figure-eight preset
- Adjustable gravity
- Adjustable simulation time scale
- Dynamic body count
- Pause/resume
- Clearable trajectory trails
- Body information display
- Select individual bodies
- Live position, velocity, and mass information
- Keyboard controls
- Modular project structure

## Controls
| Key | Action |
  | `Space` | Pause / resume simulation |
  | `R` | Generate a new random system |
  | `F` | Load the figure-eight system |
  | `C` | Clear body trails |
  | `+` / `-` | Increase / decrease gravity |
  | `←` / `→` | Decrease / increase simulation speed |
  | `↑` / `↓` | Decrease / increase body count |
  | `[` / `]` | Select previous / next body |

## Project Structure
  ThreeBodyProblem/
  │
  ├── body.py
  ├── physics.py
  ├── simulation.py
  ├── visualization.py
  ├── control_panel.py
  ├── presets.py
  └── main.py

### `body.py`
Defines individual bodies and stores properties such as:
  - Mass
  - Position
  - Velocity
  - Position history

### `physics.py`
Handles the gravitational calculations used by the simulation, including:
  - Displacement
  - Distance
  - Direction
  - Gravitational force
  - Acceleration

### `simulation.py`
Controls how the physical system changes over time.

Includes:
  - Euler integration
  - Velocity Verlet integration
  - Updating body positions
  - Updating body velocities

### `presets.py`
Contains different starting configurations for the simulation
includes:
  - Random systems
  - Three-body figure-eight orbit

### `visualization.py`
Handles the graphical side of the simulator using Matplotlib.
Includes:
  - Real-time animation
  - Body markers
  - Orbital trails
  - Simulation information displays

### `control_panel.py`
Handles interactive simulation controls and state
includes:
  - Pause/resume
  - Gravity adjustment
  - Time-scale adjustment
  - Body count
  - Preset switching
  - Body selection
  - Status information

### `main.py`
Entry point for the program.
Creates the initial simulation and starts the visualization.

## Physics
For two bodies, the gravitational force is based on Newton's law of universal gravitation:

**F = G(m1 * m2) / r²**


The simulation uses a configurable gravitational constant rather than SI-scale astronomical units.

A softening value is also included to reduce extreme forces when bodies become very close together.

The current simulation primarily uses **Velocity Verlet integration**:


**position -> calculate new acceleration -> velocity**


This provides improved numerical stability compared with the Euler method originally implemented during development.

## Technologies
  - Python
  - NumPy
  - Matplotlib


## Why I Built This
  This project was built to help me visualize and understand the Three-Body Problem, understand the work that goes behind building physics simulations.
  
  I started with a basic implementation of gravitational attraction between three bodies and continued expanding the simulation when I wanted to know how multiple bodies with different masses and gravitational pulls affected eachother.

  
## Planned Features
The project is still a work-in-progess. Potential features/improvements include:

  - Click-to-select bodies
  - Selected-body highlighting
  - Additional orbital presets
  - Better simulation UI
  - More visualization controls
  - Energy and momentum tracking
  - Improved numerical analysis
  - Collision behavior
  - Saving/loading configurations
  - Additional simulation statistics
  - Performance improvements for larger systems

## Running the Project
In order to run, install the required libraries:

```bash
pip install numpy matplotlib
```

Then run:

```bash
python main.py
```
