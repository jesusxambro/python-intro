reading_file = open("marvel_heroes.txt", "r")

clean_data = reading_file.read()
clean_data = clean_data.rstrip("\t\n")
print(clean_data)
