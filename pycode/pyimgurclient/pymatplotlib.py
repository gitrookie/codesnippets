import matplotlib.pyplot as plt


def plot8():
    y = [ 3, 10, 7, 5, -3, 4.5, 6, 8.1]
    N = len( y )
    x = range( N )
    width = 1/1.5
    plt.bar(x, y, width, color="green")
    plt.show()
plot8()