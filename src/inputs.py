import actions as a
from machine import Pin
from time import sleep


# todo: implement speed set button
action_matrix = [
    [lambda _: a.colour(0xFF, 0x00, 0x00), lambda _: a.colour(0x00, 0xFF, 0x00), lambda _: a.colour(0x00, 0x00, 0xFF), lambda ir: a.colour_fade(ir)],
    [lambda _: a.colour(0xFF, 0xA5, 0x00), lambda _: a.colour(0x4A, 0xC1, 0xDB), lambda _: a.colour(0xFF, 0xFF, 0x00), lambda ir: a.colour_flash(ir)],
    [lambda _: a.colour(0xFF, 0x00, 0x74), lambda _: a.colour(0xFF, 0xFF, 0xFF), lambda _: a.colour(None, None, None), lambda ir: a.on(ir)],
    [lambda ir: a.rainbow_effect(ir), lambda ir: a.taylor_go_home(ir), lambda _: None, lambda ir: a.off(ir)],
]

rows = [Pin(9, Pin.IN, Pin.PULL_UP), Pin(8, Pin.IN, Pin.PULL_UP), Pin(7, Pin.IN, Pin.PULL_UP), Pin(6, Pin.IN, Pin.PULL_UP)]
cols = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(11, Pin.OUT), Pin(10, Pin.OUT)]


def check(ir_led):
    for col in range(len(cols)):
        col_pin = cols[col]
        col_pin.value(0)
        for row in range(len(rows)):
            row_pin = rows[row]
            if not row_pin.value():
                action_matrix[row][col](ir_led)  # Call action for button at position x,y
                sleep(0.1)
        col_pin.value(1)
