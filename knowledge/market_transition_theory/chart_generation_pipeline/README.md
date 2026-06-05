# MarketMirrorAI Chart Generation Pipeline



Purpose:



Convert normalized OHLCV market data into visual candlestick charts.



Core Principle:



MarketMirrorAI is visual-first.



The system must generate chart images before final diagnosis.



Input:



- normalized OHLCV data

- symbol

- timeframe

- date range

- volume

- source



Output:



- candlestick chart image

- volume panel

- moving averages when required

- support/resistance overlays when detected

- chart metadata



Required Timeframes:



- 5m

- 15m

- 1h

- 4h

- 1d



Operational Sequence:



1. Receive normalized OHLCV data.

2. Build candlestick chart.

3. Add volume panel.

4. Add moving averages when relevant.

5. Save chart image.

6. Send chart image to Visual Recognition Layer.

7. Store chart metadata for audit.



Important Rule:



The generated chart must be comparable to the visual examples found in the books.



Diagnosis must compare live chart images with book page units, not raw numbers alone.
