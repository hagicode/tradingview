import streamlit as st

html_code = """
<div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div><div class="tradingview-widget-copyright"><a href="https://jp.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">TradingViewですべてのマーケットを追跡</span></a></div><script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-tickers.js" async>{"symbols": [{"description": "ドル円","proName": "OANDA:USDJPY"},{"description": "WTI原油先物","proName": "MATBAROFEX:WTI1!"},{"description": "S&P500","proName": "FRED:SP500"},{"description": "VIX","proName": "CAPITALCOM:VIX"}],"isTransparent": false,"showSymbolLogo": true,"colorTheme": "light","locale": "ja"}</script></div>
"""

st.markdown(html_code, unsafe_allow_html=True)
