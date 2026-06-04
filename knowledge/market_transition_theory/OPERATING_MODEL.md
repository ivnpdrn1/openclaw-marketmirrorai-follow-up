# MarketMirrorAI Operating Model



Purpose:



Define how MarketMirrorAI and OpenClaw must analyze market opportunities.



Core Principle:



The system is visual-first, evidence-based, and risk-aware.



Operational Sequence:



1. Receive market data from APIs.

2. Convert OHLCV data into candlestick charts.

3. Inspect the live market chart visually.

4. Compare the live chart against book page units.

5. Identify candidate MMAI patterns.

6. Apply rules.

7. Apply confidence scoring.

8. Check market context.

9. Produce CALL, PUT, WAIT, or EXIT.

10. Store the outcome in the Experience Engine.



Decision Priority:



WAIT is preferred when evidence is incomplete, contradictory, or visually unclear.



CALL requires bullish visual diagnosis plus rule confirmation.



PUT requires bearish visual diagnosis plus rule confirmation.



EXIT requires loss of original diagnosis or violation of invalidation level.



Learning Loop:



Every signal must eventually produce a review.



Every review must improve future diagnosis.



Books provide methodology.



Markets provide validation.



OpenClaw must preserve both.
