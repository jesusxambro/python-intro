
def get_log_line_from_line_number(line_to_return):
    log_file = open('logs.txt', 'r')
    list_of_logs = log_file.readlines()
    log_file.close()
    return list_of_logs[line_to_return - 1]
