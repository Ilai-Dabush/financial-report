import yfinance as yf
import pyperclip

COMPANIES = {
    "AAPL": "אפל",
    "TSLA": "טסלה",
    "SNOW": "סנואו",
    "CLBT": "סלברייט",
    "INTU": "אינטואיט",
    "MSI": "מוטורולה",
    "META": "מטא",
    "JPM": "JP",
    "NVDA": "נבידיה",
    "QQQ": "נאסדק 100",
    "SPY": "סנופי",
    "PLTR": "פלאנטיר",
}


def cal_change_from_open(price: int, open_: int):
    return ((price - open_) / open_) * 100


def get_info():
    data = yf.Tickers("AAPL TSLA SNOW CLBT MSI INTU PLTR META JPM NVDA SPY QQQ")
    msg = "סיכום יום:\n"
    for ticker_code, ticker_data in data.tickers.items():
        change_from_open = 0
        history = ticker_data.history(period="2d")
        if ticker_data.info.get("currentPrice"):
            change_from_open = cal_change_from_open(ticker_data.info.get("currentPrice"), ticker_data.info.get("previousClose"))
        else:
            change_from_open = cal_change_from_open(history["Close"].iloc[-1], history["Close"].iloc[-2])
        msg += f"{COMPANIES[ticker_code]}: {abs(change_from_open):.2f}%{'-' if change_from_open  < 0 else ''}\n"
    print(msg)
    pyperclip.copy(msg)


if __name__ == '__main__':
    # d = yf.Ticker("SPY")
    # print(d.history(period="1d")["Close"][-1])
    # print(d.info.get("previousClose"))
    get_info()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
