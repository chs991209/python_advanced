import os
import time
import sys
import csv

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


def save_csv(data, file_name):  # 단수의 CSV 파일을 저장한다.
    path = os.path.join(DEST_DIR, file_name)

    with open(path, "w", newline="") as fp:  # newline => 빈 string으로 할당하면 줄바꿈 처리 안함
        writer = csv.DictWriter(fp, fieldnames=HEADER)

        writer.writeheader()  # csv.DictWriter.writeheader

        for row in data:
            writer.writerow(row)


# NOSQL data 형태로 csv에서 뽑아냅니다.
def get_sales_data(nation):
    with open(TARGET_CSV, "r") as f:
        reader = csv.DictReader(f)  # Dictionaries를 담은 reader를 call

        data = [
            r for r in reader if r["Country"] == nation
        ]  # Using List Comprehension # reader type은 list가 아니며, .map()이 없다.
        show_with_newline("\nData rows: {}".format(len(data)))
        return data


def show_with_newline(string):
    print(string)
    sys.stdout.flush()


def show(string):
    print(string, end="")
    sys.stdout.flush()


def get_seperated_csvs(nation_list):
    for nation in sorted(nation_list):
        show(nation)  # 단순히 국가 별로 진행 상황을 콘솔에 찍는다.
        data_of_sales_by_nation = get_sales_data(nation)

        save_csv(data_of_sales_by_nation, nation.lower() + ".csv")

    return data_of_sales_by_nation


# 합친 버전
# def get_seperated_csvs(nation_list):
#     def get_sales_data(nation):
#     with open(TARGET_CSV, 'r') as f:
#         reader = csv.DictReader(f)  # Dictionaries를 담은 array로 call
#
#         header_name = reader.fieldnames  # column의 목록을 call
#         print('\n Header names are: {}'.format(header_name))
#
#         # for r in reader:
#         #     if r['Country'] == nation:
#         #         data.append(r)
#
#         data = [r for r in reader if r['Country'] == nation]
#         print('\n Nation: {} Data rows: {}'.format(nation, len(data)))
#         return data


def get_length(nation_list):
    return len(nation_list)


def main(get_seperated_csvs, get_length):
    start_time = time.time()

    get_seperated_csvs(NATION_LS)

    end_time = time.time()

    spent_time = end_time - start_time

    # csv로 정리한 국가 개수를 할당합니다.
    number_of_nation_column_count = get_length(NATION_LS)

    msg = "\n{} csv has been seperated in: {:.2f} seconds"  # 소수점 둘째 자리까지 콘솔에 찍어 준다.

    print(msg.format(number_of_nation_column_count, spent_time))


if __name__ == "__main__":
    main(get_seperated_csvs, get_length)
