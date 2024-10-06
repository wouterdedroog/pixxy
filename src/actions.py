import ir
import pixmob_ir_protocol as pmir
from machine import Pin, ADC

speed = 0.4
selected_colour = [255, 255, 255]

dial_red = ADC(Pin(26))
dial_green = ADC(Pin(27))
dial_blue = ADC(Pin(28))


def colour(red, green, blue):
    global selected_colour
    selected_colour = [red, green, blue]


def current_colour():
    if selected_colour[0] is None:
        dial_red_value = dial_red.read_u16() / 65535
        dial_green_value = dial_green.read_u16() / 65535
        dial_blue_value = dial_blue.read_u16() / 65535
        return [int(255 * dial_red_value), int(255 * dial_green_value), int(255 * dial_blue_value)]
    return selected_colour


def current_speeds():
    # divide current speed pot in 4 parts and base attack/sustain speeds on that
    # when repeating, time between commands is 100-1000ms.
    # 0/3: 100-325ms
    # 1/3 = 325-550ms
    # 2/3 = 550-775ms
    # 3/3 = 775-1000ms
    attack_speeds = [pmir.Time.TIME_32_MS, pmir.Time.TIME_96_MS, pmir.Time.TIME_192_MS, pmir.Time.TIME_192_MS]
    sustain_speeds = [pmir.Time.TIME_96_MS, pmir.Time.TIME_192_MS, pmir.Time.TIME_192_MS, pmir.Time.TIME_480_MS]
    current_speed = int(speed * 3)
    return {
        'attack_release': attack_speeds[current_speed],
        'sustain': sustain_speeds[current_speed],
    }


def colour_fade(ir_led):
    fade_command = pmir.CommandSingleColorExt(
        red=current_colour()[0], green=current_colour()[1], blue=current_colour()[2],
        attack=current_speeds()["attack_release"],
        sustain=current_speeds()["sustain"],
        release=current_speeds()["attack_release"],
    )
    ir.send_bits_command(fade_command.encode(), ir_led)


def colour_flash(ir_led):
    flash_command = pmir.CommandSingleColorExt(
        red=current_colour()[0], green=current_colour()[1], blue=current_colour()[2],
        attack=pmir.Time.TIME_0_MS,
        sustain=current_speeds()["sustain"],
        release=pmir.Time.TIME_32_MS,
    )
    ir.send_bits_command(flash_command.encode(), ir_led)


def set_speed():
    global speed
    speed = dial_blue.read_u16() / 65535  # blue pot is used for setting speed


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
