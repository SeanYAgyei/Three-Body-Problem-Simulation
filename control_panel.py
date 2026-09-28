from presets import create_random_system, create_figure_eight


class ControlPanel:
    def __init__(self, simulation, rebuild_artists, figure):
        self.simulation = simulation
        self.rebuild_artists = rebuild_artists
        self.figure = figure

        self.paused = False
        self.time_scale = 1.0
        self.current_system = "Random"
        self.body_count = len(simulation.bodies)
        self.selected_body_index = 0


    def build_status_text(self):
        return (
            f"System: {self.current_system}\n"
            f"Gravity: {self.simulation.gravity:.2f}\n"
            f"Time Scale: {self.time_scale:.2f}\n"
            f"Body Count: {len(self.simulation.bodies)}\n"
            f"Paused: {self.paused}"
        )


    def build_body_text(self):
        if len(self.simulation.bodies) == 0:
            return "No bodies"

        body = self.simulation.bodies[self.selected_body_index]

        return (
            f"Body {self.selected_body_index + 1}\n"
            f"Mass: {body.mass:.2f}\n"
            f"Position: "
            f"({body.position[0]:.2f}, {body.position[1]:.2f})\n"
            f"Velocity: "
            f"({body.velocity[0]:.2f}, {body.velocity[1]:.2f})"
        )


    def on_key(self, event):

        if event.key == " ":
            self.paused = not self.paused


        #restarts simulation
        elif event.key == "r":
            self.simulation.bodies = create_random_system(
                body_count = self.body_count,
                position_range = 2.0,
                velocity_range = 0.5,
                min_mass = 0.5,
                max_mass = 3.0
            )

            self.current_system = "Random"
            self.selected_body_index = 0

            self.rebuild_artists()
            self.figure.canvas.draw_idle()


        elif event.key == "up":
            self.body_count += 1

            self.simulation.bodies = create_random_system(
                body_count = self.body_count,
                position_range = 2.0,
                velocity_range = 0.5,
                min_mass = 0.5,
                max_mass = 3.0
            )

            self.current_system = "Random"
            self.selected_body_index = 0

            self.rebuild_artists()
            self.figure.canvas.draw_idle()


        elif event.key == "down":
            self.body_count -= 1

            if self.body_count < 2:
                self.body_count = 2

            self.simulation.bodies = create_random_system(
                body_count = self.body_count,
                position_range = 2.0,
                velocity_range = 0.5,
                min_mass = 0.5,
                max_mass = 3.0
            )

            self.current_system = "Random"
            self.selected_body_index = 0

            self.rebuild_artists()
            self.figure.canvas.draw_idle()


        #creates figure eight simulation with 'f' key
        elif event.key == "f":
            self.simulation.bodies = create_figure_eight()
            self.simulation.gravity = 1.0

            self.body_count = 3
            self.current_system = "Figure Eight"
            self.selected_body_index = 0

            self.rebuild_artists()
            self.figure.canvas.draw_idle()


        #restarts trails of bodies with 'c' key
        elif event.key == "c":
            for body in self.simulation.bodies:
                body.history = [body.position.copy()]

            self.figure.canvas.draw_idle()


        #increases simulation gravity with '+' and '=' key
        elif event.key in ["+", "="]:
            self.simulation.gravity *= 1.2


        #decreases simulation gravity with '-' key
        elif event.key == "-":
            self.simulation.gravity /= 1.2


        #increases simulation time scale with right arrow key
        elif event.key == "right":
            self.time_scale *= 1.5


        #decreases simulation time scale with left arrow key
        elif event.key == "left":
            self.time_scale /= 1.5


        #selects next body
        elif event.key == "]":
            self.selected_body_index += 1

            if self.selected_body_index >= len(self.simulation.bodies):
                self.selected_body_index = 0


        #selects previous body
        elif event.key == "[":
            self.selected_body_index -= 1

            if self.selected_body_index < 0:
                self.selected_body_index = len(self.simulation.bodies) - 1