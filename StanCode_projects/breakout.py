"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name:劉庭宇

YOUR DESCRIPTION HERE
---Algo---
1. call in class defined in another py file
2. define animation loop
3. define winning/losing scenario
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!

    # Defining initial velocity value for the ball / life count for the user
    vx = 0
    vy = 0
    life_count = NUM_LIVES

    # Using while loop to start animation
    while True:
        # Extra while loop to allow 3 life counts for the user
        while life_count > 0 and not graphics.game_cleared():
            # This vx==0, vy==0 if statement is needed so that vx&vy won't be kept refreshing by get_function()
            # Only allowing the ball to gain none zero velocity when it is NOT moving
            if vx == 0 and vy == 0:
                vx = graphics.get_vx()
                vy = graphics.get_vy()

            # moving animation that allows the ball to reflect off the canvas' boundary
            graphics.ball.move(vx, vy)

            # Bouncing of canvas limit (HORIZONTAL)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                vx = -vx
            # Bouncing of canvas limit (CANVAS TOP ONLY)
            if graphics.ball.y <= 0:
                vy = -vy
            # Bouncing off paddle by calling method defined
            if graphics.bouncing_detection():
                vy = -vy

            # Pause
            pause(FRAME_RATE)

            # If the ball falls out of the canvas' bottom, reset the game and life count minus one
            if graphics.ball.y > graphics.window.height:
                life_count -= 1
                graphics.reset()
                vx = 0
                vy = 0
                break

        # If life count == 0, give message of game over and break from loop
        if life_count == 0:
            print('GAME OVER!')
            break

        # If game is cleared as bricks created == bricks eliminated, show winning message and break from loop
        if graphics.game_cleared():
            print('Game Cleared!')
            break


if __name__ == '__main__':
    main()
