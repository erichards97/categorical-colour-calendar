import calendar
from datetime import datetime

import matplotlib.pyplot as plt

scale = 20

def num_to_day(num):
    return (num-(scale/4)) / scale

def day_to_num(day):
    return (day * scale) + (scale/4)

def get_square_coordinates(day_of_week, week_of_month):
    x_start = scale * day_of_week
    x_end = (scale * day_of_week) + (scale / 2)
    y_start = scale * week_of_month
    y_end = (scale * week_of_month) + (scale / 2)

    bottom_left = (x_start, y_start)
    top_left = (x_start, y_end)
    top_right = (x_end, y_end)
    bottom_right = (x_end, y_start)

    centre = (((x_start + x_end) / 2), ((y_start + y_end) / 2))

    return [bottom_left, top_left, top_right, bottom_right], centre


def draw_date_square(date, data, colour_map, ax):
    day_of_week = date.weekday()
    first_day_weekday = date.replace(day=1).weekday()
    week_of_month = int((first_day_weekday-1 + date.day) / 7)

    corners, centre = get_square_coordinates(day_of_week, week_of_month)

    colour = 'm'
    if date in data.index and data[date] in colour_map:
        colour = colour_map[data[date]]

    shape = plt.Polygon(corners, color=colour)
    ax.add_patch(shape)
    ax.annotate(str(date.day), centre, color='w', weight='bold', fontsize=scale/2, ha='center', va='center')

def draw_calendar_for_month(data, colour_map, year, month, ax):
    month_start_day, month_num_days = calendar.monthrange(year, month)
    for day in range(1, month_num_days+1):
        current_date = datetime(year, month, day)
        draw_date_square(current_date, data, colour_map, ax)

    secax = ax.secondary_xaxis('top', functions=(num_to_day, day_to_num))
    secax.set_xticks(range(7))
    secax.set_xticklabels(['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'])
    ax.axis('scaled')
    ax.set_title(calendar.month_name[month] + ' ' + str(year), pad=20)
    ax.axis('off')
    ax.plot()

def count_months(start_month, start_year, end_month, end_year):
    full_years = (end_year - start_year) - 1
    months_in_start_year = 13 - start_month
    return months_in_start_year + (full_years * 12) + end_month

def draw_colour_calendar(data, colour_map, months_per_row=3):
    first_date = data.index.min()
    last_date = data.index.max()

    num_months = count_months(first_date.month, first_date.year, last_date.month, last_date.year)

    fig, axs = plt.subplots(int(num_months/months_per_row)+1, months_per_row, sharex=True, sharey=True, squeeze=False)

    total_axs = len(axs) * len(axs[0])  # could use months_per_row
    unused_axs = total_axs - num_months
    for u in range(unused_axs):
        axs[len(axs)-1][(months_per_row-1)-u].remove()

    month_counter = 0
    for year in range(first_date.year, last_date.year + 1):
        start_month = 1
        end_month = 12
        if year == first_date.year:
            start_month = first_date.month
        if year == last_date.year:
            end_month = last_date.month

        for month in range(start_month, end_month+1):
            axs_x = int(month_counter / months_per_row)
            axs_y = month_counter % months_per_row
            draw_calendar_for_month(data, colour_map, year, month, axs[axs_x][axs_y])
            month_counter = month_counter + 1

    axs[0][0].invert_yaxis()

    fig.set_size_inches(25, 25)
    fig.set_dpi(300)
    fig.tight_layout()
    plt.subplots_adjust(wspace=0)

# dates = pd.date_range(start='2021-01-01', end='2021-05-01')
# df = pd.Series(np.arange(len(dates)), index=dates)
# draw_colour_calendar(df, {})