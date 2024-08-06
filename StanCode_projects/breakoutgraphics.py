"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Name:劉庭宇

YOUR DESCRIPTION HERE
--- Algo---
1. Define class (Create paddle, bricks, ball) basic graphic components
2. Define mouseevent functions
3. Define ball motion and velocity in preparation for animation
4. Define bouncing detections and functions for eliminating bricks
5. Define GAME OVER / GAME CLEARED functions
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) // 2, y=window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball_initial_x = (self.window.width - self.ball.width) // 2
        self.ball_initial_y = (self.window.height - self.ball.height) // 2
        self.window.add(self.ball, x=self.ball_initial_x, y=self.ball_initial_y)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_moving = False
        self.bricks_cleared = 0

        # Creating a label
        self.score_label = GLabel('Score=> ' + str(self.bricks_cleared))
        self.score_label.font = 'Times New Roman-15-bold-italic'
        self.score_label.color = 'blue'
        self.window.add(self.score_label, x=0, y=self.score_label.height)

        # Initialize our mouse listeners
        onmousemoved(self.follow_mouse)
        onmouseclicked(self.event)

        # ------This Part defines the functions for building the bricks based on Constants that are predefined------
        # based on CONSTANT:BRICK_ROWS, setup bricks by calling methods defined below using if/elif statements
        if brick_rows <= 2:
            self.set_red_brick()
        elif brick_rows <= 4:
            self.set_red_brick()
            self.set_orange_brick()
        elif brick_rows <= 6:
            self.set_red_brick()
            self.set_orange_brick()
            self.set_yellow_brick()
        elif brick_rows <= 8:
            self.set_red_brick()
            self.set_orange_brick()
            self.set_yellow_brick()
            self.set_green_brick()
        else:
            self.set_red_brick()
            self.set_orange_brick()
            self.set_yellow_brick()
            self.set_green_brick()
            self.set_blue_brick()

    # ------This Part defines the methods that are needed------

    # ------This Part defines the functions for building the bricks based on Constants that are predefined------
    # The set_()_brick functions below are defined in the manner of:
    # 1. Define initial brick(size/position/color/spacing based on CONSTANTS predefined)
    # 2. Using "for" statement to create bricks HORIZONTALLY in accordance to CONSTANT: BRICK_COLS
    # 3. Since each color would have "2" lines, an EXTRA if statement is used to setup "EVEN" number rows
    # 4. If a "EVEN" number rows is needed, the commands are the same as creating "ODD" number rows.
    def set_red_brick(self, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_rows=BRICK_ROWS,
                      brick_cols=BRICK_COLS, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING):

        self.brick = GRect(brick_width, brick_height)
        self.brick.filled = True
        self.brick.fill_color = 'red'
        self.window.add(self.brick, x=0, y=brick_offset)

        for i in range(1, brick_cols):
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'red'
            x_offset = brick_width * i + brick_spacing * i
            self.window.add(self.brick, x=x_offset, y=brick_offset)

        if brick_rows >= 2:
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'red'
            self.window.add(self.brick, x=0, y=brick_height + brick_offset + brick_spacing)

            for i in range(1, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'red'
                x_offset = brick_width * i + brick_spacing * i
                self.window.add(self.brick, x=x_offset, y=brick_height + brick_offset + brick_spacing)

    def set_orange_brick(self, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_rows=BRICK_ROWS,
                         brick_cols=BRICK_COLS, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING):

        self.brick = GRect(brick_width, brick_height)
        self.brick.filled = True
        self.brick.fill_color = 'orange'
        self.window.add(self.brick, x=0, y=brick_offset + brick_height * 2 + brick_spacing * 2)

        for i in range(1, brick_cols):
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'orange'
            x_offset = brick_width * i + brick_spacing * i
            self.window.add(self.brick, x=x_offset, y=brick_offset + brick_height * 2 + brick_spacing * 2)

        if brick_rows > 3:
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'orange'
            self.window.add(self.brick, x=0, y=brick_offset + brick_height * 3 + brick_spacing * 3)

            for i in range(1, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'orange'
                x_offset = brick_width * i + brick_spacing * i
                self.window.add(self.brick, x=x_offset, y=brick_offset + brick_height * 3 + brick_spacing * 3)

    def set_yellow_brick(self, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_rows=BRICK_ROWS,
                         brick_cols=BRICK_COLS, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING):

        self.brick = GRect(brick_width, brick_height)
        self.brick.filled = True
        self.brick.fill_color = 'yellow'
        self.window.add(self.brick, x=0, y=brick_offset + brick_height * 4 + brick_spacing * 4)

        for i in range(1, brick_cols):
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'yellow'
            x_offset = brick_width * i + brick_spacing * i
            self.window.add(self.brick, x=x_offset, y=brick_offset + brick_height * 4 + brick_spacing * 4)

        if brick_rows > 5:
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'yellow'
            self.window.add(self.brick, x=0, y=brick_offset + brick_height * 5 + brick_spacing * 5)

            for i in range(1, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'yellow'
                x_offset = brick_width * i + brick_spacing * i
                self.window.add(self.brick, x=x_offset, y=brick_offset + brick_height * 5 + brick_spacing * 5)

    def set_green_brick(self, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_rows=BRICK_ROWS,
                        brick_cols=BRICK_COLS, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING):

        self.brick = GRect(brick_width, brick_height)
        self.brick.filled = True
        self.brick.fill_color = 'green'
        self.window.add(self.brick, x=0, y=brick_offset + brick_height * 6 + brick_spacing * 6)

        for i in range(1, brick_cols):
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'green'
            x_offset = brick_width * i + brick_spacing * i
            self.window.add(self.brick, x=x_offset, y=brick_offset + brick_height * 6 + brick_spacing * 6)

        if brick_rows > 7:
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'green'
            self.window.add(self.brick, x=0, y=brick_offset + brick_height * 7 + brick_spacing * 7)

            for i in range(1, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'green'
                x_offset = brick_width * i + brick_spacing * i
                self.window.add(self.brick, x=x_offset, y=brick_offset + brick_height * 7 + brick_spacing * 7)

    def set_blue_brick(self, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_rows=BRICK_ROWS,
                       brick_cols=BRICK_COLS, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING):

        self.brick = GRect(brick_width, brick_height)
        self.brick.filled = True
        self.brick.fill_color = 'blue'
        self.window.add(self.brick, x=0, y=brick_offset + brick_height * 8 + brick_spacing * 8)

        for i in range(1, brick_cols):
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'blue'
            x_offset = brick_width * i + brick_spacing * i
            self.window.add(self.brick, x=x_offset, y=brick_offset + brick_height * 8 + brick_spacing * 8)

        if brick_rows > 9:
            self.brick = GRect(brick_width, brick_height)
            self.brick.filled = True
            self.brick.fill_color = 'blue'
            self.window.add(self.brick, x=0, y=brick_offset + brick_height * 9 + brick_spacing * 9)

            for i in range(1, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'blue'
                x_offset = brick_width * i + brick_spacing * i
                self.window.add(self.brick, x=x_offset, y=brick_offset + brick_height * 9 + brick_spacing * 9)

    # ------This Part defines the mouse events that are needed------

    # This method defines how the paddle would follow user mouse
    def follow_mouse(self, mouse, paddle_offset=PADDLE_OFFSET):

        # if the x coordinate of user mouse if in the created window, paddle should be centered to the mouse
        if self.paddle.width / 2 <= mouse.x <= self.window.width - (self.paddle.width / 2):
            self.paddle.x = mouse.x - self.paddle.width / 2
            self.paddle.y = mouse.y * 0 + self.window.height - paddle_offset

        # If the x coordinate of the mouse is now "BIGGER" than a value that might cause the paddle to partially
        # disappear, x coordinate of paddle is defined to the maximum value where none of the paddle would disappear
        elif mouse.x > self.window.width - (self.paddle.width / 2):
            self.paddle.x = self.window.width - self.paddle.width

        # If the x coordinate of the mouse is now "SMALLER" than a value that might cause the paddle to partially
        # disappear, x coordinate of paddle is defined to the maximum value where none of the paddle would disappear
        elif mouse.x < self.paddle.width / 2:
            self.paddle.x = 0

    # This method defines how ball would gain velocity
    def event(self, trigger):
        # With mouse event, methods set_speed_x/y() would be triggered to setup speed for dx & dy
        self.__dx = self.set_speed_x()
        self.__dy = self.set_speed_y()

    # ------This Part defines the velocity for the ball------
    def set_speed_x(self, max_x_speed=MAX_X_SPEED):
        # Commands to setup dx using random function
        self.vx = random.randint(1, max_x_speed)
        if random.random() > 0.5:
            self.vx = -self.vx
        return self.vx

    def set_speed_y(self, initial_y_speed=INITIAL_Y_SPEED):
        # Command to setup dy using CONSTANT
        return initial_y_speed

    def get_vx(self):
        # Since dx is defined as private variable, this getter function would allow user to gain dx
        return self.__dx

    def get_vy(self):
        # Since dy is defined as private variable, this getter function would allow user to gain dy
        return self.__dy

    # ------This Part defines the bouncing mechanism of the ball------

    # This part defines how the ball would deflect from bricks/walls/paddle and how bricks are eliminated
    def bouncing_detection(self):

        # Initial impact trigger is defined so one a certain corner has detect impact, there wouldn't be an extra act
        # of elimination that might cause the game to act funny
        impact_trigger = False

        # This part defines the "left upper corner"
        if not impact_trigger:
            # Define possible obj to be eliminated
            maybe_brick_lu = self.window.get_object_at(self.ball.x, self.ball.y)
            # Setup criteria for obj to be eliminated (MUST NOT BE PADDLE/LABEL/None)
            if maybe_brick_lu is not None and maybe_brick_lu is not self.paddle and maybe_brick_lu is not self.score_label:
                # Once found such obj(BRICKS), remove obj, reset impact_trigger to TRUE, bricks_clear number is recorded
                self.window.remove(maybe_brick_lu)
                impact_trigger = True
                self.bricks_cleared += 1

        # This part defines the "Right upper corner"
        if not impact_trigger:
            # Define possible obj to be eliminated
            maybe_brick_ru = self.window.get_object_at(self.ball.x + 2 * self.ball.width, self.ball.y)
            if maybe_brick_ru is not None and maybe_brick_ru is not self.paddle and maybe_brick_ru is not self.score_label:
                # Once found such obj(BRICKS), remove obj, reset impact_trigger to TRUE, bricks_clear number is recorded
                self.window.remove(maybe_brick_ru)
                impact_trigger = True
                self.bricks_cleared += 1

        # This part defines the "Left Lower corner"
        if not impact_trigger:
            # Define possible obj to be eliminated
            maybe_brick_ll = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball.height)
            if maybe_brick_ll is not None and maybe_brick_ll is not self.paddle and maybe_brick_ll is not self.score_label:
                # Once found such obj(BRICKS), remove obj, reset impact_trigger to TRUE, bricks_clear number is recorded
                self.window.remove(maybe_brick_ru)
                impact_trigger = True
                self.bricks_cleared += 1
            # Since the lower part of the ball would be the one that touches the paddle, an extra if statements is
            # needed to set impact_trigger to True so is would still BOUNCE back
            if maybe_brick_ll is self.paddle:
                impact_trigger = True

        # This part defines the "Right Lower corner"
        if not impact_trigger:
            # Define possible obj to be eliminated
            maybe_brick_rl = self.window.get_object_at(self.ball.x + 2 * self.ball.width,
                                                       self.ball.y + 2 * self.ball.height)
            if maybe_brick_rl is not None and maybe_brick_rl is not self.paddle and maybe_brick_rl is not self.score_label:
                # Once found such obj(BRICKS), remove obj, reset impact_trigger to TRUE, bricks_clear number is recorded
                self.window.remove(maybe_brick_ru)
                impact_trigger = True
                self.bricks_cleared += 1
            # Since the lower part of the ball would be the one that touches the paddle, an extra if statements is
            # needed to set impact_trigger to True so is would still BOUNCE back
            if maybe_brick_rl is self.paddle:
                impact_trigger = True

        # Using the bricks cleared value collected from above, score can be recorded
        # !!! Instead of creating label here, label should be CREATED IN MAIN CLASS(__init__), otherwise, label, font
        # would be created along with numerous loops and causing lags for the game
        self.score_label.text = 'Score: ' + str(self.bricks_cleared)

        # Reset ball impaction trigger to False
        ball_impacted = False

        # Setup impact trigger
        if impact_trigger:
            ball_impacted = True
            impact_trigger = False
            return ball_impacted

    # This part defines on resetting the ball's position/velocity once failed
    def reset(self):
        if self.ball.y > self.window.height:
            self.window.add(self.ball, x=self.ball_initial_x, y=self.ball_initial_y)
            self.__dx = 0
            self.__dy = 0

    # This part defines the winning message once game is cleared
    def game_cleared(self):
        game_cleared = False
        global bricks_cleared
        if self.bricks_cleared >= BRICK_ROWS * BRICK_COLS:
            self.window.clear()
            game_cleared = True
            return game_cleared
