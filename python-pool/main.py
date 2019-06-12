from multiprocessing import Pool, current_process
import time

def worker(i):
    p = current_process()
    worker_index = p._identity[0] if p._identity else 0
    time.sleep(1)
    return worker_index, i

def main():
    with Pool() as pool:
        for w, i in pool.imap_unordered(worker, range(10)):
            print(f'{w}: {i}')

if __name__ == '__main__':
    main()
