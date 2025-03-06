def multiple_returns():
    return 1, "Hello World"


number_to_print, string_to_show = multiple_returns()

print(number_to_print)
print(string_to_show)