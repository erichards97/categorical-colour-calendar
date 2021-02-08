from matplotlib.colors import hsv_to_rgb


def get_n_colours(n, s=0.5, v=0.95):
    return [hsv_to_rgb((i/n, s, v)) for i in range(n)]


def populate_colour_map(data, colour_map):
    values = data.unique()
    missing_values = [x for x in values if x not in colour_map]
    new_colours = get_n_colours(len(missing_values))
    new_colours_map = {x[0]: x[1] for x in zip(missing_values, new_colours)}
    return {**colour_map, **new_colours_map}
