import twstock as t
import pandas as p
import plotly.express as e

stock = t.Stock('0050')
date = stock.date
price = stock.price
amount = stock.capacity

data = p.DataFrame({'日期':date, '收盤價':price})
result = e.line(data, x='日期', y='收盤價', title='0050收盤價')
result.show()

data = p.DataFrame({'日期':date, '成交量':amount})
result = e.bar(data, x='日期', y='成交量', title='0050成交量')
result.show()