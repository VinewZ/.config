from libqtile.config import Screen
from .bar import primaryBar, secondaryBar

screens = [
    Screen(
        top=primaryBar,
        # wallpaper="~/Wallpapers/wall.jpg",
        # wallpaper_mode="stretch",
    ),
    Screen(
        top=secondaryBar,
        # wallpaper="~/Wallpapers/wall.jpg",
        # wallpaper_mode="stretch"
    ),
]
