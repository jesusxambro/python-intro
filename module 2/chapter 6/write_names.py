def main():
    print("Enter names of 3 friends:")
    name1 = input("Friend #1:")
    name2 = input("Friend #2:")
    name3 = input("Friend #3:")

    my_file = open("friends.txt", "w")
    my_file.write(name1 + '\n')
    my_file.write(name2 + '\n')
    my_file.write(name3 + '\n')

    my_file.close()
    print("Names written to File")

if __name__ == '__main__':
    main()