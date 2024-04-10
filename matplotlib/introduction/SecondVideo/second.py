#!/usr/bin/python3

from matplotlib import pyplot as plt
import pandas as pd
import csv
from collections import Counter

"""
    with open ('data.csv') as file:
        csv_reader = csv.DictReader(file)
"""
data = pd.read_csv('data.csv', on_bad_lines='skip')
ids = data['Responder_id']
programming_langauges  = data['LanguagesWorkedWith']
my_counter = Counter()

for response in programming_langauges:
    my_counter.update(response.split(';'))

languages = []
popularity  = []

for item in my_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

"""
languages.reverse()
popularity.reverse()

To reverse the order

"""

plt.barh(languages, popularity)
plt.title("Most Popular Languages")
plt.xlabel("The Count")
# plt.legend()
# plt.grid(True)
plt.tight_layout() # padding
plt.show()