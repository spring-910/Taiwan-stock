import streamlit as st
import yfinance as yf

st.set_page_config(page_title="台灣股票分析", layout="wide")
st.title("📈 台灣股票自選分析工具")

# 自選股清單
stock_list = ["2330.TW", "2317.TW", "2454.TW", "2303.TW"]
selected_stock = st.selectbox("請選擇股票代碼", stock_list)

# 選擇期間
period = st.selectbox("選擇資料期間", ["1mo", "3mo", "6mo", "1y", "5y"])

# 取得資料
stock = yf.Ticker(selected_stock)
data = stock.history(period=period)

# 技術指標
data["MA5"] = data["Close"].rolling(window=5).mean()
data["Change"] = data["Close"].pct_change() * 100

# 顯示圖表與資訊
st.line_chart(data["Close"])
st.write("📌 最新收盤價：", data["Close"].iloc[-1])
st.write("📌 平均價格：", round(data["Close"].mean(), 2))
st.write("📌 最高價：", data["High"].max())
st.write("📌 最低價：", data["Low"].min())
st.write("📌 平均漲跌幅：", round(data["Change"].mean(), 2), "%")
