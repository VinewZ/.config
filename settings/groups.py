from libqtile.config import Key, Group, ScratchPad, DropDown
from libqtile.lazy import lazy
from .keys import mod, keys

# Define the groups
groups = [
    Group(i) for i in "123456789"
] + [
    ScratchPad("scratchpad", [
        DropDown("alacritty", "alacritty", width=0.4, x=0.3, y=0.2),
        DropDown("volume", "pavucontrol", width=0.4, x=0.3, y=0.2),
        DropDown("clip-history", "copyq show", width=0.4, x=0.3, y=0.2)
    ])
]

for i, group in enumerate(groups[:-1]):  # excluding the scratchpad group
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
