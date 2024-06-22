# This is a sample Python script.
from backpropagation_modern import SoftmaxBackPropagation
import matplotlib.pyplot as plt




# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

training_set = [
    ([0.0, 0.5, 0.5, 0.0, 0.0], [0.0, 0.0, 1.0]),
    ([1.0, 1.0, 1.0, 1.0, 0.0], [0.0, 1.0, 0.0]),
    ([0.5, 1.0, 0.0, 1.0, 1.0], [1.0, 0.0, 0.0]),
    ([0.0, 0.5, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0]),
    ([1.0, 0.5, 1.0, 0.5, 0.0], [0.0, 1.0, 0.0]),
    ([1.0, 1.0, 0.0, 0.5, 0.5], [1.0, 0.0, 0.0])
 ]

net_input = [0.5, 1.0, 0.0, 1.0, 1.0]


def run_backpropagation():

    # Use a breakpoint in the code line below to debug your script.
    bpnn = SoftmaxBackPropagation(training_set, [5, 10, 10, 3], [0.01], 1000)
    bpnn.backpropagation()
    output = bpnn.run(net_input)
    print("Result is: ", output)
    print("Cross Entropy Loss: ", bpnn.cross_entropy_loss())
    bpnn.plot_activations()
    


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_backpropagation()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
