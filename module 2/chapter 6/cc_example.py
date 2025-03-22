# https://runestone.academy/ns/books/published/thinkcspy/Files/Iteratingoverlinesinafile.html

ccfile = open("ccdata.txt", "r")

for aline in ccfile:
    values = aline.split()
    #values = ["1850","-1.2","1.554"]
    if values[0] == "2000":
        print('In', values[0], 'the average temp. was', values[1], '°C and CO2 emmisions were', values[2], 'gigatons.')

ccfile.close()