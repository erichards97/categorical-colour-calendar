# Categorical Colour Calendar
Highlighting dates on a monthly calendar from categorical events
## Setup
```
python -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip
pip install -r requirements.txt
```
## Usage
```python
import pandas as pd
from cccalendar import draw_colour_calendar

dates = pd.date_range(start='2021-01-01', end='2021-05-01')
df = pd.Series(np.arange(len(dates)), index=dates)
draw_colour_calendar(df, {})
```