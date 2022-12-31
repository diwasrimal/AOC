from tools import monkeys


# Common divider to handle huge integer values of worry_level
common_divider = 1
for monkey in monkeys:
    common_divider *= monkey['divider']

# Run ten thousand rounds
for i in range(10000):
    for key, monkey in enumerate(monkeys):
        while True:

            # Turn ends if monkey doesnot have any item
            if not monkey['items']: 
                break

            # Monkey inspects an item
            monkey['item_inspects'] += 1

            # Make a variable 'item' to evaluate the string 'monkey['operation']'
            item = monkey['items'][0]
            worry_level = eval(monkey['operation']) % common_divider

            # Throw the item to another monkey
            if worry_level % monkey['divider'] == 0:
                receiver = monkey['receivers'][0] 
            else:
                receiver = monkey['receivers'][1]
            monkey['items'].pop(0)
            monkeys[receiver]['items'].append(worry_level)


# Find monkey business by finding the two highest inspects
inspects = sorted([ monkey['item_inspects'] for monkey in monkeys ], reverse=True)
monkey_business = inspects[0] * inspects[1]
print(monkey_business)
