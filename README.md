# ColorConnect
CS5400 AI Puzzle Project
Anton Strickland

To run ColorConnect, type: 
python color-connect.py FILEPATH.TXT

Where FILEPATH.TXT should be replaced by the path to a puzzle instance text file.
There is already a folder in the directory called "config" which contains the puzzles for this semester.

After finding a solution, this program creates output files at:
output/solution-NAME.txt

Where NAME refers to the input filename.

Examples:
python color-connect.py config/puzzle1.txt
python color-connect.py config/puzzle2.txt

Notes: 
The version of Python used was 64-bit version 3.4.4.
Puzzle #2 took upwards of 9 GB of memory to solve, but I was still able to generate a solution file using my laptop.