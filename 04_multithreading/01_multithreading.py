import time
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url:str):
    print(f"Fetching data from {url}")
    time.sleep(5)
    print(f"Data fetched from {url}")
    return f"Data from {url}"

url = [
    "https://api.example.com/data1",
    "https://api.example.com/data2",
    "https://api.example.com/data3",
    "https://api.example.com/data4",
    "https://api.example.com/data5",
]
results = []
with ThreadPoolExecutor(max_workers=len(url)) as executor:
    futures = executor.map(fetch_data, url)
    results.extend(futures)

print(results)

