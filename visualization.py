import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from control_panel import ControlPanel


def draw_graph(simulation):
    for body in simulation.bodies:
        x_history = []
        y_history = []

        for position in body.history:
            x_history.append(position[0])
            y_history.append(position[1])

        plt.plot(x_history, y_history)

        plt.scatter(
            body.position[0],
            body.position[1]
        )

    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.title("Three-body simulation")
    plt.axis("equal")
    plt.grid()

    plt.show()



#controls frames/speed
def animate_graph(
    simulation,
    frames = 10000,
    dt = 0.05,
    interval = 20
):
    fig, ax = plt.subplots()

    ax.set_xlabel("X position")
    ax.set_ylabel("Y position")
    ax.set_title("Three-body simulation")

    ax.set_aspect("equal")
    ax.grid()

#Controls graph zoom/size
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)


    status_text = ax.text(
        0.02,
        0.98,
        "",
        transform = ax.transAxes,
        verticalalignment = "top",
        fontsize = 7,
        bbox = dict(
            facecolor = "white",
            alpha = 0.5
        )
    )


    body_text = ax.text(
        0.98,
        0.72,
        "",
        transform = ax.transAxes,
        horizontalalignment = "right",
        verticalalignment = "top",
        fontsize = 7,
        bbox = dict(
            facecolor = "white",
            alpha = 0.5
        )

def on_click(event):
    if event.

    )


#controls key panel
    controls_text = ax.text(
        0.98,
        0.98,
        (
            "Controls\n"
            "Space : Pause/Resume\n"
            "R     : Random system\n"
            "F     : Figure Eight\n"
            "C     : Clear trails\n"
            "+ / - : Gravity\n"
            "← / → : Time scale\n"
            "↑ / ↓ : Body count\n"
            "[ / ] : Select body"
        ),
        transform = ax.transAxes,
        horizontalalignment = "right",
        verticalalignment = "top",
        fontsize = 7,
        bbox = dict(
            facecolor = "white",
            alpha = 0.5
        )
    )


    trails = []
    points = []


    def rebuild_artists():
        for trail in trails:
            trail.remove()

        for point in points:
            point.remove()

        trails.clear()
        points.clear()


        for body in simulation.bodies:

        #controls trail thickness
            trail, = ax.plot(
                [],
                [],
                linewidth = 1
            )

            #controls the shape of icon
            point, = ax.plot(
                [],
                [],
                marker = "*",
                linestyle = "None"
            )

            trails.append(trail)
            points.append(point)


    rebuild_artists()


    control_panel = ControlPanel(
        simulation,
        rebuild_artists,
        fig
    )


    def update_frame(frame):

    #if simulation is paused, physics stop
        if control_panel.paused:
            status_text.set_text(
                control_panel.build_status_text()
            )

            body_text.set_text(
                control_panel.build_body_text()
            )

            return trails + points


        simulation.update_verlet(
            dt * control_panel.time_scale
        )


        for i, body in enumerate(simulation.bodies):

            x_history = []
            y_history = []

            for position in body.history:
                x_history.append(position[0])
                y_history.append(position[1])

            trails[i].set_data(
                x_history,
                y_history
            )

            points[i].set_data(
                [body.position[0]],
                [body.position[1]]
            )


        status_text.set_text(
            control_panel.build_status_text()
        )

        body_text.set_text(
            control_panel.build_body_text()
        )

        return trails + points


#listens for keyboard input
    fig.canvas.mpl_connect(
        "key_press_event",
        control_panel.on_key
    )


    animation = FuncAnimation(
        fig,
        update_frame,
        frames = frames,
        interval = interval,
        blit = False
    )


    plt.show()