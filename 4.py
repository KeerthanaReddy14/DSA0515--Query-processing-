import matplotlib.pyplot as plt
import yfinance as yf
data = yf.download('GOOGL', start='2023-01-01', end='2023-12-31')
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], label='Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Alphabet Inc. Stock Prices')
plt.legend()
plt.show()
