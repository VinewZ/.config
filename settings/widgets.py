from libqtile import widget, qtile


def workspaces():
    return [
        widget.GroupBox(
            fontsize=18,
            borderwidth=1,
            highlight_method='block',
            active='#CAA9E0',
            block_highlight_text_color="#91B1F0",
            highlight_color='#4B427E',
            inactive='#282738',
            foreground='#4B427E',
            background='#353446',
            this_current_screen_border='#353446',
            this_screen_border='#353446',
            other_current_screen_border='#353446',
            other_screen_border='#353446',
            urgent_border='#353446',
            rounded=True,
            disable_drag=True,
        ),
    ]


def search():
    qtile.cmd_spawn("rofi -show drun")


primary_widgets = [

    widget.Spacer(
        length=15,
        background='#282738',
    ),

    widget.Image(
        filename='~/.config/qtile/Assets/6.png',
    ),

    *workspaces(),

    widget.Spacer(
        length=8,
        background='#353446',
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/1.png',
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/layout.png',
        background="#353446"
    ),


    widget.CurrentLayout(
        background='#353446',
        foreground='#CAA9E0',
        fmt='{}',
        font="JetBrains Mono Bold",
        fontsize=13,
    ),


    widget.Spacer(
        length=220,
        background='#353446',
    ),

    widget.WindowName(
        background='#353446',
        format="{name}",
        font='JetBrains Mono Bold',
        foreground='#CAA9E0',
        empty_group_string='Desktop',
        fontsize=13,
    ),

    widget.Spacer(
        background='#353446',
    ),

    widget.Volume(
        font='JetBrainsMono Nerd Font',
        theme_path='~/.config/qtile/Assets/Volume/',
        emoji=True,
        fontsize=13,
        background='#353446',
    ),


    widget.Spacer(
        length=-5,
        background='#353446',
    ),


    widget.PulseVolume(
        font='JetBrains Mono Bold',
        background='#353446',
        foreground='#CAA9E0',
        fontsize=13,
        volume_app="pavucontrol",
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/2.png',
    ),


    widget.Spacer(
        length=8,
        background='#353446',
    ),


    widget.Systray(
        background='#353446',
    ),

    widget.Spacer(
        length=8,
        background='#353446',
    ),

    widget.Image(
        filename='~/.config/qtile/Assets/Misc/clock.png',
        background='#282738',
        margin_y=6,
        margin_x=5,
    ),

    widget.Clock(
        format='%I:%M %p - %d/%m',
        background='#282738',
        foreground='#CAA9E0',
        font="JetBrains Mono Bold",
        fontsize=13,
    ),

    widget.QuickExit(
        background='#282738',
        foreground='#CAA9E0',
        font="JetBrains Mono Bold",
        fontsize=13,
    ),

    widget.Spacer(
        length=18,
        background='#282738',
    ),
]

secondary_widgets = [
    widget.Spacer(
        length=15,
        background='#282738',
    ),

    widget.Image(
        filename='~/.config/qtile/Assets/6.png',
    ),

    *workspaces(),

    widget.Spacer(
        length=8,
        background='#353446',
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/1.png',
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/layout.png',
        background="#353446"
    ),


    widget.CurrentLayout(
        background='#353446',
        foreground='#CAA9E0',
        fmt='{}',
        font="JetBrains Mono Bold",
        fontsize=13,
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/5.png',
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/search.png',
        margin=2,
        background='#282738',
        mouse_callbacks={"Button1": search},
    ),

    widget.TextBox(
        fmt='Search',
        background='#282738',
        font="JetBrains Mono Bold",
        fontsize=13,
        foreground='#CAA9E0',
        mouse_callbacks={"Button1": search},
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/4.png',
    ),


    widget.Spacer(
        background='#353446',
    ),

    widget.WindowName(
        background='#353446',
        format="{name}",
        font='JetBrains Mono Bold',
        foreground='#CAA9E0',
        empty_group_string='Desktop',
        fontsize=13,
    ),

    widget.Spacer(
        background='#353446',
    ),

    widget.Net(
        format=' {up}   {down} ',
        background='#353446',
        foreground='#CAA9E0',
        font="JetBrains Mono Bold",
        prefix='k',
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/2.png',
    ),

    widget.Spacer(
        length=8,
        background='#353446',
    ),


    widget.Image(
        filename='~/.config/qtile/Assets/Misc/ram.png',
        background='#353446',
    ),

    widget.Memory(
        background='#353446',
        format='{MemUsed: .0f}{mm}',
        foreground='#CAA9E0',
        font="JetBrains Mono Bold",
        fontsize=13,
        update_interval=5,
    ),

    widget.Image(
        filename='~/.config/qtile/Assets/2.png',
    ),


    widget.Spacer(
        length=8,
        background='#353446',
    ),

    widget.Volume(
        font='JetBrainsMono Nerd Font',
        theme_path='~/.config/qtile/Assets/Volume/',
        emoji=True,
        fontsize=13,
        background='#353446',
    ),


    widget.Spacer(
        length=-5,
        background='#353446',
    ),


    widget.PulseVolume(
        font='JetBrains Mono Bold',
        background='#353446',
        foreground='#CAA9E0',
        fontsize=13,
        volume_app="pavucontrol",
        padding=10
    ),

    widget.Image(
        filename='~/.config/qtile/Assets/Misc/clock.png',
        background='#282738',
        margin_y=6,
        margin_x=5,
    ),

    widget.Clock(
        format='%I:%M %p - %d/%m',
        background='#282738',
        foreground='#CAA9E0',
        font="JetBrains Mono Bold",
        fontsize=13,
    ),


    widget.Spacer(
        length=18,
        background='#282738',
    ),
]

widget_defaults = {
    "font": "FiraCode Nerd Font Bold",
    "fontsize": 12,
    "padding": 3,

}

extension_defaults = widget_defaults.copy()
