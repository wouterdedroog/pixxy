from utime import sleep_us


def group_by(iterable):
    result = []
    current_group = []
    current_value = None

    for item in iterable:
        if current_value is None or item != current_value:
            if current_group:
                result.append((current_value, current_group))
            current_group = [item]
            current_value = item
        else:
            current_group.append(item)

    if current_group:
        result.append((current_value, current_group))

    return result


# taken from https://github.com/danielweidman/pixmob-ir-reverse-engineering/
def bits_to_run_lengths_pulses(bit_list):
    # convert from a list of 1s and 0s to run length by number of pulses
    # Example: [1, 1, 1, 0, 0, 0, 0, 1] -> [3, 4, 1]
    run_lengths = []
    # group_by returns groups of adjacent matching things
    for _, group in group_by(bit_list):
        run_lengths.append(sum(1 for _ in group))
    return run_lengths


# taken from https://github.com/danielweidman/pixmob-ir-reverse-engineering/
def bits_to_arduino_string(bit_list):
    run_lengths = bits_to_run_lengths_pulses(bit_list)
    if max(run_lengths) > 9:
        raise ValueError(f"Arduino can't accept over 9 of the same bit in a row.\n{bit_list}")
    out = "".join([str(int(i)) for i in run_lengths])
    return out


def send_multiple_commands(command_list, ir_pin):
    for command in command_list:
        send_bits_command(command.encode(), ir_pin)


def send_bits_command(bit_list, ir_pin):
    command = bits_to_arduino_string(bit_list)
    send_raw_ir_command(command, ir_pin)


def send_raw_ir_command(command, ir_pin):
    for i in range(len(command)):
        duration = int(command[i]) * 700
        if i % 2 == 0:
            ir_pin.duty_u16(32768)  # 50% duty cycle
        else:  # Odd index (space)
            ir_pin.duty_u16(0)
        sleep_us(duration)
    ir_pin.deinit()
