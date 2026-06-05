# OHLCV Standard



Purpose:



Define the normalized candle data format used by MarketMirrorAI.



Required Fields:



symbol:



timeframe:



timestamp:



open:



high:



low:



close:



volume:



source:



session:



---



## Meaning



Open:



First traded price of the candle.



High:



Highest traded price during the candle.



Low:



Lowest traded price during the candle.



Close:



Last traded price of the candle.



Volume:



Total traded shares or contracts during the candle.



Timestamp:



Candle time reference.



Timeframe:



Chart interval used for analysis.



Examples:



- 1m

- 5m

- 15m

- 1h

- 4h

- 1d



---



## Operational Use



OHLCV data must be used to generate candlestick charts.



Those charts are then inspected visually.



Raw OHLCV alone should not produce final CALL, PUT, WAIT, or EXIT decisions.



---



## Derived Visual Elements



From OHLCV, MarketMirrorAI must derive:



- candle body

- candle wick

- candle color

- gap

- trend

- support

- resistance

- volume expansion

- volume contraction

- moving averages
