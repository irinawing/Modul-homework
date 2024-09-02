from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, encoding="utf-8") as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


if __name__ == "__main__":
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    start_l = datetime.now()

    for filename in filenames:
        read_info(filename)

    end_l = datetime.now()
    print(f"{end_l - start_l} (линейный)")

    with multiprocessing.Pool(processes=8) as pool:
        start_m = datetime.now()
        pool.map(read_info, filenames)
    end_m = datetime.now()
    print(f"{end_m - start_m} (многопроцессный)")
