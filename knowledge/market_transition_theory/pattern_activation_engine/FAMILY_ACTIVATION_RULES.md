# Family Activation Rules



Purpose:



Define how MarketMirrorAI activates pattern families before detailed analysis.



---



## Bullish Reversal Family Activation



Activate when one or more of the following are detected:



* Strong support zone

* Piso Fuerte

* Bullish gap

* Bullish breakout

* Green reversal candle

* Trendline breakout

* Recovery after decline



Activate Family:



* MMAI-001

* MMAI-002

* MMAI-003

* MMAI-004



---



## Bearish Continuation Family Activation



Activate when one or more of the following are detected:



* Descending channel

* Lower highs

* Lower lows

* Red opening candle

* Gap failure

* Support breakdown

* Bearish continuation



Activate Family:



* MMAI-005

* MMAI-006

* MMAI-007

* MMAI-008



---



## Event Family Activation



Activate when one or more of the following are detected:



* Upcoming earnings

* Earnings released

* Post-earnings reaction

* Earnings gap

* Unusual volume after earnings



Activate Family:



* MMAI-009

* MMAI-010



---



## Confirmation Family Activation



Always activate when a primary family is active.



Activate Family:



* MMAI-011

* MMAI-012

* MMAI-013

* MMAI-014

* MMAI-015



---



Conflict Rule



If Bullish Reversal Family and Bearish Continuation Family are both active:



Decision State:



CONFLICT



Required Action:



Activate Confirmation Family.



Increase analysis depth.



Prefer WAIT until conflict is resolved.



---



Priority Rule



Primary Families:



* Bullish Reversal

* Bearish Continuation



Secondary Family:



* Event



Validation Family:



* Confirmation



Operational Principle:



Activation narrows the search space.



Classification occurs later.

