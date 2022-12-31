import re


monkeys = []

with open("input.txt") as file:
    monkey_data = file.read().split('\n\n')
    for data in monkey_data:
        if not data: continue
        lines = data.splitlines()
        monkey = {
            'items': list(map(int, re.findall(r'(\d+)', lines[1]))),
            'operation': lines[2].split('= ')[1].replace('old', 'item'),
            'divider': int(lines[3].split()[-1]),
            'receivers': (int(lines[4].split()[-1]), int(lines[5].split()[-1])),
            'item_inspects': 0,
        }
        monkeys.append(monkey)
