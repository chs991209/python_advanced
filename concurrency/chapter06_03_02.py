import os
import time
import sys
import csv
from concurrent import futures
from decorators.decorators import (
    log_dependency_by_flush,
    string_args,
    first_arg_iterable_rest_string,
    MyIterable,
)

# 국가 정보를 Synchronous하게 python protocol로 call합니다.
NATION_LS = (
    "Singapore Germany Israel Norway Italy Canada France Spain Mexico".split()
)  # db에서 column 목록을 가져오면 더 효율적이다.
TARGET_CSV = "/Users/choehyeonsu/pyadvanced/python_advanced/resources/nations.csv"  # NOSQL directory
DEST_DIR = "/Users/choehyeonsu/pyadvanced/python_advanced/csvs"  # BASE directory
HEADER = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Priority",
    "Order Date",
    "Order ID",
    "Ship Date",
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit",
]  # CSV HEADER


@first_arg_iterable_rest_string
def save_csv(data, file_name):  # 단수의 CSV 파일을 저장한다.
    path = os.path.join(DEST_DIR, file_name)

    with open(path, "w", newline="") as fp:  # newline => 빈 string으로 할당하면 줄바꿈 처리 안함
        writer = csv.DictWriter(fp, fieldnames=HEADER)

        writer.writeheader()  # csv.DictWriter.writeheader

        for row in data:
            writer.writerow(row)


@string_args
def show_with_newline(string):
    print(string)
    sys.stdout.flush()


@string_args
def show(string):
    print(string, end="")
    sys.stdout.flush()


# NOSQL data 형태로 csv에서 뽑아냅니다.
@string_args
def get_sales_data_by_nation(nation):  # 선언문
    with open(TARGET_CSV, "r") as f:
        reader = csv.DictReader(f)  # Dictionaries를 담은 reader를 call

        data = [
            r for r in reader if r["Country"] == nation
        ]  # Using List Comprehension # reader type은 list가 아니며, .map()이 없다.
        show_with_newline("\nData rows: {}".format(len(data)))
        return data


@log_dependency_by_flush
def get_sales_data():  # 선언문
    with open(TARGET_CSV, "r") as f:
        reader = csv.DictReader(f)  # Dictionaries를 담은 reader를 call

        return [
            r for r in reader
        ]  # Using List Comprehension # reader type은 list가 아니며, .map()이 없다.
        # show_with_newline("\nData rows: {}".format(len(data)))


@first_arg_iterable_rest_string
def get_data_by_nation(data, nation):
    return [row for row in data if row["Country"] == nation]


sales_data = get_sales_data()


#  데이터를 csv 여러 개로 국가 별로 저장합니다.
# 선언문
def save_seperated_csvs(nation):
    # 저장 실행문
    show_with_newline(nation)  # 단순히 국가 별로 진행 상황을 콘솔에 찍는다.
    data_of_sales_by_nation = get_data_by_nation(sales_data, nation)
    iterable_data = MyIterable(data_of_sales_by_nation)

    save_csv(iterable_data, nation.lower() + ".csv")

    # return data_of_sales_by_nation
    return nation


iterable_nations = MyIterable(sorted(NATION_LS))


@log_dependency_by_flush
def main(save_nation_to_csv):
    """
    쓰레드 동시 실행 개수를
    최대 동시 작업 threads의 개수:
    len(NATION_LS)
    이상으로 지정합니다.

    case1: ThreadPoolExecutor(max_workers=)
    case2: PoolExecutor(max_workers=)
    """
    worker = min(20, len(NATION_LS))

    start_time = time.time()

    with futures.ThreadPoolExecutor(worker) as excutor:
        number_of_nation_column_count = excutor.map(
            save_nation_to_csv, iterable_nations
        )  # .map(func, iterables)

    end_time = time.time()

    spent_time = end_time - start_time

    # number_of_nation_column_count = get_length(NATION_LS)

    # csv로 정리한 국가 개수를 할당합니다.
    msg = "\n{} csv has been seperated in: {:.2f} seconds"  # 소수점 둘째 자리까지 콘솔에 찍어 준다.
    print(msg.format(len(list(number_of_nation_column_count)), spent_time))


if __name__ == "__main__":
    main(save_seperated_csvs)
