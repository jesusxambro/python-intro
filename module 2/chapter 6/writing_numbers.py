writing_numbers_example = open("number_example.txt", "w")

past_quarter_sales_data = 120000
convert_sales_data = str(past_quarter_sales_data)

writing_numbers_example.write(convert_sales_data)

writing_numbers_example.close()