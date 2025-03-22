loop_reading = open('loop_example.txt', 'r')

line = loop_reading.readline()
line = line.strip()
while line != '':
    print(line)
    line = loop_reading.readline()
loop_reading.close()

print("For Loop: ")

loop_reading = open('loop_example.txt', 'r')
heroes_string = loop_reading.readlines()

for each_line in heroes_string:
    print(each_line.rstrip())

loop_reading.close()