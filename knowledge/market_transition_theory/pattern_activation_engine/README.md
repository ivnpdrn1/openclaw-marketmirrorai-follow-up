# MarketMirrorAI Pattern Activation Engine



Purpose:



Reduce the number of patterns that must be evaluated for each diagnosis.



Core Principle:



Not every MMAI pattern is relevant to every market situation.



The system should activate candidate patterns before performing full evaluation.



Operational Sequence:



1. Receive live chart.



2. Detect high-level visual structures.



3. Activate relevant MMAI families.



4. Ignore unrelated MMAI families.



5. Send activated patterns to Visual Recognition Layer.



Example:



Bullish Gap Detected



↓



Activate:



* MMAI-002

* MMAI-003

* MMAI-004



Do Not Activate:



* MMAI-005

* MMAI-007

* MMAI-008



Example:



Descending Channel Detected



↓



Activate:



* MMAI-005

* MMAI-006

* MMAI-007

* MMAI-008



Do Not Activate:



* MMAI-002

* MMAI-003



Benefits:



* Faster diagnosis

* Lower computational cost

* Better pattern ranking

* Reduced false matches



Important Rule:



Activation is not classification.



Activation only determines which patterns deserve detailed evaluation.

