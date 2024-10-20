from libqtile import bar
from .widgets import primary_widgets, secondary_widgets

primaryBar = bar.Bar(
    primary_widgets,
    30,
    border_color='#282738',
    border_width=[0, 0, 0, 0],
    margin=[1, 1, 1, 1],
)

secondaryBar = bar.Bar(
    secondary_widgets,
    30,
    border_color='#282738',
    border_width=[0, 0, 0, 0],
    margin=[1, 1, 1, 1],
)
