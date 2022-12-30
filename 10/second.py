from tools import Crt, data


# Initialize the CRT
crt = Crt(40, 6)

cycle = 1
x = 1

for line in data:

    # Update crt's screen on each cycle
    crt.update(cycle, x)

    # 'noop' takes 1 cycle to complete
    if line == "noop":
        cycle += 1

    # 'addx V' will take 2 cycles to complete
    else:
        cycle += 1
        crt.update(cycle, x)

        cycle += 1
        # Value only added after 2 cycles are complete
        x += int(line.split()[1])

crt.print()
