import matplotlib.pyplot as plt

number_of_favorite_candy = [3,5,3,8]
label_candies = ["Kitkat", "Snickers", "Almond Joy","Reese's Pieces"]

plt.pie(x=number_of_favorite_candy, labels=label_candies, colors=("b","g","r","c"))

plt.show()