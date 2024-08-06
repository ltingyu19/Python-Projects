"""
File: my_drawing
Name: 劉庭宇
----------------------

"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow

window = GWindow(width=900, height=1250, title='StanCode Maverick')


def main():
    """
    Title: Top Coding

    Top gun has always been my favorite movie and I have always loved airplanes.
    Therefore, I decided to make a similar movie poster with one of the most famous phrase from the movie.
    Which was, "I feel the need, the need for speed" where I chanced the word "Speed" to "Coding" since
    this is a python assignment!
    """

    # This part is responsible for painting the background
    paint()
    # This part is responsible for painting the fuselage and the wing
    fuselage_wing()
    # This part is reponsible for showing the texts on the painting
    word()


def fuselage_wing():
    # Inner Fuselage
    lerx = GArc(500, 1500, 0, 90, x=-130, y=-70)
    lerx.filled = True
    lerx.fill_color = 'black'
    lerx.color = 'black'
    window.add(lerx)

    wing = GPolygon()
    wing.add_vertex((0, 305))
    wing.add_vertex((120, 305))
    wing.add_vertex((720, 550))
    wing.add_vertex((720, 700))
    wing.add_vertex((0, 750))
    wing.filled = True
    wing.fill_color = 'black'
    wing.color = 'black'
    window.add(wing)

    tip = GPolygon()
    tip.add_vertex((720, 515))
    tip.add_vertex((730, 505))
    tip.add_vertex((730, 700))
    tip.add_vertex((720, 700))
    tip.filled = True
    tip.fill_color = 'black'
    tip.color = 'black'
    window.add(tip)

    lofu = GPolygon()
    lofu.add_vertex((0, 750))
    lofu.add_vertex((110, 740))
    lofu.add_vertex((80, 1100))
    lofu.add_vertex((0, 1100))
    lofu.filled = True
    lofu.fill_color = 'black'
    lofu.color = 'black'
    window.add(lofu)

    hstab = GPolygon()
    hstab.add_vertex((95, 820))
    hstab.add_vertex((350, 1100))
    hstab.add_vertex((360, 1200))
    hstab.add_vertex((325, 1210))
    hstab.add_vertex((10, 1050))
    hstab.filled = True
    hstab.fill_color = 'black'
    hstab.color = 'black'
    window.add(hstab)

    nozzel = GPolygon()
    nozzel.add_vertex((0, 1100))
    nozzel.add_vertex((80, 1100))
    nozzel.add_vertex((75, 1150))
    nozzel.add_vertex((0, 1150))
    nozzel.filled = True
    nozzel.fill_color = 'black'
    nozzel.color = 'black'
    window.add(nozzel)

    # in_fuselage = GRect(width=200, height=800, x=0, y=0)
    # in_fuselage.filled = True
    # in_fuselage.fill_color = 'gray'
    # window.add(in_fuselage)


def paint():
    t1 = GRect(900, 25, x=0, y=0)
    t1.filled = True
    t1.fill_color = 'aliceblue'
    t1.color = 'aliceblue'
    window.add(t1)

    t2 = GRect(900, 25, x=0, y=25)
    t2.filled = True
    t2.fill_color = 'azure'
    t2.color = 'azure'
    window.add(t2)

    t3 = GRect(900, 25, x=0, y=50)
    t3.filled = True
    t3.fill_color = 'lightcyan'
    t3.color = 'lightcyan'
    window.add(t3)

    t4 = GRect(900, 25, x=0, y=75)
    t4.filled = True
    t4.fill_color = 'lightblue'
    t4.color = 'lightblue'
    window.add(t4)

    t5 = GRect(900, 25, x=0, y=100)
    t5.filled = True
    t5.fill_color = 'skyblue'
    t5.color = 'skyblue'
    window.add(t5)

    t6 = GRect(900, 25, x=0, y=125)
    t6.filled = True
    t6.fill_color = 'cyan'
    t6.color = 'cyan'
    window.add(t6)

    t7 = GRect(900, 25, x=0, y=150)
    t7.filled = True
    t7.fill_color = 'deepskyblue'
    t7.color = 'deepskyblue'
    window.add(t7)

    t8 = GRect(900, 25, x=0, y=175)
    t8.filled = True
    t8.fill_color = 'lightskyblue'
    t8.color = 'lightskyblue'
    window.add(t8)

    t9 = GRect(900, 25, x=0, y=200)
    t9.filled = True
    t9.fill_color = 'powderblue'
    t9.color = 'powderblue'
    window.add(t9)

    t10 = GRect(900, 25, x=0, y=225)
    t10.filled = True
    t10.fill_color = 'peachpuff'
    t10.color = 'peachpuff'
    window.add(t10)

    t11 = GRect(900, 25, x=0, y=250)
    t11.filled = True
    t11.fill_color = 'lightcoral'
    t11.color = 'lightcoral'
    window.add(t11)

    t12 = GRect(900, 25, x=0, y=275)
    t12.filled = True
    t12.fill_color = 'lightsalmon'
    t12.color = 'lightsalmon'
    window.add(t12)

    t13 = GRect(900, 25, x=0, y=300)
    t13.filled = True
    t13.fill_color = 'sandybrown'
    t13.color = 'sandybrown'
    window.add(t13)

    t14 = GRect(900, 25, x=0, y=325)
    t14.filled = True
    t14.fill_color = 'darksalmon'
    t14.color = 'darksalmon'
    window.add(t14)

    t15 = GRect(900, 25, x=0, y=350)
    t15.filled = True
    t15.fill_color = 'peru'
    t15.color = 'peru'
    window.add(t15)

    t16 = GRect(900, 25, x=0, y=375)
    t16.filled = True
    t16.fill_color = 'steelblue'
    t16.color = 'steelblue'
    window.add(t16)

    t17 = GRect(900, 25, x=0, y=400)
    t17.filled = True
    t17.fill_color = 'cadetblue'
    t17.color = 'cadetblue'
    window.add(t17)

    t18 = GRect(900, 25, x=0, y=425)
    t18.filled = True
    t18.fill_color = 'cornflowerblue'
    t18.color = 'cornflowerblue'
    window.add(t18)

    t19 = GRect(900, 25, x=0, y=450)
    t19.filled = True
    t19.fill_color = 'dodgerblue'
    t19.color = 'dodgerblue'
    window.add(t19)

    t20 = GRect(900, 25, x=0, y=475)
    t20.filled = True
    t20.fill_color = 'lightsalmon'
    t20.color = 'lightsalmon'
    window.add(t20)

    t21 = GRect(900, 25, x=0, y=500)
    t21.filled = True
    t21.fill_color = 'darkorange'
    t21.color = 'darkorange'
    window.add(t21)

    t22 = GRect(900, 25, x=0, y=525)
    t22.filled = True
    t22.fill_color = 'orange'
    t22.color = 'orange'
    window.add(t22)

    t23 = GRect(900, 25, x=0, y=550)
    t23.filled = True
    t23.fill_color = 'orangered'
    t23.color = 'orangered'
    window.add(t23)

    t24 = GRect(900, 25, x=0, y=575)
    t24.filled = True
    t24.fill_color = 'chocolate'
    t24.color = 'chocolate'
    window.add(t24)

    t25 = GRect(900, 25, x=0, y=600)
    t25.filled = True
    t25.fill_color = 'brown'
    t25.color = 'brown'
    window.add(t25)

    t26 = GRect(900, 25, x=0, y=625)
    t26.filled = True
    t26.fill_color = 'firebrick'
    t26.color = 'firebrick'
    window.add(t26)

    t27 = GRect(900, 25, x=0, y=650)
    t27.filled = True
    t27.fill_color = 'darkred'
    t27.color = 'darkred'
    window.add(t27)

    t28 = GRect(900, 25, x=0, y=675)
    t28.filled = True
    t28.fill_color = 'sienna'
    t28.color = 'sienna'
    window.add(t28)

    t29 = GRect(900, 25, x=0, y=700)
    t29.filled = True
    t29.fill_color = 'burlywood'
    t29.color = 'burlywood'
    window.add(t29)

    t30 = GRect(900, 25, x=0, y=725)
    t30.filled = True
    t30.fill_color = 'tan'
    t30.color = 'tan'
    window.add(t30)

    t31 = GRect(900, 525, x=0, y=750)
    t31.filled = True
    t31.fill_color = 'saddlebrown'
    t31.color = 'saddlebrown'
    window.add(t31)


def word():
    ww = GLabel('I FEEL THE NEED', x=75, y=545)

    ww.font = 'Times New Roman-40-bold-italic'
    ww.color = 'lightcyan'
    window.add(ww)

    ww2 = GLabel('THE NEED FOR CODING!', x=75, y=650)
    ww2.font = 'Times New Roman-40-bold-italic'
    ww2.color = 'lightcyan'
    window.add(ww2)

    py = GLabel('PYTHON', x=550, y=1250)
    py.font = 'Times New Roman-60-bold-italic'
    py.color = 'darkred'
    window.add(py)

    st = GLabel('stanCode', x=460, y=1150)
    st.font = 'Times New Roman-80-bold-italic'
    st.color = 'darkred'
    window.add(st)


if __name__ == '__main__':
    main()
