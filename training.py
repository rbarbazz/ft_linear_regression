import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('data.csv')
X = dataset['km']
Y = dataset['price']

thetas = pd.read_csv('thetas.csv')
t0 = thetas.iloc[-1]['t0']
t1 = thetas.iloc[-1]['t1']

iterations = 1000
learning_rate = 0.1
n = float(len(dataset['km']))

# Normalization
X_norm = ((X - X.min()) / (X.max() - X.min()))

for i in range(iterations):
    Y_pred = t0 + (t1 * X_norm)
    tmp_t0 = (1/n) * sum(Y_pred - Y)
    tmp_t1 = (1/n) * sum(X_norm * (Y_pred - Y))
    t0 -= learning_rate * tmp_t0
    t1 -= learning_rate * tmp_t1

# # Find the "unormalized" thetas
# t0 += (t1 * X.min()) / (X.max() - X.min())
# t1 = t1 / (X.max() - X.min())

# Save the thetas found
thetas = pd.DataFrame({
    't0': [t0],
    't1': [t1]
})
thetas.to_csv('thetas.csv', mode='a', header=False, index=False)

# Plot data
Y_pred = t0 + (t1 * ((X - X.min()) / (X.max() - X.min())))
plt.figure(num='Linear Regression')
plt.scatter(X, Y)
plt.plot([max(X), min(X)], [min(Y_pred), max(Y_pred)], color='red')
plt.show()
