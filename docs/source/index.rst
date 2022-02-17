Welcome to Categorical Colour Calendar's documentation!
=======================================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   pages/getting_started
   pages/functionality
   pages/reference
   pages/examples
   pages/development

Categorical Colour Calendar allows you to plot monthly calendars and highlight discrete data.

It was created as existing solutions for plotting calendars were tailored toward continuous data and thus produced heatmaps (calmap, calplot).

These other solutions also generated yearly calendar figures (in the style of GitHub contributions chart), rather than a more familiar monthly calendar.

The style of the resultant plot is fairly customizable through a range of parameters.

The library is flexible, in that you can simply provide a Series of events and the colour mapping will take place automatically.
Alternatively this colour mapping can be provided allowing you to determine the colour of each date, should you wish.

Categorical Colour Calendar uses Matplotlib for rendering.

.. image:: /_static/colourful.png
  :width: 800
  :alt: Sample calendar figure

*A colourful example*
