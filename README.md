Insight Data Engineering
===========================================================

# Applicant Readme

## Assumptions:
	- The output format is %.2f without rounding up.(5/3 = 1.66). For rounding up version(5/3 = 1.67), please uncomment line 17 in average_degree.py
	- Assume the data source does not end up with the delimiter. Start|{json}\n{json}\n....{json}|End
	- Time window is exclusive(00:01 to 01:00)

## Running the run.sh
	- Generate the required output.txt, as well as slow_output.txt as a comparison
	- Display the run time. Fast method is 3 times faster than the slower method.

## Running Environment
	- Python 3.4.3
	- run.sh has already been modified with python3
	- no other dependencies

## Implementation:
	- Normal method: maintain a heap, record the popped and pushed hashtags, and update the graph. Only modify part of the graph when necessary
	- Slow method: maintain a heap, recalculate the entire graph with the heap everytime a new tweet come.
