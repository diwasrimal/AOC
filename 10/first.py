from tools import data


cycle = 1
x = 1
total_strength = 0

for line in data:

    # Check if we reached important cycle
    if cycle % 40 == 20: 
        total_strength += cycle * x

    # 'noop' takes 1 cycle to complete
    if line == "noop":
        cycle += 1

    # 'addx V' will take 2 cycles to complete
    else:
        cycle += 1
        # Check if we reached important cycle
        if cycle % 40 == 20: 
            total_strength += cycle * x
        cycle += 1

        # Value only added after 2 cycles are complete
        x += int(line.split()[1])

print(total_strength)
