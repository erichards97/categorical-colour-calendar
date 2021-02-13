##############################################
Introduction
##############################################


.. topic:: Overview

    This page describes the purpose of the Categorical Colour Calendar library.

    :Date: 2021-02-13
    :Author: **Edward Richards**

Categorical Colour Calendar allows you to plot monthly calendars, and highlight dates based on discrete events.

It was created as existing solutions for plotting calendars generated heatmaps for continuous data (e.g. calmap, calplot).

These other solutions also produced calendars per year (in the style of GitHub contributions chart), rather than a more familiar monthly calendar.

It has been designed to be customizable, with a range of optional parameters controlling the behaviour and style of the resultant plot.

The library can be used in a few different ways. The most simple is to just provide a Series of events, and the event-colour mapping will be automatically generated.
Alternatively you can explicitly provide a dictionary mapping your events to the desired colour.
Extending on this, you could provide a Series with daily values and a corresponding colour map, giving you full control over the colour of each date on the calendar.

Categorical Colour Calendar uses Matplotlib to produce graphics but is otherwise built from the ground up.
This includes the calendar visualisations, which are drawn as polygons on axes.

.. image:: /examples/colourful.png
  :width: 768
  :alt: Sample image with alternately coloured dates