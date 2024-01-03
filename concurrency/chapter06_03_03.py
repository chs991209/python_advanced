import os
import time
import sys
import csv
from concurrent import futures

from decorators.decorators import (
    log_dependency_by_flush,
    log_dependency,
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


# 국가별 CSV 파일 저장
def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)

    with open(path, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        # Header Write
        writer.writeheader()
        # Dict to CSV Write
        for row in data:
            writer.writerow(row)


# 국가별 분리
def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict을 리스트로 적재
        data = []
        # Header 확인
        # print(reader.fieldnames)
        for r in reader:
            # OrderedDict 확인
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data


# 중간 상황 출력
def show(text):
    print(text, end=' ')
    # 중간 출력(버퍼 비우기)
    sys.stdout.flush()


# 국가 별 분리 함수 실행
def separate_many(nt):
    # 분리 데이터
    data = get_sales_data(nt)
    # 상황 출력
    show(nt)
    # 파일 저장
    save_csv(data, nt.lower() + '.csv')

    return nt


# 시간 측정 및 메인함수
def main(separate_many):
    # worker 개수
    worker = min(20, len(NATION_LS))
    # 시작 시간
    start_tm = time.time()
    # futures
    futures_list = []
    # 결과 건수
    # ProcessPoolExecutor : GIL 우회, 변경 후 -> os.cpu_count()
    # ThreadPoolExecutor : GIL 종속
    with futures.ProcessPoolExecutor() as excutor:
        # Submit -> Callable 객체 스케쥴링(실행 예약) -> Future
        # Future -> result(), done(), as_completed() 주로 사용
        for nt in sorted(NATION_LS):
            # future 반환
            future = excutor.submit(separate_many, nt)
            # 스케쥴링
            futures_list.append(future)
            # 출력
            # print('Scheduled for {} : {}'.format(nt, future))
            # print()

        for future in futures.as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled
            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    # 종료 시간
    end_tm = time.time() - start_tm
    msg = '\n csv separated in {:.2f}s'
    # 최종 결과 출력
    # print(msg.format(list(futures_list), end_tm))
    print(msg.format(end_tm))


# 실행
if __name__ == '__main__':
    main(separate_many)