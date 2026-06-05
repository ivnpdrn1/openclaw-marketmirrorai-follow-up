# MarketMirrorAI Execution Engine



Purpose:



Convert diagnosis into structured trading decisions.



The Execution Engine does not guess.



It only produces CALL, PUT, WAIT, or EXIT after reviewing:



- visual diagnosis

- MMAI classification

- rule confirmation

- market context

- confidence score

- risk notes



Core Rule:



WAIT is the default decision when evidence is incomplete, contradictory, or visually unclear.



Execution Sequence:



1. Receive visual diagnosis.

2. Identify primary and secondary MMAI patterns.

3. Apply pattern rules.

4. Check market context.

5. Calculate confidence score.

6. Define invalidation level.

7. Produce decision.

8. Send decision to Experience Engine for future review.



Decision Types:



CALL:



Bullish opportunity.



PUT:



Bearish opportunity.



WAIT:



No reliable action.



EXIT:



Original thesis invalidated.



Important:



This engine supports alerts and analysis.



It does not execute trades automatically.
