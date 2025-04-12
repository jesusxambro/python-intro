import matplotlib.pyplot as plt
def main():

    x = [0, 1, 2, 3, 4]
    y = [0, 3, 1, 5, 2]

    plt.plot(x,y)
    plt.xticks(x,["2016","2017","2018","2019","2020"])
    plt.yticks([0, 1, 2, 3, 4, 5],['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    plt.title("Simple Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.autoscale(enable=False,axis="x")


    plt.show()

def second_chart():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    plt.plot(x_coords, y_coords)

    plt.show()

if __name__ == '__main__':
    main()
    # second_chart()