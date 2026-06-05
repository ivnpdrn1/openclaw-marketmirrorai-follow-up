# MarketMirrorAI Pattern Ranking Engine



Purpose:



Rank activated MMAI patterns before sending them to the Confidence Engine.



Core Principle:



Activation selects which patterns are relevant.



Ranking determines which activated patterns deserve priority.



Inputs:



- activated pattern families

- visual similarity

- market regime adjustment

- pattern dependencies

- rule readiness

- historical validation

- event risk



Outputs:



- primary candidate pattern

- secondary candidate pattern

- rejected patterns

- ranking score

- reason for ranking



Operational Sequence:



1. Receive activated MMAI patterns.

2. Apply regime adjustments.

3. Apply visual similarity estimate.

4. Apply dependency relationships.

5. Apply rule readiness.

6. Apply validation status.

7. Rank patterns.

8. Send top candidates to Confidence Engine.



Important Rule:



The highest ranked pattern is not automatically tradable.



The Execution Engine must still confirm rules, confidence, risk, and context.
