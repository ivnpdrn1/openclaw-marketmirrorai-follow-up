# Visual-First Diagnosis Policy



MarketMirrorAI must not rely only on numerical data.



Numerical OHLCV data must be transformed into candlestick charts before final diagnosis.



Required Inputs:



- Live candlestick chart

- Relevant book page units

- MMAI rules

- MMAI signal definition

- MMAI validation requirements



Diagnosis Order:



1. Inspect live chart image.

2. Identify visible structures:

   - trend

   - gap

   - support

   - resistance

   - volume behavior

   - moving averages

   - candle formation

3. Compare against book page units.

4. Select candidate MMAI pattern.

5. Apply rules.

6. Check confirmations.

7. Produce decision.



Decision Discipline:



CALL only when bullish visual pattern and rules agree.



PUT only when bearish visual pattern and rules agree.



WAIT when evidence is incomplete, mixed, unclear, or contradictory.



EXIT when an active position loses the original visual/rule justification.



Primary Objective:



Low-error diagnosis under time constraints.
