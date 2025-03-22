import log_helper_functions
log_file = open('logs.txt', 'r')

WARNING = "WARNING"

count_of_warnings = 0
line_numbers = []

list_of_logs = log_file.readlines()

for each_line in list_of_logs:
    #If you want to look for a word inside a longer string, use this:
    if WARNING in each_line:
        count_of_warnings += 1
log_file.close()

log_file = open('logs.txt', 'r')
list_of_logs = log_file.readlines()

for index in range(len(list_of_logs)):
    if WARNING in list_of_logs[index]:
        line_numbers.append(index + 1)

print(f'Count of WARNINGS found: {count_of_warnings}')
#Call/Invoke log_helper, subtract 1
#Small example of getting the import to work with a random line:
# print(log_helper_functions.get_log_line_from_line_number(1))

#line numbers = [2,4]
for line_number in line_numbers:
    print(log_helper_functions.get_log_line_from_line_number(line_number))

print(f'These are the lines, WARNING was found: {line_numbers}')