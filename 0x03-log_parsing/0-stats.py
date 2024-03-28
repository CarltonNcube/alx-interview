#!/usr/bin/python3

import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0
    
    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) != 7:
                continue
            _, _, _, status_code, file_size, *_ = parts
            try:
                file_size = int(file_size)
                status_code = int(status_code)
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1
            except ValueError:
                continue
            
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

