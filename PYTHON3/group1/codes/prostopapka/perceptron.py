import numpy as np
def sigmoid(x):
    return 1/ (1 + np.exp(-x))

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])
training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2*np.random.random((3,1))-1

print("Случайно инициальзированные веса: ")
print(synaptic_weights)
for i in range(70000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    ajustments = np.dot(input_layer.T, err*(outputs*(1-outputs)))

    synaptic_weights += ajustments
print("веса после обучения")
print(synaptic_weights)
print("Результат после обучения: ")
print(outputs)


#TEST

new_inputs = np.array([0, 1, 1])
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print("New situation")
print(output)
    

