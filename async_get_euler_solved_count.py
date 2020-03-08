import time
import json
import asyncio
import aiohttp
from bs4 import BeautifulSoup


urls = ['http://projecteuler.net/problem={}'.format(i)
        for i in range(1, 691)]


async def async_get(session, url):
    r = await session.request('GET', url=url, timeout=60)
    d = await r.content.read()
    return url, d


async def async_api_request(urls=urls):
    semaphore = asyncio.Semaphore(10)
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in urls:
                tasks.append(async_get(session=session, url=url))
            results = await asyncio.gather(*tasks)
            return results


def get_problem_number(url):
    return url.split('=')[-1]


def handle_response(content):
    content = content.decode()
    soup = BeautifulSoup(content, 'html.parser')
    section = str(soup.find_all('div')[0]).split(';')
    for text in section:
        if 'Solved by' in text:
            return int(text.split(' ')[-1])
    return


def handle_results(results):
    return {get_problem_number(url): handle_response(r)
            for url, r in results}


def download():
    start = time.time()
    results = async_api_request(urls)
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(results)
    records = handle_results(data)
    with open("project_euler_solve_counts.json", "w") as f:
        json.dump(records, f)
    end = time.time()
    print(f"Time taken: {round(end-start, 3)}s")
    return


if __name__ == "__main__":
    download()
