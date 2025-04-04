import numpy as np

class Perceptron2Layer:
    def __init__(self, threshold=0.5):
        # For a 2-input gate with one hidden layer of 2 neurons.
        self.inputSize = 2
        self.hiddenSize = 2
        self.threshold = threshold
        # Hidden layer: weights and biases.
        self.weights_hidden = np.zeros((self.hiddenSize, self.inputSize))
        self.bias_hidden = np.zeros(self.hiddenSize)
        # Output layer: weights and bias.
        self.weights_output = np.zeros(self.hiddenSize)
        self.bias_output = 0
        # Lookup tables for XOR and XNOR.
        self.xorLUT = np.array([0, 1, 1, 0])
        self.xnorLUT = np.array([1, 0, 0, 1])
        self.whichGate = ""
    
    def randomizeWeights(self):
        # Randomize weights and biases for both layers.
        self.weights_hidden = np.random.randn(self.hiddenSize, self.inputSize)
        self.bias_hidden = np.random.randn(self.hiddenSize)
        self.weights_output = np.random.randn(self.hiddenSize)
        self.bias_output = np.random.randn()
    
    def activation(self, x):
        # Step activation function.
        return 1 if x > self.threshold else 0
    
    def predict(self, inputs):
        """
        Feeds the input through the hidden layer (with non-linearity)
        and then through the output layer to compute the final result.
        """
        hidden_raw = np.dot(self.weights_hidden, inputs) + self.bias_hidden
        hidden_activation = np.array([self.activation(val) for val in hidden_raw])
        output_raw = np.dot(self.weights_output, hidden_activation) + self.bias_output
        return self.activation(output_raw)
    
    def evaluate(self, gateType, max_attempts=10000):
        """
        Searches for a valid configuration (weights and biases) that
        using the LUT for evaluation.
        Prints the parameters upon success.
        """
        default_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        
        if gateType.upper() == "XOR":
            self.whichGate = "XOR"
            expected_outputs = self.xorLUT
        elif gateType.upper() == "XNOR":
            self.whichGate = "XNOR"
            expected_outputs = self.xnorLUT
        else:
            print("Unsupported gate type!")
            return
        
        # Random search for a configuration that matches the truth table.
        for attempt in range(max_attempts):
            self.randomizeWeights()
            valid = True
            for inp, expected in zip(default_inputs, expected_outputs):
                if self.predict(inp) != expected:
                    valid = False
                    break
            if valid:
                print(f"Found a solution for {self.whichGate} gate after {attempt+1} attempts!")
                print("Hidden layer weights:\n", self.weights_hidden)
                print("Hidden layer biases:", self.bias_hidden)
                print("Output layer weights:", self.weights_output)
                print("Output layer bias:", self.bias_output)
                return
        print("Failed to find a solution after maximum attempts.")
    
    def testInputs(self, inputs):
        """
        Given an array of input combinations, prints the truth table
        using the current weights and biases.
        """
        print(f"\nTesting the Gate with inputs and printing truth table for: {self.whichGate} gate:")
        for inp in inputs:
            print(f"{inp} --> {self.predict(inp)}")

# --- Main Function for Two-Layer Perceptron ---
if __name__ == '__main__':
    # Create an object of the class.
    perceptronXOR = Perceptron2Layer()

    print("\nXOR Gate - \n")
    # Evaluating for XOR Gate
    perceptronXOR.evaluate("XOR")

    # Testing with all input combinations and printing Truth Table
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    perceptronXOR.testInputs(inputs)

    # Create an object of the class.
    perceptronXNOR = Perceptron2Layer()

    print("\nXNOR Gate - \n")
    # Evaluating for XNOR Gate
    perceptronXNOR.evaluate("XNOR")

    # Testing with all input combinations and printing Truth Table
    perceptronXNOR.testInputs(inputs)

