import subprocess
import csv
import os

def run_bandit_and_report():
    # Run bandit on Python files
    result = subprocess.run(['bandit', '-r', '--format', 'csv', '/Users/chocks/Desktop/Fall 2023/SQA/Final Project'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Save results to a CSV file
    with open('security_report.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(['Filename', 'Line', 'Test Name', 'Issue Severity', 'Issue Confidence', 'Issue Text'])
        # Write the analysis result
        for line in result.stdout.splitlines():
            writer.writerow(line.split(','))

if __name__ == "__main__":
    run_bandit_and_report()
