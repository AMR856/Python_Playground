#!/usr/bin/python3
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# bins = [20, 30, 40, 50, 60] eliminate some values

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins, edgecolor='black', log=True)

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Average Age', linewidth=2)
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
