# Page Unit Doctrine



Each book page must be treated as a single knowledge unit.



A page has two synchronized representations:



- text/page_XXX.txt

- images/page_XXX.png



The text and image are not independent sources.



They represent the same page.



Operational Rule:



Whenever OpenClaw reads a page text file, it must inspect the corresponding page image file before drawing conclusions.



No pattern extraction should rely on text alone when a page image exists.



The page manifest links text and image into one unit.



Correct unit:



page_044.txt

page_044.png

page_044.json



Incorrect interpretation:



Text as one source and image as separate evidence.



Purpose:



Preserve the author's original explanation, including charts, drawings, candles, gaps, support, resistance, and visual annotations.
