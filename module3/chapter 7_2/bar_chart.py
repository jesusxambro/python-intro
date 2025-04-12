import matplotlib.pyplot as plt
average_height_of_plants_per_zone = [3,8,6,4.3]
zone_locations = ["A","B","C","D"]
bar_width = 0.5
plt.bar(zone_locations, average_height_of_plants_per_zone, bar_width, color=('r', 'g', 'b', 'k'))
plt.ylabel("average height")
plt.show()