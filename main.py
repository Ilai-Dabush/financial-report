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
    "IBIT": "ביטקוין",
    "ETHA": "איתריום",
    "MSTR": "microstrategy",
    "IREN": "iren",
    "CLSK": "cleanspark",
    "DDOG": "דאטה דוג",
    "GOOGL": "גוגל",
    "AMZN": "אמזון",
    "ESTC": "אלסטיק",
    "7974.T": "נינטנדו"
}


def cal_change_from_open(price: int, open_: int):
    return ((price - open_) / open_) * 100


def get_info():
    data = yf.Tickers(" ".join(COMPANIES.keys()))
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
    get_info()
