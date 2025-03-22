word_count ={}

lorem_file = open("lorem.txt", "r")

for line in lorem_file:
    words = line.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

lorem_file.close()

print("Word Counts")

for word, count in word_count.items():
    print(f"{word}: {count}")