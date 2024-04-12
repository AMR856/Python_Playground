#!/usr/bin/python3
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)
price_date = data['Date']
price_close = data['Close']


plt.plot_date(price_date, price_close, linestyle='solid', linewidth=2, color='#6d904f')
plt.gcf().autofmt_xdate()

data_format = mpl_dates.DateFormatter('%b %d %y')
plt.gca().xaxis.set_major_formatter(data_format)
plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()

"""

format string for style: 
    data_format = mpl_dates.DateFormatter('%b, %d %Y')
    plt.gca().xaxis.set_major_formatter(data_format)
    
    Notes:
        not sorted by order because they are strings not dates
"""