import sys
import re
import queue

input_filename = sys.argv[1]
file = open(input_filename,'r')
lines = file.read().splitlines()
program_regex = re.compile(r'^(\w+) ([-\w]+)(?: ([-\w]+))?$')
listing = []

for line in lines:
    match = re.search(program_regex, line)
    listing.append(tuple(match.groups()))

numeric_regex = re.compile(r'^[-\d]+$')

class Program:

    def __init__(self, pid, listing):
        self.registers = {'p': pid}
        self.program_counter = 0
        self.message_queue = queue.Queue()
        self.subscribers = []
        self.waiting = False
        self.send_count = 0
        self.program_id = pid
        self.listing = listing

    def init_register(self, x):
        if x not in self.registers:
            self.registers[x] = 0

    def increment_program_counter(self):
        self.program_counter += 1

    def evaluate(self, x):
        if numeric_regex.match(x):
            return int(x)
        self.init_register(x)
        return self.registers[x]

    def send(self, x):
        val = self.evaluate(x)
        for subscriber in self.subscribers:
            subscriber.message_queue.put(val)
        self.send_count += 1
        self.increment_program_counter()

    def set_register(self, register, x):
        self.init_register(register)
        self.registers[register] = self.evaluate(x)
        self.increment_program_counter()

    def incr_register(self, register, x):
        self.init_register(register)
        self.registers[register] += self.evaluate(x)
        self.increment_program_counter()    

    def multiply_register(self, register, x):
        self.init_register(register)
        self.registers[register] *= self.evaluate(x)
        self.increment_program_counter()    

    def modulo_register(self, register, x):
        self.init_register(register)
        self.registers[register] = self.registers[register] % self.evaluate(x)
        self.increment_program_counter()    

    def receive(self, x):
        self.waiting = True
        try:
            val = self.message_queue.get(False)
        except queue.Empty:
            self.waiting = True
        else:
            self.waiting = False
            self.registers[x] = val
            self.increment_program_counter()

    def jump_if_greater_than(self, x, y):
        if self.evaluate(x) > 0:
            self.program_counter += self.evaluate(y)
        else:
            self.increment_program_counter()

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def finished(self):
        return self.program_counter >= len(self.listing)

    instructions = {
        'snd': send,
        'set': set_register,
        'add': incr_register,
        'mul': multiply_register,
        'mod': modulo_register,
        'rcv': receive,
        'jgz': jump_if_greater_than
    }

    def tick(self):
        if not self.finished():
            operation = self.listing[self.program_counter]
            if operation[2] == None:
                self.instructions[operation[0]](self, operation[1])
            else:
                self.instructions[operation[0]](self, operation[1], operation[2])

program1 = Program(0, listing)
program2 = Program(1, listing)
program1.add_subscriber(program2)
program2.add_subscriber(program1)
while not program1.finished() or not program2.finished():
    if program1.waiting and program2.waiting:
        break # terminate in case of deadlock
    else:
        program1.tick()
        program2.tick()

print('part 2: ', program2.send_count)