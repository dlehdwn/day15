
import yfinance

apple = yfinance.Ticker("AAPL")
current_price = apple.info['currentPrice']
print(f"애플 주식의 현재가격: {current_price}") #애플 주식의 현재가격: 193.89


microsoft = yfinance.Ticker("MSFT")
current_price = microsoft.info['currentPrice']
print(f"마이크로소프트 주식의 현재가격: {current_price}") #마이크로소프트 주식의 현재가격: 396.51


google = yfinance.Ticker("GOOG")
current_price = google.info['currentPrice']
print(f"구글 주식의 현재가격: {current_price}") #구글 주식의 현재가격: 147.71