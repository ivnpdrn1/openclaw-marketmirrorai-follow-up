# MarketMirrorAI Performance Metrics



Purpose:



Define the master metrics used to evaluate diagnostic quality, trade quality, and learning quality.



---



## t1



Definition:



Time between BUY Decision Point and actual trend change.



Interpretation:



Measures anticipation of entry.



Larger is better.



Objective:



Increase the ability to detect trend changes before they become obvious.



---



## t2



Definition:



Time between actual trend change and actual opposite trend change.



Interpretation:



Measures the duration of the opportunity.



Larger is better.



Objective:



Identify setups capable of producing longer trend persistence.



---



## t3



Definition:



Time between SELL Decision Point and actual opposite trend change.



Interpretation:



Measures anticipation of trend exhaustion.



Larger is better.



Objective:



Detect weakening trends before value erosion begins.



---



## h



Definition:



Total magnitude of the trend between trend change and opposite trend change.



Interpretation:



Measures total opportunity size.



Larger is better.



Objective:



Identify high-value opportunities.



---



## Capture Efficiency



Definition:



Captured h



/



Total h



Interpretation:



Measures how much of the available opportunity was captured.



Higher is better.



---



## Ratio1



Definition:



Correctly Anticipated Trend Changes



/



Total Decision Points



Interpretation:



Measures diagnostic accuracy.



Higher is better.



---



## Ratio2



Definition:



Decision Points Without Trend Change



/



Total Decision Points



Interpretation:



Measures false signal rate.



Lower is better.



---



## Daily Evaluation Rule



Every completed trade must update:



- t1

- t2

- t3

- h

- Capture Efficiency

- Ratio1

- Ratio2



No completed trade may be ignored.



Every completed trade becomes future learning material.
