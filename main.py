import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('cardio_train_cleaned.csv', sep=',')

class My_Regression_Logistic:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        
    def sigmoid(self, x):
        if isinstance(x, np.ndarray):
            exp_vals = np.exp(-np.abs(x))
            return np.where(x >= 0, 1 / (1 + exp_vals), exp_vals / (1 + exp_vals))
        else:
            if x >= 0:
                return 1 / (1 + np.exp(-x))
            else:
                exp_val = np.exp(x)
                return exp_val / (1 + exp_val)

    def compute_loss(self, y_true, y_pred):
        epsilon = 1e-9
        y1 = y_true * np.log(y_pred + epsilon)
        y2 = (1 - y_true) * np.log(1 - y_pred + epsilon)
        return -np.mean(y1 + y2)

    def feed_forward(self, x):
        z = np.dot(x, self.weights) + self.bias
        A = self.sigmoid(z) 
        return A
        
    def fit(self, x, y):
        n_samples, n_features = x.shape
        
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iters):
            A = self.feed_forward(x)
            dz = A - y
            
            dw = (1 / n_samples) * np.dot(x.T, dz)
            db = (1 / n_samples) * np.sum(dz)
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
    def predict(self, x):
        threshold = 0.5
        y_hat = np.dot(x, self.weights) + self.bias
        y_predicted = self.sigmoid(y_hat) 
        y_predicted_cls = [1 if i > threshold else 0 for i in y_predicted]
        
        return np.array(y_predicted_cls)

X = df[['age_years', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']]
y = df['cardio']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y)

regressor = My_Regression_Logistic(learning_rate=0.01, n_iters=5000)
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)
cm = confusion_matrix(np.asarray(y_test), np.asarray(predictions))

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f_score = f1_score(y_test, predictions)

print("Test accuracy: {0:.3f}".format(accuracy))
print("Confusion Matrix:")
print(np.array(cm))
print("Precision: {0:.3f}".format(precision))
print("Recall: {0:.3f}".format(recall))
print("F1-score: {0:.3f}".format(f_score))