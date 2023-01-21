import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def print_result(future):
    result = future.result()
    print(f"{result[0]}! = {result[1]}")


def main():
    numbers = [1500, 1500, 1500]
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(factorial, n) for n in numbers]
        for future in as_completed(futures):
            print_result(future)
    print(f"Total time took: {time.time() - start_time}")


if __name__ == '__main__':
    start_time = time.time()
    main()
