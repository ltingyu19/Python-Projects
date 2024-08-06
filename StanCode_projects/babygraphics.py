"""
File: babygraphics.py
Name: 劉庭宇
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # ---algo---
    # 1. define parameters inherited from constants
    # 2. calculate x coordinates in accordance to year_index predefined
    # 3. return x coordinates

    # define parameters
    margin = GRAPH_MARGIN_SIZE
    right_limit = width - margin
    left_limit = margin

    # define equation
    spacing = (right_limit - left_limit) / len(YEARS)
    x_coordinate = margin + spacing * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # ---algo---
    # 1. define parameters from constants
    # 2. create upper/lower canvas margin lines
    # 3. using the functions defined in get_x_coordinates to draw vertical lines

    # define parameters
    line_margin = GRAPH_MARGIN_SIZE
    width = CANVAS_WIDTH
    height = CANVAS_HEIGHT
    # upper margin line (x1 = margin, y1 = margin, x2 = window.width-margin, y2 = margin)
    # lower margin line (x1 = margin, y1 = window.height - margin, x2= window.width-margin, y2=y1)
    canvas.create_line(line_margin, line_margin, width - line_margin, line_margin, width=LINE_WIDTH)
    canvas.create_line(line_margin, height - line_margin, width - line_margin, height - line_margin, width=LINE_WIDTH)

    # ---vertical lines---
    count = 0
    # loop over list to get vertical lines for all years in the list
    for year in YEARS:
        vertical_line_x = get_x_coordinate(width, count)
        canvas.create_line(vertical_line_x, line_margin, vertical_line_x, height, width=LINE_WIDTH)
        canvas.create_text(vertical_line_x + TEXT_DX, height - line_margin, text=year, anchor=tkinter.NW)
        count += 1


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # ---algo---
    # 1. search the dictionary for keys matching lookup_names
    # 2. extract data , y coordinate == value of key, x coordinate = get x coordinate function
    # 3. with data extracted draw lines and names

    # define parameters
    colors = COLORS
    margin = GRAPH_MARGIN_SIZE
    right_limit = CANVAS_WIDTH - margin
    left_limit = margin
    spacing = (right_limit - left_limit) / len(YEARS)
    height = CANVAS_HEIGHT
    color_num = 0

    # loop over dictionary/lists to find matching data
    for name in lookup_names:
        for matching_name in name_data:
            if name in matching_name:
                data_set = name_data[matching_name]

                # define rank value list to store rank value
                rk = []
                # loop over years to find data for each year
                for year in YEARS:
                    if str(year) in data_set:
                        rank_value = (data_set[str(year)])
                        rk.append(rank_value)
                    else:
                        rk.append(0)

                # define iter_line and use it to control looping iterations since we're drawing i-1 lines
                # normalized equation is used to correctly display the data in the canvas
                iter_line = 0
                for i in range(len(rk)):

                    # keep drawing before hitting max len(rk)
                    if iter_line < (len(rk) - 1):
                        normalize_y = (int(rk[i]) / 1000) * (height - margin * 2) + margin
                        normalize_y_nxt = (int(rk[i + 1]) / 1000) * (height - margin * 2) + margin

                        # define normalize_y / normalize_y_nxt value accordingly to the value of the margin
                        if normalize_y <= margin:
                            normalize_y = height - margin

                        if normalize_y_nxt <= margin:
                            normalize_y_nxt = height - margin

                        canvas.create_line(margin + (spacing * i), normalize_y, margin + (spacing * (i + 1)),
                                           normalize_y_nxt, fill=colors[color_num], width=LINE_WIDTH)

                        # create text beside data points and if data is 0, show *
                        if int(rk[i]) > 0:
                            canvas.create_text(margin + (spacing * i), normalize_y, text=name + ' ' + str(rk[i]),
                                               fill=colors[color_num], anchor=tkinter.SW)
                        else:
                            canvas.create_text(margin + (spacing * i), normalize_y, text=name + ' *',
                                               fill=colors[color_num], anchor=tkinter.SW)
                        iter_line += 1
                    else:
                        # obob case
                        canvas.create_text(margin + (spacing * i), normalize_y_nxt, text=name + ' ' + str(rk[i]),
                                           fill=colors[color_num], anchor=tkinter.SW)

                # loop over the color list to ensure colors are changed
                color_num += 1
                if color_num > 3:
                    color_num = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
