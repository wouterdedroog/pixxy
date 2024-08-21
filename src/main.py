from machine import Pin, PWM

import inputs
import ir
import select
import sys

poll_obj = select.poll()
poll_obj.register(sys.stdin, select.POLLIN)

ir_pin = Pin(16, Pin.OUT)
ir_led = PWM(ir_pin)
ir_led.freq(38000)


def read_until(until_char, keep_result=True):
    result = ''
    while True:
        char = sys.stdin.read(1)
        if char == until_char:
            break

        if keep_result:
            result += char
    return result

# todo: implement once / repeat switch
# button = Pin(2, Pin.IN, Pin.PULL_UP)


def run():
    try:
        while True:
            poll_results = poll_obj.poll(100)
            if poll_results:
                read_until(']', False)
                command = read_until(',')
                ir.send_raw_ir_command(command, ir_led)

            inputs.check(ir_led)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print('Restarting due to exception:')
        import sys
        sys.print_exception(e)
        run()  # restart on failure


if __name__ == '__main__':
    run()


