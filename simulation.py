from physics import calculate_acceleration


class Simulation:
    def __init__(self, bodies, gravity = 1.0):
        self.bodies = bodies
        self.gravity = gravity


    def update_euler(self, dt):
        accelerations = []

        #Calculate the acceleration of every body
        #using the current positions
        for body in self.bodies:
            acceleration = calculate_acceleration(
                body,
                self.bodies,
                self.gravity
            )

            accelerations.append(acceleration)

        #Update the velocity of each body
        for i in range(len(self.bodies)):
            body = self.bodies[i]
            acceleration = accelerations[i]

            body.velocity[0] += acceleration[0] * dt
            body.velocity[1] += acceleration[1] * dt

        #Update positions using the new velocities
        for body in self.bodies:
            body.position[0] += body.velocity[0] * dt
            body.position[1] += body.velocity[1] * dt

            body.history.append(body.position.copy())


    def update_verlet(self, dt):
        old_accelerations = []

        #Calculate accelerations at the current positions
        for body in self.bodies:
            acceleration = calculate_acceleration(
                body,
                self.bodies,
                self.gravity
            )

            old_accelerations.append(acceleration)

        #Update positions
        for i in range(len(self.bodies)):
            body = self.bodies[i]
            old_acceleration = old_accelerations[i]

            body.position[0] += (
                body.velocity[0] * dt
                + 0.5 * old_acceleration[0] * (dt ** 2)
            )

            body.position[1] += (
                body.velocity[1] * dt
                + 0.5 * old_acceleration[1] * (dt ** 2)
            )

        #Calculate accelerations again at the new positions
        new_accelerations = []

        for body in self.bodies:
            acceleration = calculate_acceleration(
                body,
                self.bodies,
                self.gravity
            )

            new_accelerations.append(acceleration)

        #Update velocities using old and new accelerations
        for i in range(len(self.bodies)):
            body = self.bodies[i]

            old_acceleration = old_accelerations[i]
            new_acceleration = new_accelerations[i]

            body.velocity[0] += (
                0.5
                * (old_acceleration[0] + new_acceleration[0])
                * dt
            )

            body.velocity[1] += (
                0.5
                * (old_acceleration[1] + new_acceleration[1])
                * dt
            )

            body.history.append(body.position.copy())