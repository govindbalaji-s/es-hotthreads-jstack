import argparse
import datetime
import os
from typing import List

import requests

from ThreadInfo import ThreadInfo


def fetch_async(pid, location, num_hot_threads, num_jstacks, num_cat_tasks):
    hot_threads = []
    jstacks = []
    cat_tasks = []
    timestamp = "{:%Y_%m_%d_%H_%M_%S}".format(datetime.datetime.utcnow())
    os.system(f'mkdir -p dumps/{timestamp}')
    for i in range(num_jstacks):
        file = f'dumps/{timestamp}/jstack_{i}.txt'
        jstacks.append(file)
        os.system(f'jstack -l {pid} > {file}')

    for i in range(num_hot_threads):
        file = f'dumps/{timestamp}/hot_threads_{i}.txt'
        hot_threads.append(file)
        r = requests.get(f'http://{location}/_nodes/hot_threads')
        with open(file, 'w') as io_file:
            io_file.write(r.text)

    for i in range(num_cat_tasks):
        file = f'dumps/{timestamp}/cat_tasks_{i}.txt'
        cat_tasks.append(file)
        r = requests.get(f'http://{location}/_cat/tasks?detailed=true')
        with open(file, 'w') as io_file:
            io_file.write(r.text)

    return hot_threads, jstacks, cat_tasks


def main():
    argparser = argparse.ArgumentParser(
        description='Filter jstack dump by ES thread names found in /_nodes/hot_threads outputs')
    argparser.add_argument('pid', type=int)
    argparser.add_argument('--location', default='localhost:9200')
    argparser.add_argument('--num-hot-threads', type=int, default=1)
    argparser.add_argument('--num-jstacks', type=int, default=1)
    argparser.add_argument('--num-cat-tasks', type=int, default=1)
    # argparser.add_argument('--jstacks', nargs='+', required=True, help='jstack dump file')
    # argparser.add_argument('--hot-threads', nargs='+', required=True, help='List of hot_threads output files')
    # argparser.add_argument('--cat-tasks', nargs='+', required=False, help='List of cat tasks output files')
    argparser.add_argument('--top-threads', type=int, default=3, help='Number of top stacks to print, defaults to 3')
    argparser.add_argument('--min-cpu', type=float, default=0.,
                           help='Consider only the hot threads measure with minimum cpu usage '
                                '%%, defaults to 0')
    args = argparser.parse_args()
    hot_threads_files, jstacks_files, cat_tasks_files = fetch_async(args.pid, args.location, args.num_hot_threads,
                                                                    args.num_jstacks, args.num_cat_tasks)
    print_threads_info(hot_threads_files, jstacks_files, cat_tasks_files, args.min_cpu, args.top_threads)


def print_threads_info(hot_threads_files, jstacks_files, cat_tasks_files, min_cpu, top_threads):
    threads_info: List[ThreadInfo] = ThreadInfo.inner_join_files(hot_threads_files, jstacks_files, cat_tasks_files)
    for thread_info in threads_info:
        thread_info.filter_and_sort(min_cpu)
    threads_info.sort(key=lambda thread_info: thread_info.sort_key(), reverse=True)
    for i in range(min(top_threads, len(threads_info))):
        print(threads_info[i])


if __name__ == '__main__':
    main()
