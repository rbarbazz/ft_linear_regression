import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('data.csv')
X = dataset['km']
Y = dataset['price']

thetas = pd.read_csv('thetas.csv')
t0 = thetas.iloc[-1]['t0']
t1 = thetas.iloc[-1]['t1']
iterations = 10
learning_rate = 1
m = float(len(dataset['km']))

for i in range(iterations):
    y_curr = t0 + (t1 * X)
    tmp_t0 = learning_rate * (1 / m) * sum(y_curr - Y)
    tmp_t1 = learning_rate * (1 / m) * sum(y_curr - Y) * X
    t0 -= tmp_t0
    t1 -= tmp_t1
    print('{} {}'.format(t0, t1))

print('\n{} {}'.format(t0, t1))

# pred_line = t0 + (t1 * X)
# plt.scatter(X, Y)
# plt.plot(X, pred_line, color='red')
# plt.show()
