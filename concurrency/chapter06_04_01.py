import timeit
import requests


urls = [
    "https://naver.com",
    "https://daum.net",
    "https://apple.co.kr",
    "https://github.com",
    "https://gmarket.co.kr",
]
from concurrent.futures import ThreadPoolExecutor
import threading
import asyncio
from decorators.decorators import log_dependency_by_flush, log_dependency


@log_dependency_by_flush
async def fetch(url, executor):
    print(
        "Thread Name : {}\nStart : {}\n".format(threading.current_thread().name, url)
    )  # .getName()은 deprecated'
    try:
        # loop 내 thread pool에 requests.get을
        # thread pool functions의 function arguments로 담는다.
        response = await loop.run_in_executor(executor, requests.get, url)

        # response = requests.get(url)
        # print(response.text[:len(response.text) // 500])
        # print(len(response.text[:len(response.text) // 500]))
        print(
            ">>> Thread Name : {}\nDone : {}\n ".format(
                threading.current_thread().name, url
            )
        )
        return response
    except Exception as err:
        print(
            ">>> Thread Name : {}\nError : {}".format(
                threading.current_thread().name, str(err)
            )
        )


@log_dependency
async def main():
    executor = ThreadPoolExecutor(max_workers=10)
    # futures = [asyncio.ensure_future(fetch(url) for url in urls)]
    # result = await asyncio.gather(*futures)
    result = await asyncio.gather(
        *(asyncio.ensure_future(fetch(url, executor)) for url in urls)
    )
    return result
    # with ThreadPoolExecutor(max_workers=5) as executor:
    #     executor.map(fetch, urls)


# for url in urls:
#     print('Start', url)
#     text = requests.get(url)
#     # if url.endswith('ac.kr'):
#     #     print(text.text)
#     # print('Content', text.text)
#     print('Done', url)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # custom_loop = CustomEventLoop()
    loop.run_until_complete(main())

    start = timeit.default_timer()
    # main()
    duration_time = timeit.default_timer() - start
    print(duration_time)
