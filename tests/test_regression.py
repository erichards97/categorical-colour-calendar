import importlib.resources as resources
from pathlib import Path
from tempfile import TemporaryDirectory

import matplotlib.pyplot as plt
import matplotlib.testing.compare as compare
import pandas as pd

from cccalendar import draw_colour_calendar


# @image_comparison(baseline_images=['line_dashes'], extensions=['png'], savefig_kwarg={'bbox_inches': 'tight'})
def test_simple_calendar():
    s = pd.Series({'2021-01-01': 'a'})
    cm = {'a': 'r'}
    draw_colour_calendar(s, cm)
    with TemporaryDirectory() as tmpdir:
        actual = Path(tmpdir) / "simple.png"
        plt.savefig(actual, bbox_inches='tight')

        expectation_image = resources.files(__package__) / "baseline_images" / "test_regression" / "simple.png"
        compare.compare_images(expectation_image, actual, tol=0)
