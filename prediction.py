import sys
import pandas as pd


# Get last computed thetas if exist
def get_thetas(reset=False):
    # Reset thetas
    if reset:
        thetas = pd.DataFrame({'t0': [0], 't1': [0]})
        thetas.to_csv('thetas.csv', mode='w', header=['t0', 't1'], index=False)

    try:
        thetas = pd.read_csv('thetas.csv')
    except:
        thetas = pd.DataFrame({'t0': [0], 't1': [0]})
        thetas.to_csv('thetas.csv', mode='w', header=['t0', 't1'], index=False)
    t0 = thetas.iloc[-1]['t0']
    t1 = thetas.iloc[-1]['t1']
    return t0, t1

if __name__ == '__main__':
    txt_input = input('Please input a car mileage: ')
    try:
        mileage = float(txt_input)
    except ValueError:
        sys.exit('Input is not a number')

    t0, t1 = get_thetas()

    price_prediction = t0 + (t1 * mileage)
    print('Estimated price for this mileage: {}'.format(int(price_prediction)))

# Bonus:
# - Plotting the data into a graph to see their repartition
# - Plotting the line resulting from the linear regression into the same graph
# - Calculating and plotting the precision of the algorithm
# - Reset option to reset the thetas
