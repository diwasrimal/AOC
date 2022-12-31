from tools import monkeys


# Run twenty rounds
for i in range(20):
    for key, monkey in enumerate(monkeys):
        while True:

            # Turn ends after monkey finishes its items
            if not monkey['items']: 
                break

            # Monkey inspects an item
            monkey['item_inspects'] += 1

            # Make a variable 'item' to evaluate the string 'monkey['operation']'
            item = monkey['items'][0]
            worry_level = eval(monkey['operation']) // 3

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

