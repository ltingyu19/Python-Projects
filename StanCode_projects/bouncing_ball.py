"""
File: bouncing_ball
Name: 劉庭宇
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
trigger = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.

    ---Algo---
    1. create window and ball as global
    2. define ball with preset parameters
    3. define onmouseclick event
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    onmouseclicked(start)


def start(event):
    # import global value "trigger" to determine the number of runs
    global trigger

    # define initial vertical speed as 0 and horizontal velocity as Constant VX
    vy = 0
    vx = VX

    # While loop for when trigger is under 3: 0, 1, 2(Running a total for three times)
    while trigger < 3:

        # Set initial movement
        ball.move(vx, vy)

        # Set bouncing if statement to make sure the ball stays in the canvas
        if ball.y <= 0 or ball.y + ball.height >= window.height:
            # definition of vertical speed when bouncing back
            vy = -vy * 0.9

            # EXTRA statement of NEGATIVE vertical speed is needed incase the ball falls out of the canvas
            if vy >= 0 and ball.y + ball.height >= window.height:
                vy = -vy

        # simulating the effects of gravity, allowing vy to add gravity accel in every loop
        vy += GRAVITY

        # DELAY the loop in units to milliseconds, otherwise it would be too fast for visualisation
        pause(DELAY)

        # If the ball falls out of the canvas horizontally, trigger is added and current loop is stopped
        if ball.x > window.width:
            trigger += 1
            break

    # Remove ball and add the ball back to its original position
    window.remove(ball)
    window.add(ball)
    window.add(ball, x=START_X, y=START_Y)
    # window.add(ball) This command allows you to call "ball" but does not specify x,y position
    # If you want to reset its position, you must redefine its x & y coordinates
    # This is because x&y are "optional keyword argument" for GOval


if __name__ == "__main__":
    main()
