import time
import math
from functools import reduce
start_time = time.time()

D = {}

with open('8.txt', 'r') as file:
    first_line = file.readline().strip()

    file.readline()

    for line in file:
        key, rest = map(str.strip, line.split('='))

        values = [value.strip("() ") for value in rest.split(',')]

        D[key] = list(values)

steps = len(first_line)
A = list(key for key in D.keys() if key[2] == "A")
Z = list(key for key in D.keys() if key[2] == "Z")
print(A)
print(Z)
steps_required = []


for a in A:
    J = {}
    step = 0
    X = False
    c=a
    while X == False:
        
        parsed_step = step%steps
        if first_line[parsed_step]=='L':
            c=D[c][0]
        else:
            c=D[c][1]
        print(f"{step} : {J}:{c}")
        if c[-1]=="Z":
            if c not in J:
                J[c] = {parsed_step: step+1}
            else:
                if parsed_step not in J[c]:
                    J[c][parsed_step] = step+1
                else:
                    steps_required.append([J[c][parsed_step], step+1])
                    X = True
        step += 1


print(steps_required)
import math
from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_of_list(numbers):
    return reduce(lcm, numbers)


# Example usage:
my_list = [x[0] for x in steps_required]

result = lcm_of_list(my_list)
print(f"minimum steps is {result}")
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)
