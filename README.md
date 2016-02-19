# ColorConnect
CS5400 AI Puzzle Project
Anton Strickland

To run ColorConnect, type: 
python color-connect.py FILEPATH.TXT ALGORITHM

Where FILEPATH.TXT should be replaced by the path to a puzzle instance text file.
Where ALGORITHM is the algorithm you want to perform (bfts, iddfts, gbfgs, gbfts, asgs, or asgs2).
And where python is the python interpreter to be used (which in my case was just "python").

There is already a folder in the directory called "config" which contains the puzzles for this semester.

After finding a solution, this program creates output files at:
output/solution-ALGORITHM-NAME.txt

Where ALGORITHM refers to the algorithm that was used to find the solution,
and where NAME refers to the input filename.

Examples:
python color-connect.py config/puzzle1.txt bfts
python color-connect.py config/puzzle2.txt iddfts
python color-connect.py config/puzzle3.txt gbfgs
python color-connect.py config/puzzle4.txt asgs
python color-connect.py config/puzzle5.txt asgs2

Notes: 
The version of Python I used was 64-bit version 3.4.4. You may need to use "python3" if "python" does not work.