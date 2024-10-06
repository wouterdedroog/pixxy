import actions as a
from machine import Pin
from time import sleep


action_matrix = [
    [lambda _: a.colour(0xFF, 0x00, 0x00), lambda _: a.colour(0x00, 0xFF, 0x00), lambda _: a.colour(0x00, 0x00, 0xFF), lambda ir: a.colour_fade(ir)],
    [lambda _: a.colour(0xFF, 0xA5, 0x00), lambda _: a.colour(0x4A, 0xC1, 0xDB), lambda _: a.colour(0xFF, 0xFF, 0x00), lambda ir: a.colour_flash(ir)],
    [lambda _: a.colour(0xFF, 0x00, 0x74), lambda _: a.colour(0xFF, 0xFF, 0xFF), lambda _: a.colour(None, None, None), lambda ir: a.on(ir)],
    [lambda ir: a.rainbow_effect(ir), lambda ir: a.taylor_go_home(ir), lambda _: a.set_speed(), lambda ir: a.off(ir)],
]

rows = [Pin(9, Pin.IN, Pin.PULL_UP), Pin(8, Pin.IN, Pin.PULL_UP), Pin(7, Pin.IN, Pin.PULL_UP), Pin(6, Pin.IN, Pin.PULL_UP)]
cols = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(11, Pin.OUT), Pin(10, Pin.OUT)]


repeat_switch = Pin(2, Pin.IN, Pin.PULL_UP)
repeat_action_index = None


def check(ir_led):
    global repeat_action_index
    for col in range(len(cols)):
        col_pin = cols[col]
        col_pin.value(0)
        for row in range(len(rows)):
            row_pin = rows[row]
            if not row_pin.value():
                action_matrix[row][col](ir_led)  # Call action for button at position x,y

                if col == 3 and (row == 0 or row == 1):
                    repeat_action_index = {"row": row, "col": col}
                if col == 3 and row == 3:
                    repeat_action_index = None

        col_pin.value(1)

    if repeat_switch.value() == 1 and repeat_action_index is not None:
        row = repeat_action_index["row"]
        col = repeat_action_index["col"]
        action_matrix[row][col](ir_led)
        sleep(0.1 + a.speed * 0.9)
    else:
        repeat_action_index = None
        sleep(0.1)
