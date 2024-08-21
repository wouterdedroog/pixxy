import ir
import pixmob_ir_protocol as pmir
from picozero import Pot

selected_colour = [255, 255, 255]


def colour(red, green, blue):
    global selected_colour
    selected_colour = [red, green, blue]


def current_colour():
    if selected_colour[0] is None:
        dial_red = Pot(0)
        dial_green = Pot(1)
        dial_blue = Pot(2)
        return [int(255 * dial_red.value), int(255 * dial_green.value), int(255 * dial_blue.value)]
    return selected_colour


def colour_fade(ir_led):
    fade_command = pmir.CommandSingleColorExt(
        red=current_colour()[0], green=current_colour()[1], blue=current_colour()[2],
        attack=pmir.Time.TIME_192_MS,
        sustain=pmir.Time.TIME_480_MS,
        release=pmir.Time.TIME_192_MS,
    )
    ir.send_bits_command(fade_command.encode(), ir_led)


def colour_flash(ir_led):
    flash_command = pmir.CommandSingleColorExt(
        red=current_colour()[0], green=current_colour()[1], blue=current_colour()[2],
        attack=pmir.Time.TIME_0_MS,
        sustain=pmir.Time.TIME_480_MS,
        release=pmir.Time.TIME_32_MS,
    )
    ir.send_bits_command(flash_command.encode(), ir_led)


def on(ir_led):
    commands = [
        pmir.CommandSetColor(red=current_colour()[0], green=current_colour()[1], blue=current_colour()[2], profile_id=0, skip_display=True),
        pmir.CommandSetConfig(
            on_start=True, gst_enable=True,
            profile_id_lo=0, profile_id_hi=0, is_random=False,
            attack=pmir.Time.TIME_960_MS,
            sustain=pmir.Time.TIME_960_MS,
            release=pmir.Time.TIME_0_MS
        ),
    ]
    ir.send_multiple_commands(commands, ir_led)


def off(ir_led):
    flash_command = pmir.CommandSingleColorExt(
        red=0x0, green=0x0, blue=0x0,
        attack=pmir.Time.TIME_0_MS,
        sustain=pmir.Time.TIME_0_MS,
        release=pmir.Time.TIME_0_MS,
    )
    ir.send_bits_command(flash_command.encode(), ir_led)


def rainbow_effect(ir_led):
    commands = [
        pmir.CommandSetColor(red=0xC0, green=0x64, blue=0x64, profile_id=0, skip_display=True),
        pmir.CommandSetColor(red=0xFF, green=0x00, blue=0x00, profile_id=1, skip_display=True),
        pmir.CommandSetColor(red=0xFF, green=0x6E, blue=0x00, profile_id=2, skip_display=True),
        pmir.CommandSetColor(red=0xFF, green=0xFF, blue=0x00, profile_id=3, skip_display=True),
        pmir.CommandSetColor(red=0x1E, green=0xB4, blue=0x1E, profile_id=4, skip_display=True),
        pmir.CommandSetColor(red=0x00, green=0xD2, blue=0xFF, profile_id=5, skip_display=True),
        pmir.CommandSetColor(red=0x37, green=0x47, blue=0xC8, profile_id=6, skip_display=True),

        pmir.CommandSetConfig(
            on_start=True, gst_enable=True,
            profile_id_lo=0, profile_id_hi=6, is_random=False,
            attack=pmir.Time.TIME_480_MS,
            sustain=pmir.Time.TIME_480_MS,
            release=pmir.Time.TIME_480_MS
        ),
    ]

    ir.send_multiple_commands(commands, ir_led)


def taylor_go_home(ir_led):
    commands = [
        pmir.CommandSetColor(red=0xC0, green=0x64, blue=0x64, profile_id=0, skip_display=True),
        pmir.CommandSetColor(red=0x98, green=0xC0, blue=0x30, profile_id=1, skip_display=True),
        pmir.CommandSetColor(red=0x64, green=0xC0, blue=0xC0, profile_id=2, skip_display=True),
        pmir.CommandSetColor(red=0x7C, green=0xC0, blue=0xC0, profile_id=3, skip_display=True),
        pmir.CommandSetColor(red=0x18, green=0xC0, blue=0x18, profile_id=4, skip_display=True),
        pmir.CommandSetColor(red=0xC0, green=0x64, blue=0xC0, profile_id=5, skip_display=True),
        pmir.CommandSetColor(red=0x00, green=0x28, blue=0xC0, profile_id=6, skip_display=True),
        pmir.CommandSetColor(red=0x38, green=0x38, blue=0x38, profile_id=7, skip_display=True),

        pmir.CommandSetConfig(
            on_start=True, gst_enable=True,
            profile_id_lo=0, profile_id_hi=7, is_random=True,
            attack=pmir.Time.TIME_480_MS,
            sustain=pmir.Time.TIME_480_MS,
            release=pmir.Time.TIME_480_MS
        ),
    ]

    ir.send_multiple_commands(commands, ir_led)
