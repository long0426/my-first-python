import twstock as t
import pandas as p

stock = t.realtime.get("0050")
# print(stock['success'])

result = p.DataFrame(stock).T.iloc[1:3]
result.columns = ['股票代碼','地區','股票名稱','公司全名','現在時間','最新成交價','成交量','累計成交量','最佳五檔賣出價','最佳五檔賣出量','最佳五檔買進價','最佳五檔買進量','開盤價','最高價','最低價']
result