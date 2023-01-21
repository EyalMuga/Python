import csv
import threading
from concurrent.futures import ThreadPoolExecutor


def process_row(row, year_files):
    # Extract the year from the date field
    year = row['date'][:4]
    # Get the file for this year, creating it if necessary
    if year not in year_files:
        year_files[year] = open(f'AAPL_{year}.csv', 'w', newline='')
        writer = csv.DictWriter(year_files[year], fieldnames=row.keys())
        writer.writeheader()
    else:
        writer = csv.DictWriter(year_files[year], fieldnames=row.keys())
    # Write the row to the file
    writer.writerow(row)


def main():
    # Read the original AAPL.csv file and parse the data into a list of dictionaries
    with open('AAPL.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Create a ThreadPoolExecutor with a suitable number of threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Create a lock to protect access to the year_files dictionary
        lock = threading.Lock()
        # Create a dictionary to store the files for each year
        year_files = {}
        # Submit a task to process each row of data
        for row in data:
            executor.submit(process_row, row, year_files, lock)

    # Close all the files
    for file in year_files.values():
        file.close()


if __name__ == '__main__':
    main()
