def show_sum(a, b, c, d):
    print(a + b + c + d)


def show_sum_positional_keyword(a, b, /, c, d):
    print(a + b + c + d)

def main():
    show_sum(1,2, c=3, d=4)
    show_sum_positional_keyword(1,2,c=3,d=4)



main()