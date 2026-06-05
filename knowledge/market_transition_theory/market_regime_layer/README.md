# MarketMirrorAI Market Regime Layer



Purpose:



Determine the current market environment before pattern activation and diagnosis.



Core Principle:



The same visual pattern may behave differently under different market regimes.



Market regime must be identified before assigning confidence to any MMAI pattern.



Operational Sequence:



1. Collect market context.

2. Evaluate SPY behavior.

3. Evaluate QQQ behavior.

4. Evaluate volatility conditions.

5. Evaluate trend conditions.

6. Classify current regime.

7. Send regime classification to Pattern Activation Engine.

8. Send regime classification to Confidence Engine.



Possible Regimes:



* Bull Market

* Bear Market

* Sideways Market

* High Volatility

* Low Volatility

* Risk-On

* Risk-Off



Operational Rule:



Market regime influences confidence.



Market regime does not replace pattern diagnosis.



Visual diagnosis remains primary.



Market regime provides context.



Example:



Bullish Pattern

+

Bull Market



↓



Increase confidence



Example:



Bullish Pattern

+

Bear Market



↓



Reduce confidence



Example:



Bearish Pattern

+

Risk-Off Environment



↓



Increase confidence



Important:



A valid pattern may still be rejected when market regime is strongly contradictory.

