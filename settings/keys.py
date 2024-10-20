from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "space", lazy.spawn("rofi -show drun")),

    # Browser
    ([mod], "b", lazy.spawn("zen-browser")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("wezterm")),

    # Screenshot
    ([mod, "shift"], "s", lazy.spawn("flameshot gui")),

    ([mod, "shift"], "c", lazy.spawn("xcolor -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    ([], "XF86AudioPlay", lazy.spawn(
        "playerctl play-pause"
    )),
    ([], "XF86AudioNext", lazy.spawn(
        "playerctl next"
    )),
    ([], "XF86AudioPrev", lazy.spawn(
        "playerctl previous"
    )),

    # Screen Brightness 
    ([], "XF86MonBrightnessUp", lazy.spawn(
        "brillo -A 5"
    )),
    ([], "XF86MonBrightnessDown", lazy.spawn(
        "brillo -U 5"
    )),
]]

# Add key bindings for scratchpad
keys.extend([
    # Toggle drop-down terminal
    Key([mod], 't', lazy.group['scratchpad'].dropdown_toggle('alacritty')),
    Key([mod], 'v', lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod], 'c', lazy.group['scratchpad'].dropdown_toggle('clip-history'))
])
