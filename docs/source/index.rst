Welcome to Categorical Colour Calendar's documentation!
=======================================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   pages/getting_started
   pages/functionality
   pages/reference
   pages/examples

Categorical Colour Calendar allows you to plot monthly calendars and highlight dates based on discrete events.

It was created as existing solutions for plotting calendars assumed continuous data and produced heatmaps (e.g. calmap, calplot).

These other solutions also produced calendars per year (in the style of GitHub contributions chart), rather than a more familiar monthly calendar.

It has been designed to be customizable, with a range of optional parameters controlling the behaviour the resultant plot.

The library can be used in a few different ways:

* The most simple is to provide a Series of events and the event-colour mapping will be automatically generated.

* Alternatively you can explicitly provide a dictionary mapping your events to the desired colour.

* Lastly, you could provide a Series with daily values and a corresponding colour map, giving you full control over the colour of each date on the calendar.


There are further parameters controlling other aspects of the generated figure.

Categorical Colour Calendar uses Matplotlib to create visualisations and handle colours, but is otherwise built from the ground up.
This includes rendering the calendar visualisations, which are really a collection of spaced polygons on a secondary x-axis.

.. image:: /_static/colourful.png
  :width: 800
  :alt: Sample calendar figure

*A colourful example*
