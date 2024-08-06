"""
File: draw_line
Name: 劉庭宇
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE=5

# Global Variable is needed to communicate between main() & class
trigger = 1
previous_x = 0
previous_y = 0

window=GWindow()

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.

    ---Algo---
    1. import global variables
    2. based on trigger value, determine which click it is
    3. setup first click, creating an circle
    4. setup second click, creating a line and deleting the circle
    """

    onmouseclicked(draw) # draw function


def draw(set):
    """
    trigger, previous_x, previous_y must always be "global variable"
    -- IF these variables are in main(), onmouseclicked cannot read,
    -- IF set in draw, it always be 1, or any given number set

    """
    global trigger
    global previous_x
    global previous_y

    # trigger is used to determine if its odd or even click
    if trigger==1:
        # if first click, create circle, change trigger value and give another set of variables to remember circle
        # coordinates
        circle = GOval (SIZE,SIZE,x=set.x-SIZE/2,y=set.y-SIZE/2)
        circle.color = 'black'
        window.add(circle)
        trigger-=1

        # extra set of variables to remember coordinates of x,y cannot be "circle.x" or"circle.y" as it is set as the
        # mid point of the circle, and the "window.get_object_at" command won't be able to identify the circle
        previous_x = set.x
        previous_y = set.y

    else:
        # with trigger != 1, meaning now is the second click. Drawing command must be written after deleting the
        # circle, otherwise the line will be deleted as it overlaps the circle in terms of the layer of the canvas
        previous_circle= window.get_object_at(previous_x,previous_y)
        window.remove(previous_circle)
        line = GLine(previous_x, previous_y, set.x, set.y)
        window.add(line)

        # Reset trigger value
        trigger+=1




if __name__ == "__main__":
    main()
