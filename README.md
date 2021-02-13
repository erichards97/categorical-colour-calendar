# Categorical Colour Calendar
Library for drawing monthly calendars and highlighting dates from categorical events
## Example
![Example](https://raw.githubusercontent.com/erichards97/categorical-colour-calendar/main/docs/source/examples/img.png "Optional Title")
For more examples see the docs
## Setup
```
pip install categorical-colour-calendar
```
## Usage
```python
import pandas as pd
from cccalendar import draw_colour_calendar
my_data = pd.Series({
    '2021-01-01': 'event_one',
    '2021-01-07': 'event_two',
    '2021-01-10': 'event_three',
    '2021-01-14': 'event_four',
    '2021-01-20': 'event_one',
    '2021-01-21': 'event_two',
})
draw_colour_calendar(my_data)
```
## Development
```
pip install -e .[dev]
```

## To Do
- Check DataFrame/Series compatibility
- Multiple events on one day
- Tests
- Allow override of default sizing/scaling values
- Test different Python versions
- Return fig/axes
- Docs (wip)
- Heatmap mode
- Annual calendar mode
- Consolidate readme and docs
- CI
- Badges