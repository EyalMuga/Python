import os

path = 'AAPL.csv'


def csv_checker(path: str):
    if not os.path.exists(path):
        print("path not exist")
        return False

    with open(path, 'r') as f:
        cols = None
        rows = 0
        for line in f:
            items = line.split(',')
            if cols is None:
                cols = len(items)
            elif len(items) != cols:
                print("inconsistent number of columns")
                return False
            rows += 1

        print(f"file self: {os.path.basename(path)}")
        print(f"columns: {cols}")
        print(f"rows: {rows}")


if __name__ == '__main__':
    csv_checker(path)

