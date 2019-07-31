import sys
import pandas as pd

txt_input = input('Please input a car mileage: ')

try:
    mileage = float(txt_input)
except ValueError:
    sys.exit('Input is not a number')

thetas = pd.read_csv('thetas.csv')
t0 = thetas.iloc[-1]['t0']
t1 = thetas.iloc[-1]['t1']

price_prediction = t0 + (t1 * mileage)
print('Thetas: {} and {}\nEstimated price for this mileage: {}'.format(
    t0,
    t1,
    int(price_prediction)
))
