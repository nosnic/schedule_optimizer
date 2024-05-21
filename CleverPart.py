import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error


class SmartAss():
    def __init__(self):
        self.data = pd.read_csv('data.csv', encoding='latin1', sep=';')  # dataset
        self.X = self.data[['ï»¿Teacher', 'Session', 'Profile', 'Attend', 'Lecture', 'Practic', 'Dopsa']].values
        self.y = self.data[['Itog']].values
        self.X = np.hstack((np.ones((self.X.shape[0], 1)), self.X))
        self.norm_eq_weight = self.normal_equation()
        self.mse = self.mse()

    def mse(self):
        print(mean_squared_error(self.y, np.dot(self.X, self.norm_eq_weight)))

    def normal_equation(self):
        return np.linalg.inv(self.X.T @ self.X) @ (self.X.T @ self.y)

    def linear_prediction(self, X, w):
        return np.dot(X, w)

    def find_weights(self, table):
        result = []
        for i in range(len(table)):
            for j in range(len(table[i])):
                tmp = [1, table[i][j]['teacher'], table[i][j]['session'], table[i][j]['profile'],
                       table[i][j]['notable'], table[i][j]['lecture'], table[i][j]['practica'], table[i][j]['dopsa']]
                res = self.linear_prediction(tmp, self.norm_eq_weight)
                if table[i][j]['day'] == 5 or table[i][j]['day'] == 6:
                    res = res * 0.8
                if table[i][j]['time'] == 1:
                    res = res * 0.9
                result.append(round(res[0], 2))
        return result

    def createNewTable(self, table, weights):
        n = 0
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] != "":
                    print(str(weights[n]) + " : " + str(table[i][j]))
                    if weights[n] < 0.5:
                        table[i][j] = ""
                    n += 1
        return table