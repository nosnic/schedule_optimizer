import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error


class SmartPart:
    def __init__(self):
        self.load_data()
        self.preprocess_data()
        self.calculate_weights()

    def load_data(self):
        self.data = pd.read_csv('data/data.csv', encoding='latin1', sep=';')

    def preprocess_data(self):
        self.X = self.data[['ï»¿Teacher', 'Session', 'Profile', 'Attend', 'Lecture', 'Practic', 'Dopsa']].values
        self.y = self.data[['Itog']].values
        self.X = np.hstack((np.ones((self.X.shape[0], 1)), self.X))

    def calculate_weights(self):
        self.norm_eq_weight = np.linalg.inv(self.X.T @ self.X) @ (self.X.T @ self.y)
        self.mse = mean_squared_error(self.y, np.dot(self.X, self.norm_eq_weight))

    def linear_prediction(self, X):
        return np.dot(X, self.norm_eq_weight)

    def find_weights(self, table):
        weights = []
        for i in range(len(table)):
            for j in range(len(table[i])):
                tmp = [1, table[i][j]['teacher'], table[i][j]['session'], table[i][j]['profile'],
                       table[i][j]['notable'], table[i][j]['lecture'], table[i][j]['practica'], table[i][j]['dopsa']]
                res = self.linear_prediction(tmp)
                if table[i][j]['day'] in [5, 6]:
                    res *= 0.8
                if table[i][j]['time'] == 1:
                    res *= 0.9
                weights.append(round(res[0], 2))
        return weights

    def create_new_table(self, table, weights):
        n = 0
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] != "":
                    print(str(weights[n]) + " : " + str(table[i][j]))
                    if weights[n] < 0.5:
                        table[i][j] = ""
                    n += 1
        return table
