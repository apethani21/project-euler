import time
import json
import requests
from bs4 import BeautifulSoup


def get_problem_number(url):
    return url.split('=')[-1]


def get_problem_info(problem_number):
    url = f'http://projecteuler.net/problem={problem_number}'
    r = requests.get(url, timeout=1)
    content = r.content.decode()
    soup = BeautifulSoup(content, 'html.parser')
    section = str(soup.find_all('div')[0]).split(';')
    for text in section:
        if 'Solved by' in text:
            return int(text.split(' ')[-1])
    return


def download_results():
    start = time.time()
    results = {problem_number: get_problem_info(problem_number)
               for problem_number in range(1, 691)}
    with open("project_euler_solve_counts.json", "w") as f:
        json.dump(results, f)
    end = time.time()
    print(f"Time taken: {round(end-start, 3)}s")
    return


if __name__ == "__main__":
    download_results()
