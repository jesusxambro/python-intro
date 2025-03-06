def show_tax(price, tax=0.07):
    total = price * tax
    return total


def show_tax_invalid(price=10, tax_rate):
    tax = price * tax_rate
    print(f'The tax is {tax}.')

def main():
    price_of_computer = 1200
    # total_price = show_tax(price_of_computer)
    # print(total_price)
    total_tax = show_tax(price_of_computer, 0.2)
    print(total_tax)



main()

