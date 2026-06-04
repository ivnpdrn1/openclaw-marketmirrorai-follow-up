# MarketMirrorAI Visual Recognition Layer



Purpose:



MarketMirrorAI must diagnose market situations visually before applying trading theory.



The books and classes are primarily visual.



Candlestick charts, gaps, support, resistance, moving averages, volume, and trend behavior must be interpreted as images first.



Core Sequence:



1. Receive OHLCV market data.

2. Generate candlestick charts.

3. Compare live charts against book page units.

4. Identify the closest MMAI pattern.

5. Retrieve the corresponding theory, rules, signals, and validation files.

6. Produce CALL, PUT, WAIT, or EXIT only when visual and rule-based evidence agree.



Operational Principle:



Visual diagnosis comes before theoretical application.



Text explains the image.



The image identifies the situation.



Risk Rule:



If visual evidence and textual rules disagree, OpenClaw must choose WAIT.



Goal:



Maximize correct diagnosis and minimize losses caused by misclassification.
