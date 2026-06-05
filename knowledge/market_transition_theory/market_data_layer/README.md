# MarketMirrorAI Market Data Layer



Purpose:



Define the raw market data required to generate charts and diagnose MMAI patterns.



Core Principle:



OpenClaw does not see the market directly.



OpenClaw receives structured data from market APIs.



That data must be converted into visual charts before final diagnosis.



Primary Data Sources:



- Finnhub

- Polygon

- Tradier

- TC2000

- Databento



Required Market Data:



- OHLCV candles

- timestamp

- symbol

- timeframe

- volume

- premarket data when available

- market session status

- news and catalysts

- earnings calendar

- SPY / QQQ context



Operational Sequence:



1. Request market data.

2. Normalize data.

3. Generate candlestick charts.

4. Send charts to Visual Recognition Layer.

5. Send normalized data to Confidence Engine.

6. Preserve raw data for audit.



Important Rule:



Raw numerical data alone is not sufficient for final diagnosis.



The system must generate visual candlestick charts before producing CALL, PUT, WAIT, or EXIT.

