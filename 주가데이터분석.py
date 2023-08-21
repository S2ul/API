import pandas_datareader.data as web
import fix_yahoo_finance
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2022, 3, 26)

lg = web.get_data_yahoo('066570.KS', start, end)
samsung = web.get_data_yahoo('005930.KS', start, end)

fig, ax1 = plt.subplots()
ax1.plot(lg.index, lg['Adj Close'], 'r-', label = 'LG')
ax1.set_xlabel('Time[Year]')
ax1.set_ylabel('LG', color='r')
ax1.tick_params('y', colors='r')
plt.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(samsung.index, samsung['Adj Close'], 'b-', label = 'SAMSUNG')
ax2.set_ylabel('SAMSUNG', color='b')
ax2.tick_params('y', colors='b')
plt.legend(loc='upper right')

fig.tight_layout()
plt.show()