# This is a sample Python script.
from backpropagation import BackPropagation
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

def plot_activations(bpnn):
    _, (ax1, ax2) = plt.subplots(2, 1)
    x_input = range(len(bpnn.activations[0]))
    x_output = range(len(bpnn.activations[-1]))
    ax1.set_xticks(x_input)
    ax2.set_xticks(x_output)

    input_activations = bpnn.activations[0].flatten().tolist()
    output_activations = bpnn.activations[-1].flatten().tolist()
    input_neurons = range(len(input_activations))
    output_neurons = range(len(output_activations))

    ax1.bar(input_neurons, input_activations, label='Input Layer')
    ax1.set_xlabel('Neuron')
    ax1.set_ylabel('Activation')
    ax1.set_title('Input Layer Activations')

    ax2.bar(output_neurons, output_activations, label='Output Layer')
    ax2.set_xlabel('Neuron')
    ax2.set_ylabel('Activation')
    ax2.set_title('Output Layer Activations')

    plt.tight_layout()
    plt.show()


def run_backpropagation():

    # Use a breakpoint in the code line below to debug your script.
    bpnn = BackPropagation(training_set, [5, 10, 10, 3], [0.3, 0.1, 0.1], 1000)
    bpnn.backpropagation()
    output = bpnn.run(net_input)
    print("Result is: ", output)
    print("Mean squared error is: ", bpnn.calculate_mean_squared_error())
    print("Max error of a single neuron is: ", bpnn.calculate_max_error())
    plot_activations(bpnn)
    


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_backpropagation()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
