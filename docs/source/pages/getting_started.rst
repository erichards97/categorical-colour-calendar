##############################################
Getting Started
##############################################

Installation
#############
::

    pip install categorical-colour-calendar


Usage
#############
Basic
=======
Automatically generated colours
::

    import pandas as pd
    from cccalendar import draw_colour_calendar
    my_data = pd.Series({
        '2022-01-04': 'Sprint start',
        '2022-01-14': 'Sprint planning',
        '2022-01-14': 'Sprint end',
        '2022-01-17': 'Sprint start',
        '2022-01-27': 'Sprint planning',
        '2022-01-28': 'Sprint end',
        '2022-01-31': 'Sprint start'
    })
    draw_colour_calendar(my_data,
                         min_date='2022-01-04',
                         max_date='2022-01-28',
                         exclude_dates=['2022-01-08', '2022-01-09',
                                        '2022-01-15', '2022-01-16',
                                        '2022-01-22', '2022-01-23',
                                        '2022-01-29', '2022-01-30'])

.. image:: /_static/ex1.png
  :width: 400
  :alt: Example 1 image

Defined Colours
=================
Specifying a colour map and the default square colour
::

    import pandas as pd
    from cccalendar import draw_colour_calendar
    my_data = pd.Series({
        '2021-01-01': 'event_one',
        '2021-01-07': 'event_two',
        '2021-01-10': 'event_three',
        '2021-01-14': 'event_four',
        '2021-01-19': 'event_one',
        '2021-01-23': 'event_two',
    })
    colour_map = {
        'event_one': 'b',
        'event_two': 'xkcd:green',
        'event_three': (255/255, 0/255, 255/255), # rgb
        'event_four': 'c'
    }
    draw_colour_calendar(my_data, colour_map, date_colour='#f64b00')

.. image:: /_static/ex2.png
  :width: 400
  :alt: Example 2 image