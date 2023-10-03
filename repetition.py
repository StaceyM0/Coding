



import random

numbers = list(range(0,5))

print(numbers)

for number in numbers: # iterate over list
    print(number*2)
    
for i in range(5): # do something fixed number of times
    print("This is from a for loop", str(i))
    
number = random.randint(0, 100)

counter = 0
while number != 52: # do until condition is false
    number = random.randint(0, 100)
    counter += 1
    
print(counter, number)
