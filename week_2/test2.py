import pandas as pd
import numpy as np

transactions = pd.DataFrame({
    'amount' : [100, 5000, 250, 10000, 750],
    'customer_history' : [50, 3, 27, 1, 12],
    'time_of_day' : [14, 3, 16, 2, 13],
    'unusual_location' : [0, 1, 0, 1, 0]
})

weights = {
    'amount' : 0.3,
    'customer_history' : 0.3,
    'time_of_day' : 0.2,
    'unusual_location' : 0.2
}

def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

transactions['amount_risk'] = normalize(transactions['amount']) * weights['amount']
transactions['history_risk'] = (1 - normalize(transactions['customer_history'])) * weights['customer_history']
transactions['time_risk'] = (abs(transactions['time_of_day'] - 12) / 12) * weights['time_of_day']
transactions['location_risk'] = transactions['unusual_location'] * weights['unusual_location']

transactions['total_risk'] = (
    transactions['amount_risk'] +
    transactions['history_risk'] +
    transactions['time_risk'] +
    transactions['location_risk']
)

print(transactions[['amount', 'total_risk']])