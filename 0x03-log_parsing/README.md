# Project 0x03: Log Parsing

Welcome to Project 0x03: Log Parsing! This project focuses on applying your knowledge of Python programming,
particularly in parsing and processing data streams in real-time. You will be reading from standard input (stdin), 
handling data in a specific format, and performing calculations based on the input data. Below, you will find detailed 
explanations of the project tasks along with the concepts and resources that might be useful.

## Overview

For the “0x03. Log Parsing” project, you will need to apply your knowledge of Python programming, focusing on parsing 
and processing data streams in real-time. This project involves reading from standard input (stdin), handling data in 
a specific format, and performing calculations based on the input data.

## Concepts Needed:

### File I/O in Python:
Understand how to read from sys.stdin line by line.
Python Input and Output

### Signal Handling in Python:
Handling keyboard interruption (CTRL + C) using signal handling in Python.
Python Signal Handling

### Data Processing:
Parsing strings to extract specific data points.
Aggregating data to compute summaries.

### Regular Expressions:
Using regular expressions to validate the format of each line.
Python Regular Expressions

### Dictionaries in Python:
Using dictionaries to count occurrences of status codes and accumulate file sizes.
Python Dictionaries

### Exception Handling:
Handling possible exceptions that may arise during file reading and data processing.
Python Exceptions

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, 
effectively handling data streams, parsing log entries, and computing metrics based on the processed data.


## Tasks

### 0. Log parsing
Write a script that reads stdin line by line and computes metrics:

- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, 
  the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
  - Total file size: File size: <total size>
  - Number of lines by status code:
    - Possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
    - If a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - Format: <status code>: <number>
    - Status codes should be printed in ascending order

Warning: In this sample, you will have a random value - it’s normal to not have the same output as this one.
