import pandas as pd
import matplotlib.pyplot as plt
import argparse
from prediction import get_thetas

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train the model')
    parser.add_argument(
        '-n',
        help='Display data after training',
        action='store_true',
        default=False
    )
    args = parser.parse_args()

    # Read data from provided CSV file
    dataset = pd.read_csv('data.csv')
    X = dataset['km']
    Y = dataset['price']

    t0, t1 = get_thetas()
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

    # Find the "unormalized" thetas
    t0_norm = t0
    t1_norm = t1
    t0 = t1_norm * - X.min() / (X.max() - X.min()) + t0_norm
    t1 = t1_norm * (1 - X.min()) / (X.max() - X.min()) + t0_norm - t0

    # Save the thetas found
    thetas = pd.DataFrame({
        't0': [t0],
        't1': [t1]
    })
    thetas.to_csv('thetas.csv', mode='a', header=False, index=False)

    if (args.n):
        # Plot data
        Y_pred = t0 + (t1 * X)
        plt.figure(num='Linear Regression')
        plt.scatter(X, Y)
        plt.plot([max(X), min(X)], [min(Y_pred), max(Y_pred)], color='red')
        plt.show()
