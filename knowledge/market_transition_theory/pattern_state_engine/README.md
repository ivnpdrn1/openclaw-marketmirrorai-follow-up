# MarketMirrorAI Pattern State Engine



Purpose:



Determine the current state of the market before evaluating individual MMAI patterns.



Core Principle:



Patterns do not exist in isolation.



Every pattern exists inside a broader market state.



Primary States:



STATE-001



Bearish Channel



Associated Pattern:



MMAI-005



Typical Decision:



WAIT



---



STATE-002



Bullish Reversal Candidate



Associated Pattern:



MMAI-001



Typical Decision:



CALL Candidate



---



STATE-003



Bullish Confirmation



Associated Pattern:



MMAI-002



Typical Decision:



CALL



---



STATE-004



Bullish Continuation



Associated Patterns:



Future MMAI Patterns



Typical Decision:



CALL Management



---



STATE-005



Bearish Breakdown



Associated Patterns:



MMAI-007



MMAI-008



Typical Decision:



PUT



Operational Rule:



Market state must be identified before pattern scoring begins.



Decision Hierarchy:



Market State



↓



Pattern Recognition



↓



Rule Validation



↓



Confidence Scoring



↓



Decision



Goal:



Reduce false classifications caused by analyzing patterns without context.

