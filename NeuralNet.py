class Net(object):
    def __init__(self, dimArray):
        """
        Constructor, takes array with dimension of each layer as input
        """
        self.dimArray = dimArray
        self.weights = [] #list containing matrices between each layer
        self.biases = [] #list containing biases between each layer
        for i in range(len(dimArray)-1):
            dim = (dimArray[i+1] , dimArray[i])
            self.weights.append(np.random.random(dim))
            self.biases.append(np.random.random(dim[0]))
        
    def classify(self,inputVector):
        """
        Function to classify an image
        """
        res = inputVector
        for i in range(len(self.weights)):
            res = self.weights[i].dot(res) + self.biases[i]
        return res
