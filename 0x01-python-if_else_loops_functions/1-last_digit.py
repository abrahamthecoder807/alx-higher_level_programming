
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 10:
    last = last * -1
if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
elif last < 6 and last != 0:
    print("Last digit of {} is {} and is less than 6".format(number, last))
else:
    print("Last digit of {} is {} amd is 0".format(number, last))
