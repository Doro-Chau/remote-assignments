import threading
from multiprocessing.dummy import Pool as ThreadPool
from time import sleep

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")

# rewrite everything inside this main function and keep others untouched
def main():
    p = ThreadPool(processes=5)
    result = p.map(do_job, range(5))
    
main()