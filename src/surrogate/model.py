from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
import numpy as np

class MLSurrogateModel:
    def __init__(self, model_type="rf"):
        """
        Initialize the surrogate model: RandomForest or Neural Network.
        """
        if model_type == "rf":
            self.model = RandomForestRegressor(n_estimators=100)
        elif model_type == "nn":
            self.model = MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=500)
        else:
            raise ValueError("Unsupported model type. Choose 'rf' or 'nn'.")

    def train(self, X_train, y_train):
        """
        Train ML surrogate model.
        Features X: ground energy, energy gap, dipole moment, polarizability
        """
        print(f"Training {self.model.__class__.__name__}...")
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Predict properties for candidates
        """
        return self.model.predict(X_test)
