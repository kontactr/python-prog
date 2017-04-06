import plotly.plotly as py
import plotly.figure_factory as FF
from datetime import datetime

import pandas_datareader.data as web
df = web.DataReader("fa", 'yahoo', datetime(2007, 10, 1), datetime(2009, 4, 1))
fig = FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index)
py.iplot(fig, filename='finance/aapl-candlestick', validate=False)

fig = FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index)
# Update the fig - all options here:   	
fig['layout'].update({
    'title': 'The Great Recession',
    'yaxis': {'title': 'AAPL Stock'},
    'shapes': [{
        'x0': '2007-12-01', 'x1': '2007-12-01',
        'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
        'line': {'color': 'rgb(30,30,30)', 'width': 1}
    }],
    'annotations': [{
        'x': '2007-12-01', 'y': 0.05, 'xref': 'x', 'yref': 'paper',
        'showarrow': False, 'xanchor': 'left',
        'text': 'Official start of the recession'
    }]
})
py.iplot(fig, filename='finance/aapl-recession-candlestick', validate=False)