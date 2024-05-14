import twstock as t
import pandas as p
import plotly.express as e

stock = t.Stock('0050')
period = stock.fetch_31()
data = p.DataFrame(period)
data.columns = ['日期', '成交股數', '成交量', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
data

period = stock.fetch(2021, 6)
data = p.DataFrame(period)
data.columns = ['日期', '成交股數', '成交量', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
data

period = stock.fetch_from(2019, 5)
data = p.DataFrame(period)
data.columns = ['日期', '成交股數', '成交量', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
data
result = e.line(data, x='日期', y='收盤價', title='0050收盤價')
result.show()