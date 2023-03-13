########################################
####            GLOBALS
########################################
# packages
import math

# variables
ROUNDS = 10000
MONKEY_BUSINESS = 0
MONKEYS = []
MONKEY_DICT = {}


########################################
####            CLASSES
########################################
class monkey:

    def __init__(self, name):
        self.name = name
        self.items = []
        self.operator = []
        self.op_first_num = 0
        self.op_second_num = 0
        self.times_inspected = 0
        self.test_num = 0
        self.true_monkey = ""
        self.false_monkey = ""

    def get_times_inspected(self):
        return self.times_inspected

    def add_item(self, item):
        self.items.append(item)

        return self.items

    def set_operation(self, operator, op_first_num, op_second_num):
        self.operator = operator
        self.op_first_num = int(op_first_num) if op_first_num != "old" else "old"
        self.op_second_num = int(op_second_num) if op_second_num != "old" else "old"

    def set_test_num(self, test_num):
        self.test_num = test_num

        return test_num

    def set_true_monkey(self, true_monkey):
        self.true_monkey = true_monkey

        return self.true_monkey

    def set_false_monkey(self, false_monkey):
        self.false_monkey = false_monkey

        return self.false_monkey

    def print_info(self, print_all = False):
        item_levels = [x.get_worry_level() for x in self.items]
        if print_all == True:
            print("Monkey {}".format(self.name))
            print("-------------------------")
            print("Items: ")
            for i in self.items:
                print("   - {}".format(i.get_worry_level()))
            print("Operator:         {}".format(self.operator))
            print("op first number:  {}".format(self.op_first_num))
            print("op second number: {}".format(self.op_second_num))
            print("test num:         {}".format(self.test_num))
            print("true monkey:      {}".format(self.true_monkey))
            print("false monkey:     {}".format(self.false_monkey))
            print("--------------------------------------------")
        else:
            print("Monkey: {}".format(self.name))
            print("-------------------")
            print("items inspected: {}".format(self.times_inspected))
            print("items: {}".format(item_levels))
            print("----------------------------------------")

    
    def inspect_item(self, item):
        num1 = item.get_worry_level() if self.op_first_num == "old" else self.op_first_num
        num2 = item.get_worry_level() if self.op_second_num == "old" else self.op_second_num

        # monkey inspects item and gets the new worry level
        new_num = 0
        if self.operator == "+":
            new_num = num1 + num2
        elif self.operator == "-":
            new_num = num1 - num2
        elif self.operator == "*":
            new_num = num1 * num2
        else:
            new_num = float(num1) / num2

        # monkey get's bored and worry level is divided by 3
        new_num = int(math.floor(new_num))

        # print("old: {} -> new: {}".format(item.get_worry_level(), new_num))

        item.change_worry_level(new_num)

    def test_item(self, item):
        result = True if item.get_worry_level() % self.test_num == 0 else False
        return result

    def throw_item(self, result, item):
        recipient_monkey = self.true_monkey if result == True else self.false_monkey

        MONKEY_DICT[recipient_monkey].add_item(item)

    def perform_round(self):
        num_items = len(self.items)
        for i in range(num_items):
            self.times_inspected += 1
            item = self.items.pop(0)
            self.inspect_item(item)
            result = self.test_item(item)
            self.throw_item(result, item)


class item:

    def __init__(self, worry_level):
        self.worry_level = worry_level

    def get_worry_level(self):
        return self.worry_level

    def change_worry_level(self, number):
        self.worry_level = number

        return self.worry_level

########################################
####            functions
########################################
def do_round():
    for a in MONKEYS:
        a.perform_round()

def print_results():
    for a in MONKEYS:
        a.print_info()

def check_monkey_business():
    times_inspected = []
    for a in MONKEYS:
        times_inspected.append(a.get_times_inspected())
    
    times_inspected.sort(reverse = True)

    monkey_business = times_inspected[0] * times_inspected[1]

    return monkey_business

########################################
####            MAIN
########################################
# reading in data
with open(".\input_test.txt", "r") as f:
    for line in f:
        if line == "\n":
            continue

        words = line.replace("\n", "").split()

        # going through each line
        if words[0] == "Monkey":
            new_monkey = monkey(words[1].replace(":", ""))
            MONKEYS.append(new_monkey)
            MONKEY_DICT[words[1].replace(":","")] = new_monkey

        elif words[0] == "Starting":
            length = len(words)
            for i in range(length - 2):
                worry_level = int(words[length - i - 1].replace(",", ""))
                new_item = item(worry_level)
                MONKEYS[-1].add_item(new_item)
                
        elif words[0] == "Operation:":
            op_first_num = words[3]
            operator = words[4]
            op_second_num = words[5]
            MONKEYS[-1].set_operation(operator, op_first_num, op_second_num)

        elif words[0] == "Test:":
            test_num = int(words[-1])
            MONKEYS[-1].set_test_num(test_num)

        elif words[1] == "true:":
            MONKEYS[-1].set_true_monkey(words[-1])
        
        elif words[1] == "false:":
            MONKEYS[-1].set_false_monkey(words[-1])


for i in range(ROUNDS):
    do_round()
    print("Round {}".format(i + 1))
    print("-------------------------------------------------------")
    # print_results()

print(check_monkey_business())
