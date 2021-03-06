#!/usr/bin/env python3
import concurrent.futures
import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)

        
# def download_site(url):
#     response = requests.get(url)
#     print(f"Read {len(response.content)} from {url}")

        
# def download_all_sites(sites):
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
