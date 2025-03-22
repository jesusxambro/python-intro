#reading
states_file = open("states.txt", "r")

example_dictionary = {
    "Texas": "The biggest state!"
}

#Void function example
def print_fun_fact(state):
    if state == "Texas":
        print("We got boots!")

#Value Returning
def print_cool_fact(state):
    if state == "Oregon":
        return "Twilight was filmed here!"
    else:
        return ""

for line in states_file:
    line = line.strip()
    cool_fact = print_cool_fact(line)
    if len(cool_fact) > 0:
        print(cool_fact)
    # print_fun_fact(line)
    # if line == "Texas":
    #     print(example_dictionary["Texas"])

states_file.close()
