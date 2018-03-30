# three-point-lines
A python program that accepts a set of points via csv, determines if they use at least 3 points to form a line,
 and outputs the result back as a csv.

## Requirements
* Python 3.x

## Quick Run
1. git clone https://github.com/d0coat01/three-point-lines.git or download zip.
2. python three-lines.py
3. Outputs to same directory as daniel_coats_lines_output.csv

## Configuration
* Edit lines.csv to change the input.
## Example
* Input Example:
```
0.0,0.0
1.1,1.1
3.5,4.5
2.2,2.2
0.1,1.0
2.1,1.2
3.1,1.3
```
* Output Example:
```
1,0.0,0.0,1.1,1.1,2.2,2.2
2,0.1,1.0,1.1,1.1,2.1,1.2,3.1,1.3
```
**NOTE**: The first column of the output is the line identifier (1 & 2 in this case)
## Assumptions
* Input will always be a valid csv.
* Col values are valid floats.
* Rows contain two columns each, are comma delimitted, and newline separated.
* There are no memory restrictions. I can store the points in a data structure of my choosing.
* Python has read/write access to the current directory the program resides in.

Based on my assumptions, my program will fail in the event of:
* restricted memory
* An invalid csv is provided
* Not enough permissions to read/write to current directory.

## Implementation

* A python dictionary is used.
* The dictionary indices are made up of the slope calculations between sets of points.
* Since slope doesn't mean the line is unique, each slope index maps to a list of python Sets (unique collections)
* Since you need to calculate the slope between each pair of points, a minimum runtime of O(n^2) is required.
* Using a hash to store each slope:[lines] pair costs O(n^2) space
* Additional useful examples that were added included:
  1. a set of points that contained the same slope as another line but wasn't on the same line
  2. a set of points with slopes of 0 to test to make sure our slope calculator doesn't try to divide by 0.
