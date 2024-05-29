import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, data, title='Histogram', x_label='Values', y_label='Frequency'):
        self.data = data
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def plot(self):
        plt.hist(self.data, bins='auto')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(True)
        plt.show()
